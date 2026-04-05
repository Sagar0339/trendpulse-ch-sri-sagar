# trendpulse-ch-sri-sagar
# TrendPulse Project

This project is about building a simple data pipeline using Python.
It collects trending stories from HackerNews and processes them step by step.

---

## Project Flow

Task 1 → Task 2 → Task 3 → Task 4
Fetch → Clean → Analyse → Visualize

---

## Files in this Project

* task1_data_collection.py
* task2_data_processing.py
* task3_analysis.py
* task4_visualization.py

Also folders:

* data/ → stores JSON and CSV files
* outputs/ → stores charts

---

## Task Details

### Task 1

Fetched top stories from HackerNews API and saved them as JSON file.
Also categorized stories into technology, worldnews, sports, science and entertainment.

### Task 2

Loaded JSON file and cleaned the data using pandas.
Removed duplicates, handled missing values and saved as CSV.

### Task 3

Used pandas and numpy for analysis.
Calculated average score, comments and added new columns like engagement and is_popular.

### Task 4

Created charts using matplotlib:

* Top 10 stories by score
* Stories per category
* Score vs comments

Also created a dashboard combining all charts.

---

## How to Run

Run the files in order:

```bash
python task1_data_collection.py
python task2_data_processing.py
python task3_analysis.py
python task4_visualization.py
```

---

## Output

* Cleaned CSV file
* Analysed CSV file
* Charts saved in outputs folder

---

## Tools Used

* Python
* Pandas
* NumPy
* Matplotlib
* Requests

---

## Conclusion

This project helped me understand how to build a data pipeline from collecting data to visualization.
