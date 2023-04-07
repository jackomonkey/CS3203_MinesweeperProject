CREATE TABLE Players(username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL); --this creates the table for our game with the given columns 'username' and 'password';
INSERT INTO Players(username, password) VALUES ('test username', 'test password'); --this inserts a row into the table
SELECT * FROM Players; --this can give you a visual representation of the current data in the table
