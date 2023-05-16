-- A script that lists all records (score then name and sorted by score) of
--  the table second_table of the database hbtn_0c_0 with a score >= 10
SELECT `score`, `name` FROM second_table
    WHERE `score`>=10
    ORDER BY `score` DESC;
