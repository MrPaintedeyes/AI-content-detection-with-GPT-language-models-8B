import pandas as pd
import os
import matplotlib.pyplot as plt

# loading the two datasets as dataframes to handle further data analysis and visualization
human_blog_posts_path = os.path.join("data", "human_blog_posts.csv")
ai_blog_posts_path = os.path.join("data", "ai_generated_blog_posts.csv")

df_human = pd.read_csv(human_blog_posts_path)
df_ai = pd.read_csv(ai_blog_posts_path)

# iterating over topic category within the dataframes, filtering all the entries with the corresponding topic value
human_topic_categories = set(df_human['topic_category'])
ai_topic_categories = set(df_ai['topic_category'])

# then counting the number of entries presenting that topic value
# computing the percentage of entries with that topic
# and filling data into a dict, for both dataframes
human_topic_percentages = {}
for topic in human_topic_categories:
    topic_count = len(df_human[df_human['topic_category'] == topic])
    topic_percentage = topic_count / len(df_human) * 100
    human_topic_percentages[topic] = topic_percentage

print(human_topic_percentages) # checking if it went through and the structure of the dict

ai_topic_percentages = {}
for topic in ai_topic_categories:
    topic_count = len(df_ai[df_ai['topic_category'] == topic])
    topic_percentage = topic_count / len(df_ai) * 100
    ai_topic_percentages[topic] = topic_percentage

print(ai_topic_percentages) # checking if it went through and the structure of the dict

# plotting and saving human topics' percentages and ai topics' percentages in two separate figures
plt.figure(figsize=(10, 6))
plt.bar(human_topic_percentages.keys(), human_topic_percentages.values(), color='blue')
plt.title("topics' prcentages in the human dataset")
plt.xlabel("topics")
plt.ylabel("percentages")
plt.xticks(rotation = 45, fontsize = 10)
plt.tight_layout()

# saving the figures in the plot folder, creating it if it doesn't exist yet
os.makedirs("plot", exist_ok=True)

human_plot_path = os.path.join("plot", "human_topics_percentages.png")
plt.savefig(human_plot_path)
plt.show() # checking by showing

# repeating the same for ai_generated_blog_posts.csv

plt.figure(figsize=(10, 6))
plt.bar(ai_topic_percentages.keys(), ai_topic_percentages.values(), color='orange')
plt.title("topics' percentages in the AI dataset")
plt.xlabel("topics")
plt.ylabel("percentages")
plt.xticks(rotation = 45, fontsize = 10)
plt.tight_layout()

ai_plot_path = os.path.join("plot", "ai_topics_percentages.png")
plt.savefig(ai_plot_path)
plt.show()

# we can visually confirmed that the topics' percentages are the same within both datasets, 
# and the ai-based generation pipeline respected the human blog posts' quotas provided