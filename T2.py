result_df = new_sql_df1.union(new_uvc_df1)
pandas_df = result_df.toPandas()
x = 0
for column in pandas_df:
    if pandas_df[column][0] != pandas_df[column][1]:
        pandas_df.loc[2, column] = "False"
    else:
        pandas_df.loc[2, column] = "T"
    x += 1

sparkDF = spark.createDataFrame(pandas_df.astype(str)) # view of pandas df is ugly, want all data types to String
sparkDF.display()  

aB2OM00000071H70AI
aB2OM00000072Y90AI
aB2OM0000007BRl0AM
aB2OM0000007BTN0A2
aB2OM0000007Dwb0AE
aB2OM0000007EW50AM
aB2OM0000007HiT0AU
aB2OM0000007P9l0AE
aB2OM0000007Q0z0AE
aB2OM0000007Q5p0AE
aB2OM0000007SE50AM
aB2OM0000007XvJ0AU