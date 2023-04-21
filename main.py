import MineMap
import MineUI
import MineLogin
import tkinter



if __name__ == "__main__":
  map_size = int(input("Map width and height: "))
  #mines_per_tile = float(input("Mines per tile: "))
  mines_per_tile = 0.25

  # Start up the back end
  m = MineMap.MineMap(map_size, mines_per_tile)

  # Set window size and position
  root = tkinter.Tk()
  #window_width = 500
  #window_height = 400
  #screen_width = root.winfo_screenwidth()
  #screen_height = root.winfo_screenheight()
  #x = int((screen_width / 2) - (window_width / 2))
  #y = int((screen_height / 2) - (window_height / 2))
  #root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
  
  # Build the ui object, but don't put any ui in yet.
  ui = MineUI.MineUI(root, map_size, mines_per_tile, m)

  # Build the login object, feed it the ui so it can build it when needed.
  login = MineLogin.MineLogin(root, ui)