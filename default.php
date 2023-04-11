<!DOCTYPE html>
<html>
<head>
	<title>Your Mine Will Be Swept! </title>
	<style>
		body {
			background-image: url("minesweeper.jpg");
			background-size: cover;
			background-position: center;
			background-repeat: no-repeat;
		}

		form {
			margin: auto;
			width: 50%;
			padding: 10px;
			background-color: white;
			border-radius: 10px;
			box-shadow: 0px 0px 10px grey;
		}

		label {
			display: block;
			font-weight: bold;
			margin-top: 10px;
		}

		input {
			display: block;
			width: 100%;
			padding: 10px;
			margin-top: 5px;
			border-radius: 5px;
			border: none;
			box-shadow: 0px 0px 5px grey;
		}

		input[type="submit"] {
			background-color: red;
			color: white;
			font-size: 18px;
			font-weight: bold;
			padding: 10px;
			margin-top: 20px;
			border: none;
			border-radius: 5px;
			cursor: pointer;
			box-shadow: 0px 0px 5px grey;
		}
	</style>
</head>
<body>
	<h1>Your Mine Will Be Swept!</h1>
	<p>This is a super simple website created using HTML.</p>
	<ul>
		<li>Item 1</li>
		<li>Item 2</li>
		<li>Item 3</li>
	</ul>
	<form action="process_form.php" method="post">
	    <label for="username">Username:</label>
	    <input type="text" id="username" name="username" required>
	    <br>
	    <label for="password">Password:</label>
	    <input type="password" id="password" name="password" required>
	    <br>
	    <input type="submit" value="Submit">
    </form>
</body>
</html>
