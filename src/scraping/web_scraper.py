import urllib
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup
import csv
import os
import pandas as pd

# fetching an high-level webpage within Paul Graham's website, where there is a complete list of all his blog posts ("content directory")

try:
    html_content_directory = urlopen("https://www.paulgraham.com/articles.html")
except urllib.request.URLError as e:
    print("there was an URLError, try with a different URL")

# parsing the webpage requested

soup_content_directory = BeautifulSoup(html_content_directory, "lxml")

# visualizing the parsed webpage to understand its structure and where the blog posts' links are included (uncomment if needed)
# print(soup_content_directory.prettify())

# initializing an empty list of articles' links

articles = []

# identifying all the blog post links 
# with structure "https://www.paulgraham.com/" + the string inside the attribute href of each filtered element <a>

for a in soup_content_directory.find_all('a'):
    article_link = "https://www.paulgraham.com/" + a['href']

    # skipping all the links not related to the blog posts:
    # link to the home page, to the rss feed or that don't end with "html"

    if "index.html" in article_link or "rss.html" in article_link or not article_link.endswith("html"):
        continue

# appending each correctly identified article's link to the list "articles"
        
    articles.append(article_link)

    #printing the retrieved link to verify that each iteration is working (uncomment if needed)
    # print(article_link)

# printing all the retrieved links to verify that retrieval worked (uncomment if needed)
# print(articles)

# looking at the structure of a typical blog post page, by fetching it, parsing it and visualizing it 
# to understand where the blog post text is included within the html structure (uncomment if needed)
# test_link = articles[0]
# html_test = urlopen(test_link)
# soup_test = BeautifulSoup(html_test, "lxml")
# print(soup_test.prettify())

human_blog_posts_data = []  # initializing a list of (URL, content body) pairs to convert into a csv later

# actually scraping blog posts' content
# implementing the fetching, parsing and collection of all blog post texts related to the stored links (iterating over links)
# knowing that the main text is within the element <body>

for link in articles:
    try:
        html_blog_post = urlopen(link)
        soup_blog_post = BeautifulSoup(html_blog_post, "lxml")
        blog_post_body = soup_blog_post.body # the content of body is the blog post text mixed with other html elements we don't need
        blog_post_text = blog_post_body.get_text() # so we apply bs4 method "get_text()" to retrieve all the textual content of the body
        human_blog_posts_data.append((link, blog_post_text)) # adding to the list human_blog_posts_data the pair (URL + text)
    except urllib.request.URLError as e:
        print("there was an URLError, try with a different URL")

# creating the dataset where to store data in the target directory "data"
human_blog_posts_path = os.path.join("data", "human_blog_posts.csv")

os.makedirs(os.path.dirname(human_blog_posts_path), exist_ok=True)

# saving human_blog_posts_data the data into a csv file with columns: URL, blog_post, author, AI_or_human

with open(human_blog_posts_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file) # initializing writer
    writer.writerow(["URL", "blog_post", "author", "AI_or_human"]) # writing the columns names (first row)
    for URL, blog_post in human_blog_posts_data: # writing the other rows, including each pair (URL + blog post) + author name + "human" label in a single row
        writer.writerow([URL, blog_post , "Paul Graham", "human"])

# checking that the process went through (uncomment if needed)
print("human_blog_posts_data have been saved to a csv file, including also the variables 'author' and 'AI_or_human'")

# exploring the dataset with pandas, in particular searching for empty values
df_human = pd.read_csv(human_blog_posts_path)

human_blog_posts_path = os.path.join("data", "human_blog_posts.csv")

df_human = pd.read_csv(human_blog_posts_path)

# exploring human_blog_posts.csv structure, entries counts, values' types and emppty values
print(df_human.describe)
print(df_human.info)
print(df_human.isna().sum())

# drop rows with empty values in them
df_human.dropna(inplace=True)

# take a look at potential changes in count
print(df_human.tail)

# and save the df back to csv without the super annoying index
df_human.to_csv(human_blog_posts_path, index=False)