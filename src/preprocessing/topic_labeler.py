import os
import pandas as pd
import google.generativeai as genai
import time

# configuring API key, initializing selected generative ai model
genai.configure(api_key="AIzaSyCkTDJidvCdoo3vSinFNLYutZV43pm_fBI")

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
)

# indicating the csv dataset containing the blog posts to classify, and transforming it into a dataframe
human_blog_posts_path = os.path.join("data", "human_blog_posts.csv")

df_human_blog_posts = pd.read_csv(human_blog_posts_path)

# initializing an empty list where to store all the thematic labels for the moment
topic_categories = []

# iterating over all the values (the blog post texts) within the column "blog_post" of the dataframe df_human_blog_posts
# send the blog post text to the model in order to classify it with respect to its main theme
# then retrieve the model's response (the thematic label)
for post in df_human_blog_posts['blog_post']:

    # configuring a prompt that changes dynamically incorporating the blog post text while iterating over the dataframe
    prompt = f"""ROLE: You are a classifier aimed to label written blog posts by Paul Graham with respect to their MAIN TOPIC/PURPOSE. 
    Thus, your goal is to identify the overarching topic/purpose of blog post text, focusing on its primary message. 
    
    LABELS YOU CAN USE:
    - life advice
    - career advice
    - technological and societal insights
    - programming advice
    - startup advice
    - social commentary
    - educational content
    - historical analysis
    - philosophical reflection
    - personal experience report
    - writing advice
    - other
    
    INSTRUCTIONS:
    1. Provide a structured and consistent output. OUTPUT ONLY THE LABEL REPRESENTING THE BLOG POST’S TOPIC/PURPOSE, 
    2. DO NOT ATTACH ANYTHING TO THE LABEL IN YOUR ANSWER (NO EXPLANATIONS, NO REFLECTIONS, NO INTRODUCTIONS). 
    3. Use only the provided list of labels. Use "other" when all the other labels do not apply to the text analyzed.

    
    RECAP: You are a blog post classifier aimed to output the label best representing the blog post topic/purpose. 
    You just have to output the label describing the topic/purpose in plain text with nothing else attached.
    You must use only the labels in the provided list. 
    Remember to stick to this output format answering with just the label and nothing else attached.
    
    Now, provide the classification for the following blog post: {post}"""
    
    # sending the prompt to the model, while configuring temperature and max_output_tokens
    response = model.generate_content(prompt,
    generation_config = genai.GenerationConfig(
        max_output_tokens=8000,
        temperature=0,
    ))
    
    model_output = response.text # retrieve the model response in plain text

    topic_categories.append(model_output) # adding the thematic label to the list

    print(f"topic category: {model_output} was added to the list") # checking the progression of the labeling task

    time.sleep(15) # adding some seconds of delay to avoid the overload of API requests

# adding a new column to the dataframe with the values from the list "topic categories"
df_human_blog_posts['topic_category'] = topic_categories

# to verify the overall process went through
print(df_human_blog_posts.head())

# save the updated dataset back to the csv file
df_human_blog_posts.to_csv(human_blog_posts_path, encoding="utf-8", index=False)

# giving a feedback on the completion of the process
print("human_blog_posts.csv was enriched with topics' labels and saved back to a csv file")