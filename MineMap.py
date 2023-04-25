import random
import MineCell
from timeit import default_timer

class MineMap:

  def __init__(self, map_size, mines_per_tile):
    self.map_size = map_size
    self.tiles_left = map_size * map_size
    self.total_mines = int(map_size * map_size / mines_per_tile)
    self.mines_per_tile = mines_per_tile
    self.lose = False
    self.map_generated = False
    self.start_time = 0


  def get_time(self):
    if(self.map_generated):
      return default_timer() - self.start_time
    else:
      return 0
    
  def generatemap(self, row, column):
    ## TODO: FIND A WAY TO DO THIS AFTER WE PICK OUR FIRST TILE, SO WE GET A STARTING AREA
    self.map_generated = True
    self.map = []
    mines_placed = 0
    for r in range (0, self.map_size):
      self.map.append([])
      for c in range(0, self.map_size):
        if (((abs(r-row) > 2) or (abs(c-column) > 2)) and (random.randrange(0,10, 1) / 10.0 < self.mines_per_tile)): #don't put bombs where they first click. Otherwise, randomly disperse.
          self.map[r].append(MineCell.Cell(True))
          mines_placed += 1
          self.tiles_left -= 1
        else:
          self.map[r].append(MineCell.Cell(False))

    self.start_time = default_timer() # Timer starts when you first click.

  def check_cell_neighbors(self, row, col):
    neighbor_bombs = 0

    #check the ones up top, trying not to hit errors
    if ((row - 1) >= 0):
      if ((col - 1) >= 0):
        if (self.map[row-1][col-1].is_bomb()):
          neighbor_bombs += 1

      if (self.map[row-1][col].is_bomb()):
          neighbor_bombs += 1
        
      if ((col + 1) < self.map_size):
        if (self.map[row-1][col+1].is_bomb()):
          neighbor_bombs += 1

    #Check the middle ones, still dodging errors. Skip self.
    if ((col - 1) >= 0):
        if (self.map[row][col-1].is_bomb()):
          neighbor_bombs += 1
        
    if ((col + 1) < self.map_size):
      if (self.map[row][col+1].is_bomb()):
        neighbor_bombs += 1

    #Check bottom ones, again avoiding boundaries. 
    if ((row + 1) < self.map_size):
      if ((col - 1) >= 0):
        if (self.map[row+1][col-1].is_bomb()):
          neighbor_bombs += 1

      if (self.map[row+1][col].is_bomb()):
          neighbor_bombs += 1
        
      if ((col + 1) < self.map_size):
        if (self.map[row+1][col+1].is_bomb()):
          neighbor_bombs += 1

    return neighbor_bombs
          
  def reveal_cell(self, row, col):
    if (self.map[row][col].revealed):
      return
    self.map[row][col].reveal()
    if (self.map[row][col].is_bomb()):
      self.lose = True
      #print("BOMB!")
      ## TODO: FIGURE OUT WHERE THE LOSE FUNCTION GOES, AND LINK TO IT HERE
    else:
      self.tiles_left -= 1
      #print(self.tiles_left)
      self.map[row][ col].set_neighbor_count(self.check_cell_neighbors(row, col)
      )
        ## TODO: FIGUREOUT WHERE THE WIN FUNCTION GOES, AND LINK TO IT HERE 

      return self.map[row][col].neighbor_count
        
  def return_cell_status(self, row, col, debug=False):
    return self.map[row][col].appears()

  def check_lose(self):
    return self.lose

  def check_win(self):
    if (not self.lose) and self.tiles_left == 0:
      return True
    else:
      return False

  def toggle_flag(self, row, col):
    self.map[row][col].toggle_flag()
    

  def print_map(self, debug=False):
    for row in range (0, self.map_size):
      print("\n")
      for col in range(0, self.map_size):
        if (debug):
          print(self.map[row][col].is_bomb(), end=" ")
        else:
          print(self.map[row][col].appears(), end=" ")

    print("\n")
      
  
  def prompt_user(self):
    self.print_map()
    print("What cell would you like to check?")
    self.reveal_cell(int(input("y: ")), int(input("x: ")))




if __name__ == "__main__":
  print("Hi!")