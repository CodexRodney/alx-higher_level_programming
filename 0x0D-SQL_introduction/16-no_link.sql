-- lists all records of the table second_table
-- doesn't list rows without a name value
-- listed by descending score

SELECT score, name
FROM second_table
WHERE name <> 'NULL'
ORDER BY score DESC;
