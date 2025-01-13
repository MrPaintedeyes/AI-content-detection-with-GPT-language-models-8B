import os
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

# Paths to the JSON files
human_blog_posts_path = os.path.join("data", "human_blog_posts_processed.json")
ai_generated_blog_posts_path = os.path.join("data", "ai_generated_blog_posts_processed.json")

# loading the JSON datasets into pandas DataFrames
df_human = pd.read_json(human_blog_posts_path, orient="records")
df_ai = pd.read_json(ai_generated_blog_posts_path, orient="records")

# initializing lists to collect lemmas for both datasets
human_corpus_lemmas = []
ai_corpus_lemmas = []

# collecting lemmas from the lemmatized_blog_post column as an unified list of lists (all 'lemmatized_blog_post', which are lists of lemmas)
for lemmatized_blog_post in df_human['lemmatized_blog_post']:
    human_corpus_lemmas.extend(lemmatized_blog_post)

for lemmatized_blog_post in df_ai['lemmatized_blog_post']:
    ai_corpus_lemmas.extend(lemmatized_blog_post)

# counting the occurrences of each lemma in the unified lists for both corpora
human_corpus_lemmas_count = Counter(human_corpus_lemmas)
ai_corpus_lemmas_count = Counter(ai_corpus_lemmas)

# computing the 100 most common lemmas in each corpus
most_common_human_corpus_lemmas = human_corpus_lemmas_count.most_common(100)
most_common_ai_corpus_lemmas = ai_corpus_lemmas_count.most_common(100)

# extracting the sets of lemmas from the most common lists...
human_lemmas_set = set([lemma for lemma, frequency in most_common_human_corpus_lemmas])
ai_lemmas_set = set([lemma for lemma, frequency in most_common_ai_corpus_lemmas])

# ...to find the intersection of the two sets and calculating the percentage of lemmas' overlap
common_lemmas = human_lemmas_set.intersection(ai_lemmas_set)
lemmas_overlap_percentage = (len(common_lemmas) / 100) * 100

# checking the number and percentage of lemmas in common, and printing the lemmas in common, hoping is more than 30% (percentage set as )
print(f"Number of lemmas in common: {len(common_lemmas)}")
print(f"Percentage of lemmas' overlap: {lemmas_overlap_percentage}%")
print(f"The most common and shared lemmas are the following: {common_lemmas}")

if lemmas_overlap_percentage > 30: # checking if corpora similarity passed the baseline of 30%
    print("the two corpora are similar enough from a lexical POV according to our predefined baseline (30% of shared most frequent lemmas)")

# creating the "plot" folder if it doesn't exist yet, and declaring the saving path for graphs
os.makedirs("plot", exist_ok=True)

ai_lemmas_plot_path = os.path.join("plot", "top_100_ai_corpus_lemmas.png")
human_lemmas_plot_path = os.path.join("plot", "top_100_human_corpus_lemmas.png")

# separating most common lemmas from their counts by iterating over most_common_[human/AI]_corpus_lemmas
# to retrieve the lemma, we just need to select the first element (idx 0) of each pair
# while to retrieve the frequency, we just need to select the second element (idx 1) of each pair

lemmas_human = [pair[0] for pair in most_common_human_corpus_lemmas] # lemmas
frequencies_human = [pair[1] for pair in most_common_human_corpus_lemmas] # frequencies

lemmas_ai = [pair[0] for pair in most_common_ai_corpus_lemmas] # lemmas
frequencies_ai = [pair[1] for pair in most_common_ai_corpus_lemmas] # frequencies

# plotting most common lemmas for the human and AI corpora to visualize lexical similarity
plt.figure(figsize=(12, 7))
plt.bar(range(len(lemmas_human)), frequencies_human, color='green')
plt.xticks(range(len(lemmas_human)), lemmas_human, rotation=90, fontsize=8)
plt.title("top 100 most common lemmas in human corpus", fontsize=14)
plt.xlabel("lemmas", fontsize=12)
plt.ylabel("frequency", fontsize=12)
plt.savefig(human_lemmas_plot_path)
plt.show()


plt.figure(figsize=(13, 8))
plt.bar(range(len(lemmas_ai)), frequencies_ai, color='red')
plt.xticks(range(len(lemmas_ai)), lemmas_ai, rotation=90, fontsize=8)
plt.title("top 100 most common lemmas in AI corpus", fontsize=14)
plt.xlabel("lemmas", fontsize=12)
plt.ylabel("frequency", fontsize=12)
plt.savefig(ai_lemmas_plot_path)
plt.show()

# Observations about overlap in lemmas:
# topic similarity is evident in certain keywords like startup, founder, company, idea, people, user, work, language, writing etc.
# as these are completely aligned with Paul Graham's focus as a writer, philosophy major, tecg startup founder/investor and computer scientist.
# we should consider also the relevance of the personal pronoun "I", since the majority of blog posts from Paul Graham are in first person