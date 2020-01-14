#!/usr/bin/python3

"""
Tic Tac Toe 3D
In aceasta librarie sunt imbinate toate librariile si este afisat jocul pentru a putea fi jucat.

Mai multe detalii: http://aninu.xyz/post/tic-tac-toe-3d-python3/
"""

__version__ = '1.2'
__date__    = '01.01.2018'
__author__  = 'Anghelina Alin <dev@aninu.ro>'

from Interface import *

Window = Tk()
Interface(Window)
Window.mainloop()

print ("Success close game")