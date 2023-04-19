CREATE TABLE Users(username VARCHAR(50) NOT NULL, password VARCHAR(50) NOT NULL, time INT); --this creates the table for our game with the given columns 'username', 'password', and a time slot;
INSERT INTO Players(username, password) VALUES ('test username', 'test password', 0); --this inserts a row into the table
SELECT * FROM Users; --this can give you a visual representation of the current data in the table
SELECT time FROM Users WHERE username = '$username' AND password = '$password' --selects the time of the given row where 'username' and 'password' are found
