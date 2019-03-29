import sys
if sys.version_info >= (3, 0):      #untuk interface (GUI)
  from tkinter import Tk, Button
  from tkinter.font import Font
else:
  from Tkinter import Tk, Button
  from tkFont import Font
from copy import deepcopy

class Board:
  
  def __init__(self,other=None):    #menginisialisasi komponen dari board
    self.player = 'X'
    self.opponent = 'O'
    self.empty = '.'
    self.size = 3
    self.fields = {}
    for y in range(self.size):
      for x in range(self.size):
        self.fields[x,y] = self.empty
    # copy constructor
    if other:
      self.__dict__ = deepcopy(other.__dict__)      #mengcopy self dan semua isinya ke other._dict_
      
  def move(self,x,y):
    board = Board(self)             #mereturn status terbaru dari setiap state
    board.fields[x,y] = board.player
    (board.player,board.opponent) = (board.opponent,board.player)
    
  def won(self):                    #mengecek kemenangan setiap baris horizontal,vertical,diagonal
    # horizontal
    for y in range(self.size):
      winning = []
      for x in range(self.size):
        if self.fields[x,y] == self.opponent:
          winning.append((x,y))
      if len(winning) == self.size:
        return winning
    # vertikal
    for x in range(self.size):
      winning = []
      for y in range(self.size):
        if self.fields[x,y] == self.opponent:
          winning.append((x,y))
      if len(winning) == self.size:
        return winning
    # diagonal
    winning = []
    for y in range(self.size):
      x = y
      if self.fields[x,y] == self.opponent:
        winning.append((x,y))
    if len(winning) == self.size:
      return winning
    # diagonal lain
    winning = []
    for y in range(self.size):
      x = self.size-1-y
      if self.fields[x,y] == self.opponent:
        winning.append((x,y))
    if len(winning) == self.size:
      return winning
    return None
