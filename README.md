# LinkedIn Lexicon and Thematic Analysis of topvoice
## Abstract
This project seeks to analyze the linguistic patterns and thematic trends in the LinkedIn posts of [niche speaker]. The primary goals are to identify the lexicon used, uncover the main themes of communication, and track how these elements have evolved over a specified time window. We aim to create insights into professional communication styles and their changes over time. Optionally, we will explore fine-tuning a large language model (LLM) to generate content mimicking the [niche speaker] and test audience detection between human and machine-generated content. Data will be scraped from LinkedIn using the API and processed using NLP techniques, with visualizations provided for clarity.

## Research Questions
What is the lexicon of [niche speaker] on LinkedIn?
What are the main themes of [niche speaker]'s posts on LinkedIn?
How did the lexicon and themes change over the last [time window]?
Can we fine-tune an LLM to mimic the [niche speaker]'s voice?
Can [niche speaker]'s audience detect the difference between human and machine-generated content?

## Dataset
The primary dataset will consist of LinkedIn posts from the [niche speaker], collected manually or via the LinkedIn API. 
Up to three profiles can be scraped, and the data will be stored in posts.csv. 
The posts will undergo pre-processing (tokenization, lemmatization) using NLTK, and the processed data will be saved in preprocessed_posts.csv. 
We will utilize the gemini-1.5-flash API for thematic analysis iterating the model over the rows of posts.csv. 
The dataset size will vary depending on the time window, but each post will include timestamps for longitudinal analysis.

## A Tentative List of Milestones for the Project
#### Week 1-2:
Scraping LinkedIn posts and storing raw data in posts.csv.
Pre-processing (tokenization + lemmatization) of text data using NLTK.
Assigned to [Team Member 1]
#### Week 3-4:
Perform thematic analysis using gemini-1.5-flash API and store themes in preprocessed_posts.csv.
Assigned to [Team Member 2]
#### Week 5:
Analyze and visualize lexicon and theme trends over the selected time window (barplots).
Assigned to [Team Member 1 & 2]
#### Week 6-7 (Optional):
Fine-tune an LLM based on the speaker's voice and create a basic test for audience recognition of human vs. machine-generated content.
Assigned to [Team Member 3]

## Documentation
The repository will contain:
- Data folder: Raw and preprocessed datasets (posts.csv, preprocessed_posts.csv).
- Scripts folder: Python scripts for data scraping, preprocessing, and analysis.
- Results folder: Lexicon and theme visualizations (barplots).
- Instructions to reproduce the results, including setting up the NLP pipeline and utilizing the gemini-1.5-flash API for thematic analysis, will be provided. Steps for fine-tuning the LLM (optional) will also be included if that part is attempted.
