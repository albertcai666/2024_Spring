
unmatch = []
list_eval = ['aB2OM00000071H70AI','aB2OM00000072Y90AI','aB2OM0000007BRl0AM','aB2OM0000007BTN0A2','aB2OM0000007Dwb0AE','aB2OM0000007EW50AM','aB2OM0000007HiT0AU','aB2OM0000007P9l0AE','aB2OM0000007Q0z0AE','aB2OM0000007Q5p0AE','aB2OM0000007SE50AM','aB2OM0000007XvJ0AU']

for e in list_eval:
    new_sql_df.createOrReplaceTempView('merged_quality2')
    new_sql_df2=spark.sql(
    f"""select distinct * EXCEPT( Dw_Createduserid, Dw_Lastupdateduserid, Dw_Createdtime, Dw_Lastupdatedtime, Overall_Score, Questions, Answer)
        from merged_quality2
        where Evaluation_Id = '{e}'
    """)
    new_uvc_df.createOrReplaceTempView('merged_quality3')
    new_uvc_df2=spark.sql(
    f"""--select distinct *
        select distinct * EXCEPT(Questions, Answer)
        from merged_quality3
        where Evaluation_Id = '{e}'
    """)
    compar = []
    result_df2 = new_sql_df2.union(new_uvc_df2) # union
    result_df2.display()
    lst = result_df2.collect() # array of Row objects  
    for z in range(len(result_df2.columns)):
        if pd.isnull(pandas_df[column][0]) and pd.isnull(pandas_df[column][1]): # both null value
            continue
        if lst[0][z] != lst[1][z]:
            unmatch_multi[result_df2.columns[z]] = e

unmatch_set = set(unmatch)
print(unmatch_set) 

fact: incremental __loader_
refresh everyday: dim table
# can apache spark support parallel processing if pandas dataframe is used in each iteration
# runtime for pandas df is 3 mins
actual procedure

verintwfm_raw_container: dim table
start_time already converted, line 34