## Base made by Isaac Stein, using python's tkinter module and taking heavily from its documentation
## Sql connection designed by Nicholas Rodriguez
import tkinter
from PIL import ImageTk, Image
import mysql.connector

# Note: Need lipraries:
#pip install mysql-connector-python (installing the package)
# https://www.whatismyip.com/ //add this on your hostinger remote tab

class MineUI:
  
  def on_button_press(self, row, col):
    if not self.mine_map.map_generated: #if it is the first click, generate the map
      self.mine_map.generatemap(row, col)
      self.update_timer() # Timer starts when you first click.

    
    if self.mine_map.check_win():
      return
      
    if self.flag_mode:
      self.mine_map.toggle_flag(row, col) # change flag/unflag
      
      if self.mine_map.map[row][col].is_flagged: # Change color
        #self.map[row][col].configure(background = "red")
        self.map[row][col].configure(image=self.flag_icon)
      else:
        #self.map[row][col].configure(background = "white")
        #print("removing flag")
        self.map[row][col].configure(image=self.blank_icon)
      
    else:
      if (self.mine_map.map[row][col].revealed): # try not to open up to errors by revealing revealed cells.
        return
      elif (self.mine_map.map[row][col].is_flagged): # don't punish misclicks.
        return

      ## at this point, we start normal behavior, main loop stuff.
      
      self.map[row][col].destroy() # Get rid of that button!
      cell_neighbors = self.mine_map.reveal_cell(row, col) # Update the sub-surface stuff

       # Replace it with a label that has no interaction!
      if (self.mine_map.return_cell_status(row, col) == 'B'): #Bomb if bomb
        tkinter.Label(self.frm, image=self.bomb_icon).grid(row=row+3, column=col)
      else: # Otherwise, appropriate number
        tkinter.Label(self.frm, image=self.num_pictures[self.mine_map.return_cell_status(row, col)]).grid(row=row+3, column=col)
      
      
      if cell_neighbors == 0: #if cell has no neighbors
        # reveal neighboring cells.
        
        #check the ones up top, trying not to hit errors
          if ((row - 1) >= 0):
            if ((col - 1) >= 0):
              self.on_button_press(row-1, col-1)
  
            self.on_button_press(row-1, col)
            
            if ((col + 1) < self.map_size):
              self.on_button_press(row-1, col+1)
      
          #Check the middle ones, still dodging errors. Skip self.
          if ((col - 1) >= 0):
            self.on_button_press(row, col-1)
              
          if ((col + 1) < self.map_size):
            self.on_button_press(row, col+1)
      
          #Check bottom ones, again avoiding boundaries. 
          if ((row + 1) < self.map_size):
            if ((col - 1) >= 0):
              self.on_button_press(row+1, col-1)
      
            self.on_button_press(row+1, col)
              
            if ((col + 1) < self.map_size):
              self.on_button_press(row+1, col+1)
      if self.mine_map.check_lose():
        #A bit of a ramshackle solution, but I reckon it won't cause problems. Hopefully.
        self.lose()
      elif self.mine_map.check_win():
        self.win()

  def lose(self):
    tkinter.Label(self.top, text="You lost!").grid(column=int(self.map_size/2), row=1)
    #for rows in range(0, self.map_size): ## results in too many recursions? or too much recurstion depth? something like that. :'( ## if it worked, would reveal the map after you lost.
      #for columns in range(0,self.map_size):
        #self.on_button_press(rows, columns)
    
  def win(self):
    self.finish_time = int(self.mine_map.get_time())
    tkinter.Label(self.top, text="You Won!").grid(column=int(self.map_size/2), row=1)
    
    
    self.sendData(self.username, self.password, self.finish_time)

  def collect_ID(self):
    #Collects username, password, map_size, and finish_time, returns as a tuple.
    return (self.username.get(), self.password.get(), self.map_size, self.finish_time)

  def toggle_flag_mode(self):
    self.flag_mode = not self.flag_mode
    if (self.flag_mode):
      self.flag_button.configure(background="Red")
    else:
      self.flag_button.configure(background="white")
  def update_timer(self):
    time = int(self.mine_map.get_time())
    self.d0 = tkinter.Label(self.top, image=self.num_pictures[time % 10]).grid(row=0, column=self.map_size - 1)
    self.d1 = tkinter.Label(self.top, image=self.num_pictures[int(time / 10) % 10]).grid(row=0, column=self.map_size - 2)
    self.d2 = tkinter.Label(self.top, image=self.num_pictures[int(time / 100) % 10]).grid(row=0, column=self.map_size - 3)
    if (not (self.mine_map.check_win() or self.mine_map.check_lose())):
        self.root.after(1000, self.update_timer)

  def store_login(self, username, password):
    self.username = username
    self.password = password

  def unpack_images(self):
    ## Set up images!
    flag_image = Image.open("./Images/Flag.png")
    flag_image = flag_image.resize((24, 24))
    self.flag_icon = ImageTk.PhotoImage(flag_image)

    bomb_image = Image.open("./Images/Bomb.png")
    bomb_image = bomb_image.resize((24, 24))
    self.bomb_icon = ImageTk.PhotoImage(bomb_image)
    
    blank_image = Image.open("./Images/Blank.png")
    blank_image = blank_image.resize((24, 24))
    self.blank_icon = ImageTk.PhotoImage(blank_image)

    flag_button_image = Image.open("./Images/flagbutton.png")
    flag_button_image = flag_button_image.resize((48, 24))
    self.flag_button_icon = ImageTk.PhotoImage(flag_button_image)

    title_image = Image.open("./Images/title.png")
    title_image = title_image.resize((120, 24))
    self.title_icon = ImageTk.PhotoImage(title_image)

    ## Images for the various numbers:
    self.num_pictures = []
    for ii in range(0,10):
      # unpacks and adds the image for each number to the corresponding place in the list.
      self.num_pictures.append(ImageTk.PhotoImage(Image.open("./Images/Numbers/num" + str(ii) + ".png").resize((24,24))))


  # Now we are getting into the functions that initialize the ui and build the map.

  def build_map(self):
    # build the map
    self.map = []
    for row in range (0,self.map_size):
      self.map.append([])
      for col in range(0,self.map_size):
        self.map[row].append(tkinter.Button(self.frm, image=self.blank_icon))
        self.map[row][col]['command'] = lambda row=row, col=col: self.on_button_press(row, col)
        self.map[row][col].grid(column=col,row=row+3)
        #print(self.map[row][col].configure().keys())

  def build_game(self):
    ## Builds and starts the game.

    self.frm = tkinter.Frame(self.root, border=10)
    self.top = tkinter.Frame(self.root, border=10)
    #self.frm.grid_propagate(False)
    self.top.grid()
    self.frm.grid()
    self.flag_mode = False

    self.unpack_images()
    self.build_map()

    # Setup the rest of the screen    
    tkinter.Label(self.top, image=self.title_icon).grid(column=int(self.map_size/2), row=0)
    #tkinter.Button(self.top, text="Quit", command=self.root.destroy).grid(row=0, column=self.map_size - 1)
    self.flag_button = tkinter.Button(self.top, image=self.flag_button_icon, command=lambda: self.toggle_flag_mode())
    self.flag_button.grid(column=0, row=0)

    # Start the game.
    
    self.root.mainloop()

  def __init__(self, root, map_size, mines_per_tile, mine_map):
    #save some variables
    self.map_size = map_size
    self.mines_per_tile = mines_per_tile
    self.map = []
    self.mine_map = mine_map

    ## initial tkinter setup
    self.root = root
    
  def send_data(self, Username, Password, Time):
      # Sends data to the remote server.
      mydb = mysql.connector.connect(
      host="86.38.202.204",
      user="u351964368_root",
      password="SoftwareEngineering3203",
      database="u351964368_SoftwareEngr"
    )
      cursor = mydb.cursor()


      sql = "INSERT INTO Users (username, password, time) VALUES (%s, %s, %s)"
      val = (Username, Password, Time) #instead of food the variable
      cursor.execute(sql, val)

      mydb.commit()
      mydb.close()
      # Set focus on username field
      #self.entry_user.focus()

      self.root.mainloop()
  