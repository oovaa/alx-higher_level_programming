-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

SELECT id , name FROM cities WHERE state_id = 1
