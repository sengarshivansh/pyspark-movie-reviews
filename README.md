# PySpark Movie Reviews

Homework 1.2 for Data and Story Telling. Basic PySpark code to process the IMDb movie review dataset.

## Dataset

IMDb Dataset of 50K Movie Reviews from Kaggle:
https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

The dataset is not uploaded here because it is too big. Download it, unzip it and keep it as `data/IMDB_Dataset.csv`.

## What the code does

1. Loads the CSV file into a PySpark DataFrame
2. Prints the schema and shows the first 5 rows
3. Removes rows with null or empty reviews
4. Counts the total reviews and the number of positive and negative reviews
5. Adds a `review_length` column and shows reviews longer than 500 characters
6. Saves the cleaned and transformed data as a new CSV file in `output/cleaned_reviews`

## How to run

Needs Python and Java 17.

```
pip install pyspark
python movie_reviews.py
```

## Output

- Total reviews: 50,000
- Positive: 25,000 and Negative: 25,000
- Reviews longer than 500 characters: 45,017
