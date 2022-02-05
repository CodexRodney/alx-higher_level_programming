-- Lists all records of second_table of database hbtn_0c_0
-- Lists the scores >= 10 in table second_table
SELECT score, name
FROM  second_table
WHERE score >= 10
ORDER BY score DESC;
