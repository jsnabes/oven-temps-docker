import pyspark
from pyspark.sql import SparkSession

BOOTSTRAP_SERVERS = "localhost:29092"
TOPIC = "oven"

def main():
    # spark = SparkSession.builder.master("local[1]") \
    #     .appName('OvenTempReader') \
    #     .getOrCreate()

    spark = SparkSession.builder.master("local[1]") \
        .appName('OvenTempReader') \
        .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1') \
        .getOrCreate()

    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", BOOTSTRAP_SERVERS) \
        .option("session.timeout.ms", "4000") \
        .option("subscribe", TOPIC) \
        .load()

    query = df.selectExpr("CAST(value AS STRING)") \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    main()