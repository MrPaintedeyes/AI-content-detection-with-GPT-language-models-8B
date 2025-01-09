README: AI Content Detection Using GPT-based Models
Overview
This project investigates the ability of Generative Pretrained Transformer (GPT)-based language models to differentiate between human and AI-generated texts. The focus is on exploring both zero-shot and few-shot learning techniques to establish a low-resource, reliable detection method. The study centers on blog posts by Paul Graham to represent human-generated content and uses Google’s gemini-1.5-fast model to create a matching dataset of AI-generated texts.

Through a lexicon analysis and classification tasks, the project examines the thematic and stylistic similarities between the two datasets and evaluates the performance of GPT-based models. The results demonstrate the superior performance of few-shot learning over zero-shot learning for AI content detection.

Key Objectives
Dataset Creation: Collect human-generated blog posts and generate AI-matching texts.
Lexicon Analysis: Evaluate the linguistic similarity between human and AI-generated datasets.
Content Classification: Use zero-shot and few-shot learning methods to classify the content.
Performance Evaluation: Compare accuracy, precision, and recall of the two approaches.
Project Structure
Data
The project leverages blog posts authored by Paul Graham as the human-generated dataset and uses the gemini-1.5-fast model to produce AI-generated content. The datasets are stored in the data directory:

data/raw: Contains unprocessed human and AI texts.
data/processed: Preprocessed datasets with labels and metrics for analysis.
data/generated: Outputs from the AI content generation process.
Workflow
Data Collection:

Scrape human-written content from Paul Graham's blog.
Generate AI content using gemini-1.5-fast with parameters tuned to mimic the human dataset's style and themes.
Preprocessing:

Normalize, tokenize, and lemmatize the text using NLP techniques.
Save processed datasets for analysis and classification tasks.
Lexicon Analysis:

Compare word usage and thematic distributions across datasets.
Content Classification:

Employ zero-shot learning and few-shot learning using the gemini-1.5-fast model to classify human and AI content.
Measure performance metrics such as accuracy, recall, and precision.
Visualization:

Generate bar plots and other visualizations to illustrate the lexicon and thematic trends.
Results
The key findings of this project include:

Lexicon Analysis: Confirmed linguistic similarity between the human and AI datasets, validating the effectiveness of the AI text generation process.
Classification Performance:
Zero-shot learning achieved low accuracy (~2%).
Few-shot learning significantly outperformed zero-shot, achieving up to 60% accuracy with improved precision and recall.
These results establish a baseline for GPT-based AI text detection and highlight the importance of few-shot learning in low-resource settings.

## Repository Structure

plaintext
ai_detection/
├── data/
│   ├── raw/                    # Raw datasets
│   ├── processed/              # Preprocessed datasets
│   └── generated/              # AI-generated texts
│
├── notebooks/
│   ├── exploration.ipynb       # Data exploration and lexicon analysis
│   └── results.ipynb           # Results and performance evaluation
│
├── src/
│   ├── scraping/               # Scraping implementation for human content
│   ├── preprocessing/          # Text preprocessing scripts
│   ├── linguistic/             # Lexicon and thematic analysis
│   ├── generation/             # AI text generation with gemini-1.5-fast
│   ├── classification/         # Zero-shot and few-shot classification tasks
│   ├── evaluation/             # Performance metrics computation
│   └── frontend/               # Optional visualization tools (if implemented)
│
├── tests/
│   ├── test_scraping.py        # Tests for scraping functionality
│   ├── test_preprocessing.py   # Tests for preprocessing scripts
│   ├── test_linguistic.py      # Tests for linguistic analysis
│   ├── test_generation.py      # Tests for AI text generation
│   ├── test_classification.py  # Tests for classification models
│   └── test_evaluation.py      # Tests for evaluation metrics
│
├── paper/
│   ├── main.tex                # LaTeX paper source
│   ├── figures/                # Figures for the paper
│   └── bibliography.bib        # References
│
├── requirements.txt            # Python dependencies
├── setup.py                    # Installation script
├── run_pipeline.py             # Main script to execute the entire pipeline
└── README.md                   # Project documentation


## Setup Instructions
Prerequisites
Python 3.8 or higher
Access to the gemini-1.5-fast API
Required Python packages (see requirements.txt)
Installation
Clone the repository:

bash
Copia codice
git clone https://github.com/yourusername/ai_detection.git
cd ai_detection
Install dependencies:

bash
Copia codice
pip install -r requirements.txt
Set up API keys and configuration files for the gemini-1.5-fast model.

Running the Pipeline
To execute the full pipeline:

bash
Copia codice
python run_pipeline.py
This script will:

Scrape human content.
Generate AI content.
Perform preprocessing, lexicon analysis, classification, and evaluation.
Future Work
Fine-Tuning GPT Models: Fine-tune an LLM to mimic Paul Graham’s voice and test audience detection of human vs. AI content.
Extended Analysis: Apply the methods to other datasets or domains for a broader evaluation.
License
This project is licensed under the MIT License. See LICENSE for details.
