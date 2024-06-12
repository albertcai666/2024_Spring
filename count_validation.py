SELECT year(created_date), count(*)
FROM merge_quality
GROUP BY year(created_date)
ORDER BY year(created_date)


SELECT month(created_date), count(*)
FROM merge_quality
WHERE year(created_date) = 2024
GROUP BY month(created_date)
ORDER BY month(created_date)

SELECT day(created_date), count(*)
FROM merge_quality
WHERE year(created_date) = 2023 AND month(created_date) = 5
GROUP BY day(created_date)
ORDER BY day(created_date)

SELECT Evaluation_Id, count(*)
FROM merge_quality
WHERE created_date = "2024-05-10"
GROUP BY Evaluation_Id
ORDER BY Evaluation_Id

SELECT Answer,Questions
FROM merge_quality
WHERE created_date = "2024-04-19" AND Evaluation_Id = "aB2OM000000A3kb0AC"
ORDER BY Questions

SELECT *
FROM merge_quality
WHERE eval_id IN ("213630345", "213630348", "213630349", "213630472")

SELECT id, Evaluation_Form__c
FROM merge_quality
WHERE Evaluation_Form__c not IN ('Chat Evaluation', 'Email Evaluation')

select * EXCEPT(Dw_Createduserid, Dw_Lastupdateduserid, Dw_Createdtime, Dw_Lastupdatedtime, Wire_Type) 

select count(*) from(
    SELECT distinct eval_id 
    FROM merge_quality) AS abc

--- curation.verintquality

SELECT DISTINCT Evaluation_Id, System_Start_Time
FROM merge_quality
WHERE year(System_Start_Time) = 2024 AND month(System_Start_Time) = 5
GROUP BY System_Start_Time, Evaluation_Id
ORDER BY date(System_Start_Time)

SELECT year(System_Start_Time), count(*)
FROM merge_quality
GROUP BY year(System_Start_Time)
ORDER BY year(System_Start_Time)

SELECT month(System_Start_Time), count(*)
FROM merge_quality
WHERE year(System_Start_Time) = 2024
GROUP BY month(System_Start_Time)
ORDER BY month(System_Start_Time)

SELECT year(Evaluation_Datetime_Indexed), count(*)
FROM merge_quality
GROUP BY year(Evaluation_Datetime_Indexed)
ORDER BY year(Evaluation_Datetime_Indexed)

SELECT Answer,Questions
FROM merge_quality
WHERE source_system = "Salesforce" and date(CreatedTime) = "2023-11-24" AND Evaluation_Id = "aB2OM0000004okb0AA"
ORDER BY Questions

SELECT month(CreatedTime), count(*)
FROM merge_quality
WHERE source_system = "Salesforce" and year(CreatedTime) = 2024
GROUP BY month(CreatedTime)
ORDER BY month(CreatedTime)

CreatedTime is more accurate

SELECT AFF_Compliance_Error_s__c, LastModifiedDate, CreatedDate, etl_load_time 
FROM merge_quality
WHERE id = "aB2OM0000004okb0AA"

select * EXCEPT(Dw_Createduserid, Dw_Lastupdateduserid, Dw_Createdtime, Dw_Lastupdatedtime, Wire_Type) 
    from merged_quality 
    --where Created_Date between '2024-05-01' AND '2024-05-31'
    where Evaluation_Id = "213629664"
    ORDER BY Questions

    