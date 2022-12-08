.read data.sql


CREATE TABLE bluedog AS
SELECT color, pet
FROM students
WHERE color = "blue"
  AND pet = "dog"
;

CREATE TABLE bluedog_songs AS
SELECT color, pet, song
FROM students
WHERE color = "blue"
  AND pet = "dog"
;


CREATE TABLE smallest_int_having AS
SELECT time, smallest
FROM students
GROUP BY smallest
HAVING COUNT(*) = 1
ORDER BY smallest
;


CREATE TABLE matchmaker AS
SELECT a.pet, a.song, a.color, b.color
FROM students AS a,
     students AS b
WHERE a.pet = b.pet
  AND a.song = b.song
  AND a.time < b.time
;


CREATE TABLE sevens AS
SELECT seven
FROM students AS s,
     numbers AS n
WHERE s.time = n.time
  AND s.number = 7
  AND n."7" = "True"
;


CREATE TABLE average_prices AS
SELECT category, AVG(MSRP) AS average_price
FROM products
GROUP BY category
;


CREATE TABLE lowest_prices AS
SELECT
;


CREATE TABLE shopping_list AS
SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";


CREATE TABLE total_bandwidth AS
SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

