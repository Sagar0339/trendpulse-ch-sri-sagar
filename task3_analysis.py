import pandas as pd
import numpy as np

# load cleaned csv file
file_path = "data/trends_clean.csv"

try:
    df = pd.read_csv(file_path)
    print("Loaded data:", df.shape)
except:
    print("Error loading file")
    df = pd.DataFrame()

# print first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# basic averages
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score  :", avg_score)
print("Average comments:", avg_comments)

# -------- NumPy Analysis --------

scores = df["score"].values  # converting to numpy array

print("\n--- NumPy Stats ---")

# mean, median, std deviation
print("Mean score   :", np.mean(scores))
print("Median score :", np.median(scores))
print("Std deviation:", np.std(scores))

# max and min
print("Max score    :", np.max(scores))
print("Min score    :", np.min(scores))

# category with most stories
cat_counts = df["category"].value_counts()
top_category = cat_counts.idxmax()
print("\nMost stories in:", top_category, "(", cat_counts.max(), "stories )")

# story with most comments
max_comments_row = df.loc[df["num_comments"].idxmax()]
print("\nMost commented story:", max_comments_row["title"], " — ", max_comments_row["num_comments"], "comments")

# -------- Adding New Columns --------

# engagement = comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular = score > average score
df["is_popular"] = df["score"] > avg_score

# -------- Save the new file --------

output_file = "data/trends_analysed.csv"
df.to_csv(output_file, index=False)

print("\nSaved to", output_file)