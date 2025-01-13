import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import os
import string

# tokenization, removing stop words, lemmatization, word count (propedeutic for data analysis and visualization)

# downloading necessary NLTK data
nltk.download("stopwords")

# file paths to the datasets with human- and ai-generated blog posts
human_blog_posts_path = os.path.join("data", "human_blog_posts.csv")
ai_generated_blog_posts_path = os.path.join("data", "ai_generated_blog_posts.csv")

# loading the datasets as dataframes
df_human = pd.read_csv(human_blog_posts_path)
df_ai = pd.read_csv(ai_generated_blog_posts_path)

# normalizing blog posts' text, and adding the normalized texts as the values of a new column "normalized_blog_post", in both datasets
df_human['normalized_blog_post'] = df_human['blog_post'].str.lower()
df_ai['normalized_blog_post'] = df_ai['blog_post'].str.lower()

print("performed normalization on both datasets and saved outputs in a new column 'normalized_blog_post'") # checking on the completion of the process

# tokenizing normalized blog posts' text, and adding the tokenized texts as the values of a new column "tokenized_blog_post", in both datasets
tokenized_human_posts = []
for human_post in list(df_human['blog_post']):
    tokenized_human_post = nltk.tokenize.word_tokenize(human_post)
    tokenized_human_posts.append(tokenized_human_post)
df_human['tokenized_blog_post'] = tokenized_human_posts

tokenized_ai_posts = []
for ai_post in list(df_ai['blog_post']):
    tokenized_ai_post = nltk.tokenize.word_tokenize(ai_post)
    tokenized_ai_posts.append(tokenized_ai_post)
df_ai['tokenized_blog_post'] = tokenized_ai_posts

print("Performed tokenization on both datasets and saved outputs in a new column 'tokenized_blog_post'") # checking


# cleaning of blog post texts, namely stop word and punctuation remotion, in both datasets
stop_words = set(stopwords.words("english")) # set of stop words
punctuation = string.punctuation # list of punctuation characters

cleaned_human_posts = []
for tokenized_human_post in list(df_human['tokenized_blog_post']):
    filtered_tokens = [token for token in tokenized_human_post if token not in stop_words and token not in punctuation]
    cleaned_human_posts.append(filtered_tokens)
df_human['cleaned_blog_post'] = cleaned_human_posts

cleaned_ai_posts = []
for tokenized_ai_post in list(df_ai['tokenized_blog_post']):
    filtered_tokens = [token for token in tokenized_ai_post if token not in stop_words and token not in punctuation]
    cleaned_ai_posts.append(filtered_tokens)
df_ai['cleaned_blog_post'] = cleaned_ai_posts

print("removed stop words from tokenized blog posts, and saved the outputs in a separate column 'blog_post_no_stop_words") # checking

# lemmatization of cleaned blog posts in both datasets
lemmatized_human_posts = []

for cleaned_human_post in df_human['cleaned_blog_post']:
    lemmatized_human_post = []
    for token in cleaned_human_post:
        lemma = nltk.WordNetLemmatizer().lemmatize(token)
        lemmatized_human_post.append(lemma)
    lemmatized_human_posts.append(lemmatized_human_post)  # Append here, inside the outer loop

df_human['lemmatized_blog_post'] = lemmatized_human_posts

lemmatized_ai_posts = []

for cleaned_ai_post in df_ai['cleaned_blog_post']:
    lemmatized_ai_post = []
    for token in cleaned_ai_post:
        lemma = nltk.WordNetLemmatizer().lemmatize(token)
        lemmatized_ai_post.append(lemma)
    lemmatized_ai_posts.append(lemmatized_ai_post)

df_ai['lemmatized_blog_post'] = lemmatized_ai_posts

print("performed lemmatization on both datasets, and saved the output in a new column 'blog_post_lemmatized'") # checking

# saving processed datasets to json files to preserve lists of lemmas (df series "lemmatized_blog_post")

human_blog_posts_json_path = os.path.join("data", "human_blog_posts_processed.json")
ai_blog_posts_json_path = os.path.join("data", "ai_generated_blog_posts_processed.json")

df_human.to_json(human_blog_posts_json_path, orient = 'records')
df_ai.to_json(ai_blog_posts_json_path, orient = 'records')

print("both datasets were saved, and all the processing (normalization, tokenization, lemmatization) went through") # checking