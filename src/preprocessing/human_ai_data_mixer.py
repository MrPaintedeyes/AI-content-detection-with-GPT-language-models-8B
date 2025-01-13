import pandas as pd
import os
import random
import csv

# loading human- and ai-generated datasets into dataframes, plus declaring the mixed dataset path...
human_blog_posts_path = os.path.join("data", "human_blog_posts.csv")
ai_blog_posts_path = os.path.join("data", "ai_generated_blog_posts.csv")
ai_human_blog_posts_path = os.path.join("data", "ai_human_blog_posts.csv")

df_human = pd.read_csv(human_blog_posts_path)
df_ai = pd.read_csv(ai_blog_posts_path)

# ...that it's created if it doesn't exist yet
if not os.path.exists(ai_human_blog_posts_path):
    with open(ai_human_blog_posts_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["blog_post", "topic_category", "AI_or_human"]) # writing the header

# to compile the mixed dataset in a way it is balances, we unify all the 100 ai-generated blog posts to 100 random human blog posts,
# while preserving topics' percentages
# so we iterate over each topic category, compute the number of needed human blog posts for that category (= to the number of ai-blog-posts), 
# and randomly sample that number of human blog posts from df_human[df_human['topic_category]==category][blog_post]

# Initialize lists to store mixed data as df series (df['series'] = list)
blog_posts = []
topic_categories = []
authors = []
ai_or_human = []

# Iterate over each topic category
categories = set(df_ai["topic_category"])

for category in categories:
    # Compute the number of AI blog posts for the current category
    num_ai_blog_posts_per_category = len(df_ai[df_ai["topic_category"] == category])
    
    print(f"We should add {num_ai_blog_posts_per_category} human blog posts for the category {category}")  # Progression check

    # Sample human-generated content for the current category
    human_contents = df_human[df_human["topic_category"] == category]['blog_post']
    sampled_human_contents = random.sample(list(human_contents), num_ai_blog_posts_per_category)
    
    # add sampled human blog posts to lists, along with the labels for "topic category" and "AI_or_human"
    blog_posts.extend(sampled_human_contents)
    topic_categories.extend([category for element in range(num_ai_blog_posts_per_category)])
    ai_or_human.extend(["human" for element in range(num_ai_blog_posts_per_category)])

# adding all ai-generated blog posts to the previous lists, before populating the corresponding dataframe series of df_mixed
mixed_blog_posts = blog_posts + list(df_ai['blog_post'])
mixed_topic_categories = topic_categories + list(df_ai['topic_category'])
mixed_ai_or_human = ai_or_human + list(df_ai["AI_or_human"])

# populating the dataframe df_mixed, declaring as many dataframe series as the number of mixed lists we created before
# and saving the new dataframe as a csv file in the target path

df_mixed = pd.DataFrame({
    'blog_post': mixed_blog_posts,
    'topic_category': mixed_topic_categories,
    'AI_or_human': mixed_ai_or_human})

df_mixed.to_csv(ai_human_blog_posts_path, index=False, encoding="utf-8")

print("ai_human_blog_posts.csv was successfully created.") # checking if it went through