# IMDb movie reviews 

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, trim

spark = SparkSession.builder.appName("MovieReviews").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# load data
df = spark.read.csv(
    "data/IMDB_Dataset.csv",
    header=True,
    inferSchema=True,
    multiLine=True,
    escape='"'
)

# schema and first 5 rows
df.printSchema()
df.show(5)

# remove null
clean_df = df.filter(col("review").isNotNull() & (trim(col("review")) != ""))

# total reviews
print("Total reviews:", clean_df.count())

#positive and negative count
clean_df.groupBy("sentiment").count().show()

#add review length
clean_df = clean_df.withColumn("review_length", length(col("review")))

#reviews longer than 500 chars
long_reviews = clean_df.filter(col("review_length") > 500)
print("Reviews longer than 500:", long_reviews.count())
long_reviews.show(5)

#save to csv
clean_df.coalesce(1).write.csv("output/cleaned_reviews", header=True, mode="overwrite")
print("Saved")

spark.stop()
