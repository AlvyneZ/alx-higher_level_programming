-- A script that lists all records (score then name and sorted by score) of
--  the table second_table of the database hbtn_0c_0
--  Leaves out records without name
SELECT `score`, `name` FROM second_table
    WHERE `name` IS NOT NULL
    ORDER BY `score` DESC;
