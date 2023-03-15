-- list all privileges of the MySQL specified users
SELECT DISTINCT CONCAT("'" , user , "'@'", host , "'") AS user_host,
       CONCAT("SHOW GRANTS FOR '", user , "'@'", host , "';") AS query
FROM mysql.user
WHERE user IN ('user_0d_1', 'user_0d_2');