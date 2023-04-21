## Made by Isaac Stein, using python's tkinter module and taking heavily from its documentation
import tkinter
from PIL import ImageTk, Image

class MineUI:
  
  def on_button_press(self, row, col):
    if not self.mine_map.map_generated: #if it is the first click, generate the map
      self.mine_map.generatemap(row, col)

    
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
    #tkinter.Label(self.top, text="Username:").grid(column=1, row=0)
    #tkinter.Label(self.top, text="Password:").grid(column=3, row=0)
    tkinter.Button(self.top, text="Submit", command=self.collect_ID).grid(column=4, row=1)
    ## TODO: FIX FOR DIFFERENT BOARD SIZES!
    ## or just remove?
    
    tkinter.Label(self.top, text="Please enter a username and password to put your name on the leaderboard!").grid(column = int(self.map_size/2), row = 2)
    self.username = tkinter.Entry(self.top)
    self.password = tkinter.Entry(self.top)
    self.username.grid(row=1, column=1)
    self.password.grid(row=1, column=3)
    tkinter.Button(self.frm, text = "submit").grid(column = self.map_size-1, row = 1, command=lambda: self.collectID())
    
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
    self.d0 = tkinter.Label(self.top, image=self.num_pictures[time % 10]).grid(row=0, column=self.map_size - 2)
    self.d1 = tkinter.Label(self.top, image=self.num_pictures[int(time / 10) % 10]).grid(row=0, column=self.map_size - 3)
    self.d2 = tkinter.Label(self.top, image=self.num_pictures[int(time / 100) % 10]).grid(row=0, column=self.map_size - 4)
    self.root.after(1000, self.update_timer)
  def __init__(self, map_size, mines_per_tile, mine_map):
    #save some variables
    self.map_size = map_size
    self.mines_per_tile = mines_per_tile
    self.map = []
    self.mine_map = mine_map

    ## initial tkinter setup
    self.root = tkinter.Tk()
    self.frm = tkinter.Frame(self.root, border=10)
    self.top = tkinter.Frame(self.root, border=10)
    #self.frm.grid_propagate(False)
    self.top.grid()
    self.frm.grid()
    self.flag_mode = False

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

    ## Images for the various numbers:
    self.num_pictures = []
    for ii in range(0,10):
      # unpacks and adds the image for each number to the corresponding place in the list.
      self.num_pictures.append(ImageTk.PhotoImage(Image.open("./Images/Numbers/num" + str(ii) + ".png").resize((24,24))))
  
  # build the map
    self.map = []
    for row in range (0,map_size):
      self.map.append([])
      for col in range(0,map_size):
        self.map[row].append(tkinter.Button(self.frm, image=self.blank_icon))
        self.map[row][col]['command'] = lambda row=row, col=col: self.on_button_press(row, col)
        self.map[row][col].grid(column=col,row=row+3)
        #print(self.map[row][col].configure().keys())
    
    # Setup the rest of the screen    
    tkinter.Label(self.top, text="Minesweeper!").grid(column=int(self.map_size/2), row=0)
    tkinter.Button(self.top, text="Quit", command=self.root.destroy).grid(row=0, column=self.map_size - 1)
    self.flag_button = tkinter.Button(self.top, text="flag mode", command=lambda: self.toggle_flag_mode())
    self.flag_button.grid(column=0, row=0)

    self.update_timer()
    self.root.mainloop()
  