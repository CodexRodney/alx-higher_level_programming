-- lists the number of records with the same score in the table second_table
SELECT score, COUNT(score) AS number 
FROM second_table
WHERE score = score
GROUP BY score
ORDER BY score DESC;
