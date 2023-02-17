-- a script that list all records with a scoree >=10 in the second_table in the database hbtn_0c_0

SELECT score, name FROM second_table WHERE >= 10 ORDER BY score DESC;
