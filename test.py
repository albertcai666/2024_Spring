# import numpy
print("hello world")
lst = ["a","b","c"]
for index, element in enumerate(lst):
    print(str(index)+", "+element)


storage_account = spark.conf.get("storage_account")
silver_container = spark.conf.get("silver_container")
gold_container = spark.conf.get("gold_container")

wfm_silver = f"abfss://{silver_container}@{storage_account}.dfs.core.windows.net/wfm"

# SHOW SCHEMAS;

