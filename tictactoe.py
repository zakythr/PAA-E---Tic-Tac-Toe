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
