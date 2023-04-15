<?php
// Retrieve the username and password entered by the user

// Connect to your MySQL database
$servername = "localhost";
$username = "u351964368_root";
$password = "SoftwareEngineering3203";
$dbname = "u351964368_SoftwareEngr";
$conn = new mysqli($servername, $username, $password, $dbname);

$username = $_POST["username"];
$password = $_POST["password"];

$username = mysqli_real_escape_string($conn, $username);
$password = mysqli_real_escape_string($conn, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Execute a SELECT statement to retrieve the row from the Users table that matches the entered username and password
$sql = "SELECT time FROM Users WHERE username = '$username' AND password = '$password'";
$result = $conn->query($sql);

// If a matching row is found, extract the value of the time column from the row
if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $time_value = $row["time"];
    // Modify the HTML output to display the time value
    echo "The time for user " . $username . " is " . $time_value;
} else {
    echo "No matching user found";
}

// Close the database connection
$conn->close();
?>
