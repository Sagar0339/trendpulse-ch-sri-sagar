import pandas as pd
import os
from datetime import datetime

# getting today's file name (same pattern as task 1)
file_name = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

# load json file into dataframe
try:
    df = pd.read_json(file_name)
    print("Loaded", len(df), "stories from", file_name)
except:
    print("Error loading file")
    df = pd.DataFrame()

# remove duplicate post_id
before = len(df)
df = df.drop_duplicates(subset=["post_id"])
print("After removing duplicates:", len(df))

# remove rows with missing important fields
df = df.dropna(subset=["post_id", "title", "score"])
print("After removing nulls:", len(df))

# convert score and num_comments to integer
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# remove low quality posts (score < 5)
df = df[df["score"] >= 5]
print("After removing low scores:", len(df))

# remove extra spaces in title
df["title"] = df["title"].str.strip()

# save cleaned data to csv
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)

print("\nSaved", len(df), "rows to", output_file)

# print number of stories per category
print("\nStories per category:")
print(df["category"].value_counts())