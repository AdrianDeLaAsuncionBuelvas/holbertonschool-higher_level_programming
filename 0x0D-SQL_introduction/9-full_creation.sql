-- script that creates a table second_table in the database hbtn_0c_0.

CREATE TABLE IF NOT EXISTS seccond_table (
       id INT,
       name VARCHAR(256),
       score INT
);
INSERT INTO first_table(id, name, score)
VALUES (1, 'John', 10,
       2, 'Alex', 3,
       3, 'Bod', 14,
       4, 'George', 8);
