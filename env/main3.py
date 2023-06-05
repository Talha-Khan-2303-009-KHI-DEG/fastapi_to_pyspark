import requests
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType, StructField, ArrayType


url = "https://tasty.p.rapidapi.com/recipes/list"
querystring = {"from": "0", "size": "20", "tags": "under_30_minutes"}
headers = {
    "X-RapidAPI-Key": "43f261cfb8msh07b4a9375ae71bap1da682jsn95323af568fd",
    "X-RapidAPI-Host": "tasty.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

spark = SparkSession.builder.appName("FastAPI to PySpark").getOrCreate()
    # Define the schema for the data
schema = StructType([
    StructField("count", IntegerType(), True),
    StructField("results", ArrayType(StructType([
        StructField("name", StringType(), True),
        StructField("description", StringType(), True)
        ])), True),
    ])
count = data.get("count")
results = data.get("results")
    # Create the PySpark DataFrame
rows = [(count, results)]
df = spark.createDataFrame(rows, schema)
    # Select the "name" and "description" columns from the "results" column
result_data = df.select("results.name", "results.description").collect()
result_list = []
    
for row in result_data:
    names = row["name"]
    descriptions = row["description"]
        # Iterate over each name and description in the results array
    for name, description in zip(names, descriptions):
        result_list.append({"name": name, "description": description})
    
# Stop the Spark session
    
spark.stop()

