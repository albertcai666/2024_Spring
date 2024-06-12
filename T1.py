
unmatch = []
list_eval = ['aB2OM00000071H70AI','aB2OM00000072Y90AI','aB2OM0000007BRl0AM','aB2OM0000007BTN0A2','aB2OM0000007Dwb0AE','aB2OM0000007EW50AM','aB2OM0000007HiT0AU','aB2OM0000007P9l0AE','aB2OM0000007Q0z0AE','aB2OM0000007Q5p0AE','aB2OM0000007SE50AM','aB2OM0000007XvJ0AU']
for e in list_eval:
    new_sql_df.createOrReplaceTempView('merged_quality')
    new_sql_df2=spark.sql(
    """select distinct * EXCEPT(Questions, Answer, Dw_Createduserid, Dw_Lastupdateduserid, Dw_Createdtime, Dw_Lastupdatedtime)
        from merged_quality 
        where Evaluation_Id = '{e}'
    """)
    new_uvc_df.createOrReplaceTempView('merged_quality1')
    new_uvc_df1=spark.sql(
    """select distinct * EXCEPT(Questions, Answer)
        from merged_quality1
        where Evaluation_Id = '{e}'
    """)

    compar = []
    result_df2 = new_sql_df2.union(new_uvc_df1) # union
    lst = result_df.collect() # array of Row objects  
    for z in range(len(result_df2.columns)):
        if lst[0][z] != lst[1][z]:
            unmatch.append(result_df2.columns[z])

unmatch_set = set(unmatch)
print(unmatch_set) 
