#Login page designed by Nicholas Rodriguez, modified by Isaac Stein to fit with the rest of the project.

import tkinter as tk

class MineLogin():
   
  def submit_pressed(self):
    username = self.get_username()
    hashed_password = self.get_hashed_password() #TODO: ENSURE HASHING HAPPENS!

    self.ui.store_login(username, hashed_password)
    ## TODO: CHECK LOGIN BEFORE WE MOVE ON! ENSURE LOGIN IS VALID! SET UP SOME SORT OF SYSTEM FOR THAT!

    self.frame.destroy()
    self.ui.build_game()

  def get_username(self):
    user = self.entry_user.get()
    return user
    
  def get_hashed_password(self): 
    # Gets the password, but hashed, hopefully.

    # TODO: HASH THE PASSWORD BEFORE WE STORE IT!
    password = self.entry_password.get()

    return password

  def __init__(self, root, ui):

    self.ui = ui

    # Create self.frame
    self.frame = tk.Frame(root, padx=50, pady=50, bg='white')
    self.frame.pack(expand=True, fill='both')

    # Create login label and entry field
    label_user = tk.Label(self.frame, text="Username:", font=('Helvetica', 18), fg='black', bg='white')
    label_user.grid(row=0, column=0, padx=20, pady=20)
    self.entry_user = tk.Entry(self.frame, font=('Helvetica', 18))
    self.entry_user.grid(row=0, column=1, padx=20, pady=20)

    # Create password label and entry field
    label_password = tk.Label(self.frame, text="Password:", font=('Helvetica', 18), fg='black', bg='white')
    label_password.grid(row=1, column=0, padx=20, pady=20)
    self.entry_password = tk.Entry(self.frame, show="*", font=('Helvetica', 18))
    self.entry_password.grid(row=1, column=1, padx=20, pady=20)

    # Create login button
    button_login = tk.Button(self.frame, text="Submit", font=('Helvetica', 18), bg='black', fg='white', command=self.submit_pressed) # note there needs tp be a command here to destroy window
    button_login.grid(row=2, column=0, columnspan=2, padx=20, pady=20)  

    root.mainloop()
