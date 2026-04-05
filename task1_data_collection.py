import requests
import json
import os
import time
from datetime import datetime

# header required by API
headers = {"User-Agent": "TrendPulse/1.0"}

# API URLs
top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# categories with keywords to match in title
categories = {
    "technology": ["AI", "software", "tech", "code", "computer", "data", "cloud", "API", "GPU", "LLM"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["NFL", "NBA", "FIFA", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "NASA", "genome"],
    "entertainment": ["movie", "film", "music", "Netflix", "game", "book", "show", "award", "streaming"]
}

# function to find category based on title keywords
def get_category(title):
    title = title.lower()  # convert to lowercase for easy matching
    for cat in categories:
        for word in categories[cat]:
            if word.lower() in title:
                return cat
    return None  # if no keyword matches

# getting top story ids from HackerNews
try:
    res = requests.get(top_url, headers=headers)
    ids = res.json()
except:
    print("Error getting top stories")
    ids = []

# only take first 500 ids
ids = ids[:500]

final_data = []

# keeping count of stories per category
count = {
    "technology": 0,
    "worldnews": 0,
    "sports": 0,
    "science": 0,
    "entertainment": 0
}

# storing current time for all records
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# OPTIMIZED: Loop through each story ID once, fetch it once, then categorize it
for i in ids:
    # fetch each story details
    try:
        r = requests.get(item_url.format(i), headers=headers)
        story = r.json()
    except:
        print("error in story", i)
        continue

    # skip if no title present
    if story is None or "title" not in story:
        continue

    # find which category this story belongs to
    cat = get_category(story["title"])

    # only save if category is found and we haven't collected 25 for that category yet
    if cat and count[cat] < 25:
        obj = {
            "post_id": story.get("id"),
            "title": story.get("title"),
            "category": cat,
            "score": story.get("score", 0),  # default 0 if not present
            "num_comments": story.get("descendants", 0),
            "author": story.get("by"),
            "collected_at": time_now
        }

        final_data.append(obj)
        count[cat] += 1  # increase count

# wait 2 seconds after each category fetching is done
for cat in categories:
    time.sleep(2)

# create data folder if not exists
if not os.path.exists("data"):
    os.mkdir("data")

# filename with today's date
filename = "data/trends_" + datetime.now().strftime("%Y%m%d") + ".json"

# save data into json file
with open(filename, "w") as f:
    json.dump(final_data, f, indent=4)

# print final result
print("Collected", len(final_data), "stories. Saved to", filename)