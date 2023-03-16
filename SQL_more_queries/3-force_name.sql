-- script that creates the table force_name
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO force_name (id, name) VALUES (1, 'Force A') ON DUPLICATE KEY UPDATE name = 'Force A';