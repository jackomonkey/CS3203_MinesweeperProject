class Cell:
  def __init__(self, contains_bomb):
    self.bomb = contains_bomb
    self.is_flagged = False
    self.revealed = False
    self.neighbor_count = 0

  def is_bomb(self):
    return self.bomb

  def toggle_flag(self):
    self.is_flagged =  not self.is_flagged

  def appears(self):
    if (self.is_flagged):
      return ("F")
    elif not (self.revealed):
      return ("+")
    else:
      if self.is_bomb():
        return 'B'
      else:
        return self.neighbor_count

  def reveal(self):
    self.revealed = True

  def set_neighbor_count(self, neighbor_count):

    self.neighbor_count = neighbor_count
    