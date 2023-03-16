-- script that creates the table force_name
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
UPDATE force_name SET name='Python is cool' WHERE id=1;
INSERT INTO force_name (id, name) VALUES (2, 'Holberton School');
SELECT * FROM force_name;