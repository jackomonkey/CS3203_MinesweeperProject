import MineMap
import MineUI



if __name__ == "__main__":
  map_size = int(input("Map width and height: "))
  #mines_per_tile = float(input("Mines per tile: "))
  mines_per_tile = 0.3
  m = MineMap.MineMap(map_size, mines_per_tile)
  #while True:
   # m.prompt_user()
  ui = MineUI.MineUI(map_size, mines_per_tile, m)
