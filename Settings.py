#!/usr/bin/python3

"""
Tic Tac Toe 3D
In aceasta librarie sunt toate setarile si variabilele generale folosite de joc.

Mai multe detalii: http://aninu.xyz/post/tic-tac-toe-3d-python3/
"""

__version__ = '1.2'
__date__    = '01.01.2018'
__author__  = 'Anghelina Alin <dev@aninu.ro>'

# Imports
from Rules import *
import Requests as Rqm
import Sockets as Sok

# Debug Mode
debug_mode = True

# Window Name
window_name = "APP: Tic Tac Toe 3D | "

# Window Icon
window_icon = "./Images/favicon.ico"

# Window fixed size (True | False)
window_fixed = True

# Game size (3,4)
game_size = 3

# Game MAX size
game_size_max = 4

# Game Style (1,2)
game_style = 2

# Afiseaza popup (True | False)
game_popup = True

# Sound Effect Computer Press (True | False)
game_sound = True

# Color button presed
button_x = "#007F46"
button_o = "#0094FF"
button_win = "#FF6A00"
button_clear = "#F0F0F0"
button_size = "#0094FF"
button_style = "#A0A0A0"

# Player Name
player_name = "NoName"

# Computer_name
computer_name = "Gelu"

# Row Player (0 - PC | 1 - Player)
row_player = 1

# Button default text
bt_def_text = "-"

# Tic Tac Toe Index (X/O)
TTT_X = 1
TTT_O = 2

# Status Game (True, False)
game_status = True

# Player / Computer - Jocuri castigate
win_computer = 0
win_player = 0
area_for_play = 0

# General settings for design and game save position                                            #
#################################################################################################
Array_A1_BW_Start = [10, 10, 10, 10]					# Position for start Area 1 (width)     #
Array_A1_BH_Start = [170, 170, 170, 170]				# Position for start Area 1 (height)    #
Array_A2_BW_Start = [200, 10, 250, 10]					# Position for start Area 2 (width)     #
Array_A2_BH_Start = [170, 270, 170, 295]				# Position for start Area 2 (height)    #
Array_A3_BW_Start = [390, 10, 490, 10]					# Position for start Area 3 (width)     #
Array_A3_BH_Start = [170, 370, 170, 420]				# Position for start Area 3 (height)    #
Array_A4_BW_Start = [0, 0, 730, 10]						# Position for start Area 4 (width)     #
Array_A4_BH_Start = [0, 0, 170, 545]					# Position for start Area 4 (height)    #
Array_window_width = [550, 330, 940, 400]				# Window width                          #
Array_window_height = [330, 445, 375, 650]				# Window height                         #
Array_reset_b_width = [460, 240, 850, 315]				# Width for reset button                #
Array_window_name = ["3^S1", "3^S2", "4^S1", "4^S2"]	# Window name for special size / style  #
#################################################################################################
A_Buttons = [											# Array with buttons                    #
	[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
	[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
	[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
	[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
]
Game = [												# List with position and what is here   #
	[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
	[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
	[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
	[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]],
]
AvailableMove = game_size * game_size * game_size		# Mutari disponibile                    #
#################################################################################################
