<?php
// Connect to the MySQL database
$servername = "localhost";
$username = "u351964368_root";
$password = "SoftwareEngineering3203";
$dbname = "u351964368_SoftwareEngr";

$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}

// Retrieve data submitted from the username and password fields
$username = $_POST['username'];
$password = $_POST['password'];

// Validate and sanitize the data
$username = mysqli_real_escape_string($conn, $username);
$password = mysqli_real_escape_string($conn, $password);

// Insert the data into the specific table in the database
$sql = "INSERT INTO Players (username, password) VALUES ('$username', '$password')";

if (mysqli_query($conn, $sql)) {
  echo "Data inserted successfully!";
} else {
  echo "Error inserting data: " . mysqli_error($conn);
}

// Close the database connection
mysqli_close($conn);
?>
