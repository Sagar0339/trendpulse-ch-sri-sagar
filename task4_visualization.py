import pandas as pd
import matplotlib.pyplot as plt
import os

# load analysed data
file_path = "data/trends_analysed.csv"

try:
    df = pd.read_csv(file_path)
except:
    print("Error loading file")
    df = pd.DataFrame()

# create outputs folder if not exists
if not os.path.exists("outputs"):
    os.mkdir("outputs")

# -------- Chart 1: Top 10 stories by score --------

# sort and take top 10
top10 = df.sort_values(by="score", ascending=False).head(10)

# shorten long titles
top10["title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure(figsize=(8,6))
plt.barh(top10["title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")

plt.gca().invert_yaxis()  # highest score on top

plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# -------- Chart 2: Stories per category --------

cat_counts = df["category"].value_counts()

plt.figure(figsize=(6,5))
plt.bar(cat_counts.index, cat_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.close()

# -------- Chart 3: Score vs Comments --------

plt.figure(figsize=(6,5))

# split data into popular and non-popular
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.close()

# -------- Bonus: Dashboard --------

fig, axs = plt.subplots(1, 3, figsize=(18,5))

# chart 1 in dashboard
axs[0].barh(top10["title"], top10["score"])
axs[0].set_title("Top Stories")
axs[0].invert_yaxis()

# chart 2 in dashboard
axs[1].bar(cat_counts.index, cat_counts.values)
axs[1].set_title("Categories")

# chart 3 in dashboard
axs[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axs[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axs[2].set_title("Score vs Comments")
axs[2].legend()

plt.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in outputs/ folder")