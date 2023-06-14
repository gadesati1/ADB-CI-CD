# Databricks notebook source
# Databricks notebook source
df = spark.sql("select * from samples.nyctaxi.trips")
df.display()

