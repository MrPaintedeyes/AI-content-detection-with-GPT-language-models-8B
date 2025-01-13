import pandas as pd
import google.generativeai as genai
import os
import random
import csv
import time

# indicating the path to the blog post examples and to the dataset with ai-generated texts
# if ai_generated_blog_posts.csv doesn't exist yet, it is created with columns "blog_post", "author", "AI_or_human", and "topic_category"

blog_posts_examples_path = os.path.join("data", "human_blog_posts.csv")

ai_blog_posts_path = os.path.join("data", "ai_generated_blog_posts.csv")

if not os.path.exists(ai_blog_posts_path):
    with open(ai_blog_posts_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["blog_post", "author", "AI_or_human", "topic_category"])

# the dataset with human blog posts is transformed into a dataframe, to randomly retrieve blog post examples to embed in the prompt

df_human = pd.read_csv(blog_posts_examples_path)

# after we set the number of synthetic blog posts to craft (100)
number_synthetic_contents = 100

# we can compute the percentage of each topic in the original dataset 
# to dinamically adjust the amount of synthetic content to produce for each category
# and produce a dataset of ai-generated blog posts that is balanced and representative with respect to human_blog_posts.csv

categories = set(df_human["topic_category"])

# configuring API key and selecting the generative model
genai.configure(api_key="AIzaSyCkTDJidvCdoo3vSinFNLYutZV43pm_fBI")

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
)

# dinamically changing the prompt with different blog posts examples randomly extracted within each topic category
# this should decrease the influence of specific examples on the quality of the generation

for category in categories:

    topic_percentage = len(df_human[df_human["topic_category"] == category]) / len(df_human)
    
    # calculate the number of synthetic contents to generate for each topic category
    number_of_contents_per_category = round(topic_percentage * number_synthetic_contents)
    
    print(f"generating: {number_of_contents_per_category} entries for {category}") # getting feedback on the process' start

    # iterating over each predicted generation round
    for i in range(1, (number_of_contents_per_category+1)):

        content_list = list(df_human[df_human["topic_category"] == category]["blog_post"])

        sample_content_examples = []

        # 3 human blog posts are extracted from the human_blog_posts.csv dataset and listed in sample_content_examples,
        # but if the number of examples within a topic category is less than 3,
        # all the examples in that category are listed in sample_content_examples
        if len(content_list) >= 3:
            sample_content_examples = random.sample(content_list, 3) # randomly lists 3 blog posts from the human blog posts
        else:
            sample_content_examples = content_list

        # setting a prompt that changes dinamically while different content examples are sampled at each generation round
        prompt = f"Write a blog post as Paul Graham would do. Look at the following 3 examples within the topic category {category} as a reference for tone of voice, style, structure, lenght and main topic/purpose. Do not plagarize the examples repeating their wording and content, but only look at them as models. Examples: {sample_content_examples}. You should just output the new blog post in plain text, with nothing else attached. Return the blog post as plain text only, and NO JSON, NO extra formatting or NO explanations are needed. Just output the blog post in plain text. Remember to adhere strictly to the output format (blog post only in plain text). Remember to look at the examples as models, but do not plagarize them."

        # sending the prompt to the model, while configuring also its temperature to 1 (enhancing creativity and variety) and the max number of tokens
        response = model.generate_content(
                prompt, 
                generation_config = genai.GenerationConfig(
                      max_output_tokens=100000,
                      temperature=1,
                )
        )

        # checking the progression of generation for the current topic category
        print(f"writing {i}° piece of content for the category {category}")
        
        # retrieving the model's response as plain text
        blog_post_text = response.text

        # adding and saving progressively the output in the target dataset "ai_generated_blog_posts.csv", respecting columns order
        with open(ai_blog_posts_path, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([blog_post_text, "gemini-1.5-fast", "AI", category])
        
        time.sleep(5) # avoid to overcome API requests' limits by adding some seconds of delay between model's calls
    
    
#checking on the completion of the task and on the dataframe 5 first rows
print("content generation completed, blog posts saved into ai_generated_blog_posts.csv")

# exploring ai_generated_blog_posts.csv structure, entries' counts, values' types
df_ai = pd.read_csv(ai_blog_posts_path)

print(df_ai.info)

# and saving df_ai back to csv as ai_generated_blog_posts.csv without the super annoying index
df_ai.to_csv(ai_blog_posts_path, index=False)