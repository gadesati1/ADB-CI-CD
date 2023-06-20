# Databricks notebook source
# Databricks notebook source
diamonds = (spark.read
  .format("csv")
  .option("header", "true")
  .option("inferSchema", "true")
  .load("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv")
)

diamonds.write.format("delta").mode("overwrite").save("/mnt/delta/diamonds")

#testing line added
