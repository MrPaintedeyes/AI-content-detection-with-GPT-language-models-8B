import os
import time
import random
import pandas as pd
import google.generativeai as genai

# loading datasets from csv to df
mixed_blog_posts_path = os.path.join("data", "ai_human_blog_posts.csv")
human_blog_posts_path = os.path.join("data", "human_blog_posts.csv")
ai_blog_posts_path = os.path.join("data", "ai_generated_blog_posts.csv")

df_mixed = pd.read_csv(mixed_blog_posts_path)
df_human = pd.read_csv(human_blog_posts_path)
df_ai = pd.read_csv(ai_blog_posts_path)

# configuring API key and selecting generative language model
genai.configure(api_key="AIzaSyCkTDJidvCdoo3vSinFNLYutZV43pm_fBI")

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
)

# initializing a list where we store classification results
classification_results = []

# iterating over the dataframe rows thanks to .iterrows() to pass each blog post to the model for classification
for index, row in df_mixed.iterrows():
    
    post = row["blog_post"] # dinamically identify the blog post to classify within each row

    # sampling 6 random blog posts' examples to guide the model's decision during the task
    human_blog_posts_examples = random.sample(list(df_human["blog_post"]), 3)
    ai_blog_posts_examples = random.sample(list(df_ai["blog_post"]), 3)

    # configuring a dynamic system prompt giving context, output formatting guidelines, instructions and blog posts examples for each category (AI, human), the prompt changes dinamically while examples are sampled  
    system_prompt = f"You are a AI-generated content detector aimed to classify blog post texts either as \"human\" if you think the blog post is human-generated, or \"AI\" if you think the blog post is AI-generated.\n\nTo guide the classification process, you can look at the following examples for both the categories:\n\nAI-generated content examples: \"\"\"\n{ai_blog_posts_examples}\n\"\"\"\n\nHuman-generated content examples:\"\"\"\n{human_blog_posts_examples}\n\"\"\"\n\n Your outout should contain just the classification result, namely the label representing your choice, with nothing else attached. The output format should be in plain text. \n\nLook at this output example to understand better how you should respond:\n\nIf the blog post text seems to you AI-generated -> OUTPUT = AI\nIf the blog post text seems to you human-generated -> OUTPUT = human\n\nRemember to consider content examples to guide your classification.\nRemember to strictly adhere to the mentioned output format (just the classification label in plain text and nothing else attached)."
    
    # configuring a dynamic user prompt, incorporating system prompt and the blog post to classify
    user_prompt = system_prompt + post

    # sending the prompt to the model while configuring temperature to 0 and max number of output tokens
    response = model.generate_content(
        user_prompt, 
        generation_config = genai.GenerationConfig(
        max_output_tokens=100000,
        temperature=0,
        ))
            
    classification_result = response.text # accessing the model response

    classification_results.append(classification_result) # storing the classification result in the list

    print(f"classified {index+1}° blog post -> result = {classification_result}")

    time.sleep(5) # adding some delay between calls to stay under API limits

df_mixed['classification_result_fewshot'] = classification_results # storing the results in a proper df column

# saving the updated df_mixed back to a csv file
df_mixed.to_csv(mixed_blog_posts_path, index=False, encoding="utf-8")

print("df_mixed successfully saved. Classification results for fewshot are stored.") # getting feedback if the process went through

print(df_mixed) # double-checking