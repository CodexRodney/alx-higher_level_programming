-- lists all cities contained in the databse hbtn_0d_usa
-- results sorted in ascending order

SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON states.id = cities.state_id;
