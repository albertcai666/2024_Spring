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

# result_df = new_sql_df1.unionByName(new_uvc_df1) # union
# lst = result_df.collect() # array of Row objects 
# for i in range(len(result_df.columns)):
#    if lst[0][i] != lst[1][i]:
#       unmatch.add(result_df.columns[i])
#       if type(lst[0][i]) == bool:
#          compar.append(False)
#       else:
#          compar.append("False")  # o/w incompatible data type
#    else:
#       if type(lst[0][i]) == bool:
#          compar.append(True)
#       else:
#          compar.append("T")
# compar_row = spark.createDataFrame([tuple(compar)])
# result_df = result_df.union(compar_row) 
