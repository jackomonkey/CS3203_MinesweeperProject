<?php
// Connect to your MySQL database
//When you use "localhost" as the servername, PHP knows to connect to 
//the MySQL server running on the same computer as the PHP script
$servername = "localhost";
//the username of the database
$username = "u351964368_root";
//the password to access the database with the specified user
$password = "SoftwareEngineering3203";
//the name of the database
$dbname = "u351964368_SoftwareEngr";
//establishes the connection to the database. 
//creates a new object of the mysqli class in PHP,
//which is used for connecting to a MySQL database.
//you can then execute query statements with $conn
$conn = new mysqli($servername, $username, $password, $dbname);
//The $_POST superglobal variable in PHP is an associative array that 
//contains data submitted to the server via an HTTP POST request. When a 
//form is submitted via POST, the data in the form is encoded and sent to the 
//server, which can then access the data using the $_POST variable. 
//Essentially, when you enter data into the 'username' and 'password' 
//fields on the website, that data is stored in these variables.
$username = $_POST["username"];
$password = $_POST["password"];

//Used for SQL injection attacks
//takes the data, sanitizes it and escapes special unneeded 
//characters, and stores the 'username' back in the 'username' field.
$username = mysqli_real_escape_string($conn, $username);
//takes the data, sanitizes it and escapes special unneeded 
//characters, and stores the 'password' back in the 'password' field.
$password = mysqli_real_escape_string($conn, $password);

// Checks if the connection to the server is valid.
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Execute a SELECT statement to retrieve the row from the Users table that matches the entered username and password
$sql = "SELECT time FROM Users WHERE username = '$username' AND password = '$password'";
//this result object will contain information about the rows and columns
//of data returned by the query, such as the number of rows and the names 
//and types of the columns. Returns a result set object that represents 
//the set of data returned by the mySQL query.
$result = $conn->query($sql);

// If a matching row is found, extract the value of the time column from the row
//checks if the table is populated with data.
if ($result->num_rows > 0) {
    //the $row variable now contains the row where the 
    //time that is needed is stored.
    $row = $result->fetch_assoc();
    //this statement retrieves the time with the specified row
    $time_value = $row["time"];
    
    echo "The time for user " . $username . " is " . $time_value;
} else {
    echo "No matching user found";
}

// Closes the database connection
$conn->close();
?>
