import tkinter as tk

def get_input():
    user = entry_user.get()
    password = entry_password.get()
    sendData(user,password)

root = tk.Tk()
root.title("Login Page")

# Set window size and position
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# Create frame
frame = tk.Frame(root, padx=50, pady=50, bg='white')
frame.pack(expand=True, fill='both')

# Create login label and entry field
label_user = tk.Label(frame, text="Username:", font=('Helvetica', 18), fg='black', bg='white')
label_user.grid(row=0, column=0, padx=20, pady=20)
entry_user = tk.Entry(frame, font=('Helvetica', 18))
entry_user.grid(row=0, column=1, padx=20, pady=20)

# Create password label and entry field
label_password = tk.Label(frame, text="Password:", font=('Helvetica', 18), fg='black', bg='white')
label_password.grid(row=1, column=0, padx=20, pady=20)
entry_password = tk.Entry(frame, show="*", font=('Helvetica', 18))
entry_password.grid(row=1, column=1, padx=20, pady=20)

# Create login button
button_login = tk.Button(frame, text="Submit", font=('Helvetica', 18), bg='black', fg='white', command=get_input) # note there needs tp be a command here to destroy window
button_login.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

import mysql.connector

#pip install mysql-connector-python (installing the package)
# https://www.whatismyip.com/ //add this on your hostinger remote tab






def sendData(String1, String2):
    
  mydb = mysql.connector.connect(
  host="86.38.202.204",
  user="u351964368_root",
  password="SoftwareEngineering3203",
  database="u351964368_SoftwareEngr"
)
  cursor = mydb.cursor()


  sql = "INSERT INTO Users (username, password, time) VALUES (%s, %s, %s)"
  val = (String1, String2, 21) #instead of food the variable
  cursor.execute(sql, val)




  mydb.commit()


  mydb.close()


    




# Set focus on username field
entry_user.focus()

root.mainloop()
