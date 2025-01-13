import pandas as pd
import os
import matplotlib.pyplot as plt
import json

# declaring the path to the mixed data and loading the data
mixed_blog_posts_path = os.path.join("data", "ai_human_blog_posts.csv")

df_mixed = pd.read_csv(mixed_blog_posts_path)

# stripping newlines from columns where values must be equal strings to compute classification results (true positives etc.)
df_mixed['classification_result_zeroshot'] = df_mixed['classification_result_zeroshot'].str.strip()
df_mixed['classification_result_fewshot'] = df_mixed['classification_result_fewshot'].str.strip()
df_mixed['AI_or_human'] = df_mixed['AI_or_human'].str.strip()

# initializing counts for TP, TN, FP, FN for zeroshot and fewshot learning
true_positives_zero = 0
true_negatives_zero = 0
false_positives_zero = 0
false_negatives_zero = 0

true_positives_few = 0
true_negatives_few = 0
false_positives_few = 0
false_negatives_few = 0

# iterating through each row in df_mixed to compare the row classification results with the annotated groundtruth (what was the blog post)
for index, row in df_mixed.iterrows():
    classification_zero = row['classification_result_zeroshot']
    classification_few = row['classification_result_fewshot']
    ground_truth = row['AI_or_human']

    if classification_zero == 'AI' and ground_truth == 'AI':
        true_positives_zero += 1
    if classification_few == 'AI' and ground_truth == 'AI':
        true_positives_few += 1
    if classification_zero == 'human' and ground_truth == 'human':
        true_negatives_zero += 1
    if classification_few == 'human' and ground_truth == 'human':
        true_negatives_few += 1
    if classification_zero == 'AI' and ground_truth == 'human':
        false_positives_zero += 1
    if classification_few == 'AI' and ground_truth == 'human':
        false_positives_few += 1
    if classification_zero == 'human' and ground_truth == 'AI':
        false_negatives_zero += 1
    if classification_few == 'human' and ground_truth == 'AI':
        false_negatives_few += 1

# computing performance metrics for zeroshot and fewshot learning following the standard formulas
accuracy_zero = (true_positives_zero + true_negatives_zero) / len(df_mixed)
precision_zero = (true_positives_zero / (true_positives_zero + false_positives_zero) if (true_positives_zero + false_positives_zero) > 0 else 0)
recall_zero = (true_positives_zero / (true_positives_zero + false_negatives_zero) if (true_positives_zero + false_negatives_zero) > 0 else 0)
F1_score_zero = (2 * (precision_zero * recall_zero) / (precision_zero + recall_zero) if (precision_zero + recall_zero) > 0 else 0)

# Compute metrics for fewshot
accuracy_few = (true_positives_few + true_negatives_few) / len(df_mixed)
precision_few = (true_positives_few / (true_positives_few + false_positives_few) if (true_positives_few + false_positives_few) > 0 else 0)
recall_few = (true_positives_few / (true_positives_few + false_negatives_few) if (true_positives_few + false_negatives_few) > 0 else 0)
F1_score_few = (2 * (precision_few * recall_few) / (precision_few + recall_few) if (precision_few + recall_few) > 0 else 0)

# storing classification results and performance metrics into dictionaries, comparing both approaches
classification_results = {
    'true positives zero-shot': true_positives_zero,
    'true positives few-shot': true_positives_few,
    'true negatives zero-shot': true_negatives_zero,
    'true negatives few-shot': true_negatives_few,
    'false positives zero-shot': false_positives_zero,
    'false positives few-shot': false_positives_few,
    'false negatives zero-shot': false_negatives_zero,
    'false negatives few-shot': false_negatives_few
}

performance_metrics = {
    'accuracy zero-shot': accuracy_zero,
    'accuracy few-shot': accuracy_few,
    'precision zero-shot': precision_zero,
    'precision few-shot': precision_few,
    'recall zero-shot': recall_zero,
    'recall few-shot': recall_few,
    'F1-score zero-shot': F1_score_zero,
    'F1-score few-shot': F1_score_few
}

print(classification_results) # looking at results
print(performance_metrics)

# store the results into json
classification_json_path = os.path.join("data", "model_classification_results.json")
with open(classification_json_path, 'w') as file:
    json.dump(classification_results, file)

metrics_json_path = os.path.join("data", "model_performance_metrics.json")
with open(metrics_json_path, 'w') as file:
    json.dump(performance_metrics, file)

# plotting classification results comparing both approaches, and saving the graph to the plot folder
classification_colors = ['cyan', 'pink', 'cyan', 'pink', 'cyan', 'pink', 'cyan', 'pink'] # defining colours for bars contrasting for the 2 approaches
performance_colors = ['purple', 'gray', 'purple', 'gray', 'purple', 'gray', 'purple', 'gray']

plt.figure(figsize=(10, 6))
plt.bar(classification_results.keys(), classification_results.values(), color=classification_colors)
plt.title("classification results: zeroshot vs fewshot")
plt.xlabel("classification results")
plt.ylabel("absolute counts")
plt.xticks(rotation = 45, fontsize = 10)
plt.tight_layout()

classification_results_plot_path = os.path.join("plot", "classification_results_zeroshot_vs_fewshot.png")
plt.savefig(classification_results_plot_path)
plt.show()

# plotting performance metrics comparing both approaches, and saving the graph to the plot folder
plt.figure(figsize=(10, 6))
plt.bar(performance_metrics.keys(), performance_metrics.values(), color=performance_colors)
plt.title("performance metrics: zeroshot vs fewshot")
plt.xlabel("performance metrics")
plt.ylabel("performance measurement")
plt.xticks(rotation = 45, fontsize = 10)
plt.tight_layout()

performance_metrics_plot_path = os.path.join("plot", "performance_metrics_zeroshot_vs_fewshot.png")
plt.savefig(performance_metrics_plot_path)
plt.show()