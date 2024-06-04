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
WHERE year(created_date) = 2024 AND month(created_date) = 5
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

