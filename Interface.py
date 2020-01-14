#!/usr/bin/python3

"""
Tic Tac Toe 3D
In aceasta librarie este construit intreg jocul.

Mai multe detalii: http://aninu.xyz/post/tic-tac-toe-3d-python3/
"""

__version__ = '1.2'
__date__    = '01.01.2018'
__author__  = 'Anghelina Alin <dev@aninu.ro>'

import time
from Settings import *
from tkinter import *
from SoundEffect import *
import tkinter.messagebox

class Interface:
	"""
	Construieste jocul X si O
	"""
	def __init__(self, window):
		"""
		Initializeaza setarile pentru joc
		""" 
		self.window = window
		
		# Get Index Game size / game style
		IndexSS = self.GetIDStyle()
		
		# Set Window Size
		window.geometry(str(Array_window_width[IndexSS])+"x"+str(Array_window_height[IndexSS]))
		if (window_fixed):
			window.minsize(width=Array_window_width[IndexSS], height=Array_window_height[IndexSS])
			window.maxsize(width=Array_window_width[IndexSS], height=Array_window_height[IndexSS])
		
		# Set Window Title
		window.title(window_name + Array_window_name[IndexSS])
		
		# Set Window Icon
		window.iconbitmap(window_icon)
		
		# Add labels for area
		self.Add_Labels(window)
		
		# Add buttons for area
		self.AddButtons(window)
		
		# Add button, label and input for player
		self.SetPlayerName(window)
		
		# Add other element
		self.AddOtherDesign(window)
	
	def ButtonPress(self, sArea, i, j):
		"""
		Functia care se apeleaza cand se apasa butoanele pentru joc
		"""
		global row_player, AvailableMove, Game, game_status
		if (debug_mode): print("[DebugMode]: Press Button :> {" + str(sArea) + "}  i{" + str(i) + "} j{" + str(j)+"}")
		
		if (game_status):
			if (AvailableMove > 0):
				if (self.CheckIsFreePosition(sArea, i, j)):
					AvailableMove -= 1
					index = self.GetIndexFromArea(sArea)
					if (row_player == 1):
						sButton = "X"
						sBG = button_x
						row_player = 0
						# Save X Press to GAME
						Game[index][i][j] = TTT_X
					else:
						sButton = "O"
						sBG = button_o
						row_player = 1
						# Save O Press to GAME
						Game[index][i][j] = TTT_O
					
					# Update Color and Text on Button {}
					A_Buttons[index][i][j].config(text = sButton, bg = sBG)
					
					# Check win game 
					self.CheckWinGame(sButton)
					
					# Computer Press Button
					if (row_player == 0): 
						# Play sound effect after press button
						if (game_sound): PlaySound()
						# Call function
						self.ComputerPress(sArea)
					
					# Check if are move availables
					if (AvailableMove == 0):
						if (debug_mode): print ("[DebugMode]: {Auto} Jocul s-a incheiat. Nu mai sunt mutari disponibile.")
						if(game_popup): tkinter.messagebox.showinfo(window_name, "Salut " +str(player_name)+ ", \nNu mai sunt mutari disponibile.")
						Rqm.Send_POST(player_name, 0, 0, game_size)
						Sok.message_to_server("Jocul dintre calculator si "+str(player_name)+" s-a terminat remiza.")
				else:
					if (debug_mode): print ("[DebugMode]: Pozitia selectata este deja ocupata.")
					if(game_popup): tkinter.messagebox.showinfo(window_name, "Salut " +str(player_name)+ ", \nPozitia selectata este deja ocupata. Trebuie sa alegi alta pozitie.")
			else:
				if (debug_mode): print ("[DebugMode]: Jocul s-a incheiat. Nu mai sunt mutari disponibile.")
				if(game_popup): tkinter.messagebox.showinfo(window_name, "Salut " +str(player_name)+ ", \nJocul s-a incheiat. Nu mai sunt mutari disponibile.")
				Rqm.Send_POST(player_name, 0, 0, game_size)
				Sok.message_to_server("Jocul dintre calculator si "+str(player_name)+" s-a terminat remiza.")
		else:
			if (debug_mode): print ("[DebugMode]: Jocul s-a incheiat. Avem un castigator. Poti incepe un joc nou.")
			if(game_popup): tkinter.messagebox.showinfo(window_name, "Salut " +str(player_name)+ ", \nJocul s-a incheiat. Avem un castigator. Poti incepe un joc nou.")
		return 0
	
	def Add_Labels(self, window):
		"""
		Adauga label cu denumirea fiecarei zone
		"""
		global A1_Name, A2_Name, A3_Name, A4_Name
		Index = self.GetIDStyle()
		# Add Label for Area 1
		A1_Name = Label(window, text = "Area 1")
		A1_Name.place(x = Array_A1_BW_Start[Index], y = Array_A1_BH_Start[Index] - 25)
		
		# Add Label for Area 2
		A2_Name = Label(window, text = "Area 2")
		A2_Name.place(x = Array_A2_BW_Start[Index], y = Array_A2_BH_Start[Index] - 25)
		
		# Add Label for Area 3
		A3_Name = Label(window, text = "Area 3")
		A3_Name.place(x = Array_A3_BW_Start[Index], y = Array_A3_BH_Start[Index] - 25)
		
		# Add Label for Area 4
		A4_Name = Label(window, text = "Area 4")
		if (game_size == 4):
			A4_Name.place(x = Array_A4_BW_Start[Index], y = Array_A4_BH_Start[Index] - 25)
		else:
			A4_Name.place(x = -500, y = -500)
		return 0
	
	def Create_Button(self, window, sArea, i, j):
		"""
		Adauga fiecare buton la coordonata corespunzatoare pentru GAME_SIZE
		si GAME_STYLE setat in 'Settings.py' si construirea matricei de butoane
		"""
		Index = self.GetIDStyle()
		if (sArea == "A1"):
			if (game_style == 1):
				A_Buttons[0][i][j] = Button(window, text = bt_def_text, bg = button_clear, width = 5, height = 2, command = lambda: self.ButtonPress(sArea, i, j))
				if ((game_size == 3 and i < 3 and j < 3) or (game_size == 4)):
					A_Buttons[0][i][j].place(x = Array_A1_BW_Start[Index] + (i*50), y = Array_A1_BH_Start[Index] + (j*50))
			else:
				A_Buttons[0][i][j] = Button(window, text = bt_def_text, bg = button_clear, width = 10, height = 1, command = lambda: self.ButtonPress(sArea, i, j))
				if ((game_size == 3 and i < 3 and j < 3) or (game_size == 4)):
					A_Buttons[0][i][j].place(x = Array_A1_BW_Start[Index] + 50 - (j * 15) + (i*82), y = Array_A1_BH_Start[Index] - 25 + (j*30))
		elif (sArea == "A2"):
			if (game_style == 1):
				A_Buttons[1][i][j] = Button(window, text = bt_def_text, bg = button_clear, width = 5, height = 2, command = lambda: self.ButtonPress(sArea, i, j))
				if ((game_size == 3 and i < 3 and j < 3) or (game_size == 4)):
					A_Buttons[1][i][j].place(x = Array_A2_BW_Start[Index] + (i*50), y = Array_A2_BH_Start[Index] + (j*50))
			else:
				A_Buttons[1][i][j] = Button(window, text = bt_def_text, bg = button_clear, width = 10, height = 1, command = lambda: self.ButtonPress(sArea, i, j))
				if ((game_size == 3 and i < 3 and j < 3) or (game_size == 4)):
					A_Buttons[1][i][j].place(x = Array_A2_BW_Start[Index] + 50 - (j * 15) + (i*82), y = Array_A2_BH_Start[Index] - 25 + (j*30))
		elif (sArea == "A3"):
			if (game_style == 1):
				A_Buttons[2][i][j] = Button(window, text = bt_def_text, bg = button_clear, width = 5, height = 2, command = lambda: self.ButtonPress(sArea, i, j))
				if ((game_size == 3 and i < 3 and j < 3) or (game_size == 4)):
					A_Buttons[2][i][j].place(x = Array_A3_BW_Start[Index] + (i*50), y = Array_A3_BH_Start[Index] + (j*50))
			else:
				A_Buttons[2][i][j] = Button(window, text = bt_def_text, bg = button_clear, width = 10, height = 1, command = lambda: self.ButtonPress(sArea, i, j))
				if ((game_size == 3 and i < 3 and j < 3) or (game_size == 4)):
					A_Buttons[2][i][j].place(x = Array_A3_BW_Start[Index] + 50 - (j * 15) + (i*82), y = Array_A3_BH_Start[Index] - 25 + (j*30))
		else:
			if (game_style == 1):
				A_Buttons[3][i][j] = Button(window, text = bt_def_text, bg = button_clear, width = 5, height = 2, command = lambda: self.ButtonPress(sArea, i, j))
				if (game_size == 4):
					A_Buttons[3][i][j].place(x = Array_A4_BW_Start[Index] + (i*50), y = Array_A4_BH_Start[Index] + (j*50))
			else:
				A_Buttons[3][i][j] = Button(window, text = bt_def_text, bg = button_clear, width = 10, height = 1, command = lambda: self.ButtonPress(sArea, i, j))
				if (game_size == 4):
					A_Buttons[3][i][j].place(x = Array_A4_BW_Start[Index] + 50 - (j * 15) + (i*82), y = Array_A4_BH_Start[Index] - 25 + (j*30))
		return 0
	
	def AddButtons(self, window):
		"""
		Adauga butoanele pentru a juca X si O
		"""
		# Add buttons to area 1
		for i in range(0, game_size_max):
			for j in range(0, game_size_max):
				self.Create_Button(window, "A1", i, j)
				self.Create_Button(window, "A2", i, j)
				self.Create_Button(window, "A3", i, j)
				self.Create_Button(window, "A4", i, j)
		return 0
	
	def SetPlayerName(self, window):
		"""
		Adauga elementele corespunzatoare pentru salvarea numelui de jucator
		"""
		# Add label for player name
		P_Name = Label(window, text = "Numele jucatorului este:").place(x = 10, y = 5)
		# Add input for player name
		P_In = Entry(window, width=22)
		P_In.insert(END, player_name)
		P_In.place(x = 10, y = 30)
		# Add button for save player name
		P_Save = Button(window, text = "Salveaza", width = 10, height = 2, command = lambda: self.SavePlayerName(P_In))
		P_Save.place(x = 150, y = 8)
		return 0
	
	def SavePlayerName(self, P_in):
		"""
		(Button) Salveaza numele jucatorului
		"""
		global player_name
		old_name = player_name
		player_name = P_in.get()
		if (debug_mode): print ("[DebugMode]: Numele jucatorului este: " +str(player_name))
		Sok.message_to_server("Jucatorul a schimbat numele din {" +str(old_name)+ "} in {" +str(player_name)+ "}.")
		return 0
	
	def AddOtherDesign(self, window):
		"""
		Adauga butoanele pentru REST, JOC NOU, GAME SIZE, GAME STYLE
		Adauga label pentru SCOR si LINII
		"""
		global S_Jucator, S_Calculator, P_Reset, P_GNew
		global P_Game3, P_Game4, P_Style1, P_Style2
		# Index for Style and Game size
		Index = self.GetIDStyle()
		# Bar Len
		b_text = "_"
		for i in range(0, 250): b_text += "_"
		# Add Label
		B_Lab = Label(window, text = b_text).place(x = -5, y = 50)		
		# Add button for reset
		P_Reset = Button(window, text = "Reseteaza", width = 10, height = 1, command = lambda: self.GameReset())
		P_Reset.place(x = Array_reset_b_width[Index], y = 8)
		# Add button New Game
		P_GNew = Button(window, text = "Joc Nou", width = 10, height = 1, command = lambda: self.NewGame())
		P_GNew.place(x = Array_reset_b_width[Index], y = 35)
		# Scor text
		B_Scor = Label(window, text = "Scor:").place(x = 10, y = 70)
		# Scor Bar
		B_Sc = Label(window, text = b_text).place(x = -5, y = 85)
		# Scor Jucator
		S_Jucator = Label(window, text = "Jucator: {0}", fg = button_x)
		S_Jucator.place(x = 50, y = 70)
		# Scor Calculator
		S_Calculator = Label(window, text = "Calculator: {0}", fg = button_o)
		S_Calculator.place(x = 125, y = 70)
		# Add button for change game size and game style
		B_GSS = Label(window, text = b_text).place(x = -5, y = 120)
		
		# Button for 3x3x3
		if (game_size == 3): P_Game3_BG = button_win
		else: P_Game3_BG = button_size
		P_Game3 = Button(window, text = "Size: 3x3x3", width = 10, height = 1, bg = P_Game3_BG, fg = "white", command = lambda: self.ChangeGameSize3())
		P_Game3.place(x = 10, y = 105)

		# Button for 3x3x3
		if (game_size == 4): P_Game4_BG = button_win
		else: P_Game4_BG = button_size
		P_Game4 = Button(window, text = "Size: 4x4x4", width = 10, height = 1, bg = P_Game4_BG, fg = "white", command = lambda: self.ChangeGameSize4())
		P_Game4.place(x = 90, y = 105)

		# Button for Style 1
		if (game_style == 1): P_Style1_BG = button_win
		else: P_Style1_BG = button_style
		P_Style1 = Button(window, text = "Style: 1", width = 8, height = 1, bg = P_Style1_BG, fg = "white", command = lambda: self.ChangeGameStyle1())
		P_Style1.place(x = 175, y = 105)

		# Button for Style 2
		if (game_style == 2): P_Style2_BG = button_win
		else: P_Style2_BG = button_style
		P_Style2 = Button(window, text = "Style: 2", width = 8, height = 1, bg = P_Style2_BG, fg = "white", command = lambda: self.ChangeGameStyle2())
		P_Style2.place(x = 241, y = 105)

		return 0
	
	def ChangeGameSize3(self):
		"""
		Schimba GAME_SIZE = 3 si incepe un joc nou
		"""	 
		global game_size, game_style, P_Game3, P_Game4, P_Style1, P_Style2
		if (game_size != 3):
			# Button update color
			P_Game3.config(bg = button_win)
			P_Game4.config(bg = button_size)
			# Change game size and update
			game_size = 3
			self.UpdateWindowInterface()
			if (debug_mode): print("[DebugMode]: Design-ul jocului a fost schimbat la {Size #3x3x3}")
		return 0
	
	def ChangeGameSize4(self):
		"""	
		Schimba GAME_SIZE = 4 si incepe un joc nou
		"""	 
		global game_size, game_style, P_Game3, P_Game4, P_Style1, P_Style2
		if (game_size != 4):
			# Button update color
			P_Game3.config(bg = button_size)
			P_Game4.config(bg = button_win)
			# Change game size and update
			game_size = 4
			self.UpdateWindowInterface()
			if (debug_mode): print("[DebugMode]: Design-ul jocului a fost schimbat la {Size #4x4x4}")
		return 0
	
	def ChangeGameStyle1(self):
		"""
		Schimba GAME_STYLE = 1 si incepe un joc nou
		"""	 
		global game_size, game_style, P_Game3, P_Game4, P_Style1, P_Style2
		if (game_style != 1):
			# Button update color
			P_Style1.config(bg = button_win)
			P_Style2.config(bg = button_style)
			# Change game size and update
			game_style = 1
			self.UpdateWindowInterface()
			if (debug_mode): print("[DebugMode]: Design-ul jocului a fost schimbat la {Style #1}")
		return 0
	
	def ChangeGameStyle2(self):
		"""
		Schimba GAME_STYLE = 2 si incepe un joc nou
		"""	 
		global game_size, game_style, P_Game3, P_Game4, P_Style1, P_Style2
		if (game_style != 2):
			# Button update color
			P_Style1.config(bg = button_style)
			P_Style2.config(bg = button_win)
			# Change game size and update
			game_style = 2
			self.UpdateWindowInterface()
			if (debug_mode): print("[DebugMode]: Design-ul jocului a fost schimbat la {Style #2}")
		return 0
	
	def GetIDStyle(self):
		"""	
		Pentru GAME_SIZE si GAME_STYLE exista un index special pentru fiecare valoare data
		"""	 
		global game_size, game_style
		if (game_size == 3 and game_style == 1): 
			return 0
		elif (game_size == 3 and game_style == 2): 
			return 1
		elif (game_size == 4 and game_style == 1): 
			return 2
		else: 
			return 3
	
	def UpdateWindowInterface(self):
		"""
		Actualizeaza elementele din fereastra in functie de modul de joc
		"""	 
		global P_Reset, P_GNew, A_Buttons, game_size_max
		Index = self.GetIDStyle()
		# Set new title
		self.window.title(window_name + Array_window_name[Index])
		# Set new size
		self.window.geometry(str(Array_window_width[Index])+"x"+str(Array_window_height[Index]))
		if (window_fixed):
			self.window.minsize(width=Array_window_width[Index], height=Array_window_height[Index])
			self.window.maxsize(width=Array_window_width[Index], height=Array_window_height[Index])
		# Set new position for button
		P_Reset.place(x = Array_reset_b_width[Index], y = 8)
		P_GNew.place(x = Array_reset_b_width[Index], y = 35)
		# Set new position for button press game
		for i in range(0, game_size_max):
			for j in range(0, game_size_max):
				# Area 1
				if (game_style == 1):
					A_Buttons[0][i][j].config(width = 5, height = 2)
					A_Buttons[0][i][j].place(x = Array_A1_BW_Start[Index] + (i*50), y = Array_A1_BH_Start[Index] + (j*50))
				else:
					A_Buttons[0][i][j].config(width = 10, height = 1)
					A_Buttons[0][i][j].place(x = Array_A1_BW_Start[Index] + 50 - (j * 15) + (i*82), y = Array_A1_BH_Start[Index] - 25 + (j*30))
				# Area 2
				if (game_style == 1):
					A_Buttons[1][i][j].config(width = 5, height = 2)
					A_Buttons[1][i][j].place(x = Array_A2_BW_Start[Index] + (i*50), y = Array_A2_BH_Start[Index] + (j*50))
				else:
					A_Buttons[1][i][j].config(width = 10, height = 1)
					A_Buttons[1][i][j].place(x = Array_A2_BW_Start[Index] + 50 - (j * 15) + (i*82), y = Array_A2_BH_Start[Index] - 25 + (j*30))
				# Area 3
				if (game_style == 1):
					A_Buttons[2][i][j].config(width = 5, height = 2)
					A_Buttons[2][i][j].place(x = Array_A3_BW_Start[Index] + (i*50), y = Array_A3_BH_Start[Index] + (j*50))
				else:
					A_Buttons[2][i][j].config(width = 10, height = 1)
					A_Buttons[2][i][j].place(x = Array_A3_BW_Start[Index] + 50 - (j * 15) + (i*82), y = Array_A3_BH_Start[Index] - 25 + (j*30))
				# Area 4
				if (game_size == 4):
					if (game_style == 1):
						A_Buttons[3][i][j].config(width = 5, height = 2)
						A_Buttons[3][i][j].place(x = Array_A4_BW_Start[Index] + (i*50), y = Array_A4_BH_Start[Index] + (j*50))
					else:
						A_Buttons[3][i][j].config(width = 10, height = 1)
						A_Buttons[3][i][j].place(x = Array_A4_BW_Start[Index] + 50 - (j * 15) + (i*82), y = Array_A4_BH_Start[Index] - 25 + (j*30))
				# Remove plus button
				if (game_size == 3):
					if (i == 3 or j == 3):
						for z in range(0, game_size_max):
							A_Buttons[z][i][j].place(x = -500, y = -500)
		# Set new position for label
		A1_Name.place(x = Array_A1_BW_Start[Index], y = Array_A1_BH_Start[Index] - 25)
		A2_Name.place(x = Array_A2_BW_Start[Index], y = Array_A2_BH_Start[Index] - 25)
		A3_Name.place(x = Array_A3_BW_Start[Index], y = Array_A3_BH_Start[Index] - 25)
		A4_Name.place(x = Array_A4_BW_Start[Index], y = Array_A4_BH_Start[Index] - 25)
		# Reset Game
		self.NewGame()
		return 0

	def GameReset(self):
		"""
		Reseteaza complet jocul
		"""	 
		global row_player, AvailableMove, game_status, win_computer, win_player, area_for_play
		if (debug_mode): print ("[DebugMode]: Reset Game")
		S_Jucator.config(text = "Jucator: {0}")
		S_Calculator.config(text = "Calculator: {0}")
		self.ClearButtonsColorText()
		row_player = 1
		area_for_play = 0
		game_status = True
		win_computer = 0
		win_player = 0
		AvailableMove = game_size * game_size * game_size
		if (debug_mode): print ("[DebugMode]: Finish Reset Game \n")
		return 0
	
	def NewGame(self):
		"""
		Reseteaza jocul, lasand scorul intact
		"""	 
		global row_player, AvailableMove, game_status, win_computer, win_player, area_for_play
		if (debug_mode): print ("[DebugMode]: Start New Game")
		self.ClearButtonsColorText()
		row_player = 1
		area_for_play = 0
		game_status = True
		AvailableMove = game_size * game_size * game_size
		if (debug_mode): print ("[DebugMode]: Finish Start New Game \n")
		return 0
	
	def ClearButtonsColorText(self):
		"""
		Aceasta functie va actualiza textul si culorile butoanelor folosite pentru jocul de X si O
		"""	 
		global Game, A_Buttons
		if (debug_mode): print ("[DebugMode]: Clear Buttons Color and text")
		for z in range(0, game_size):
			for i in range(0, game_size):
				for j in range(0, game_size):
					A_Buttons[z][i][j].config(text = bt_def_text, bg = button_clear)
					Game[z][i][j] = 0
		if (debug_mode): print ("[DebugMode]: Finish Clear Buttons Color and text")
		return 0
		
	def GetIndexFromArea(self, sArea):
		"""
		Fiecare zona are un idex (A1: 0, A2: 1, A3: 2, A4: 3)
		Aceasta functie primeste ca parametru numere zonei si returneaza index-ul acesteia
		"""	 
		if (sArea == "A1"): return 0
		elif (sArea == "A2"): return 1 
		elif (sArea == "A3"): return 2
		else: return 3
	
	def CheckIsFreePosition(self, sArea, i, j):
		"""
		Verifica o anumita pozitie daca este libera
		"""	 
		# Check if your position is free
		index = self.GetIndexFromArea(sArea)
		if (Game[index][i][j] != 0): return 0
		else: return 1
	
	def CheckWinGame(self, sType = "X"):
		"""
		Verifica daca jucatorul sau calculatorul a castigat jocul
		"""
		global Rules_3, Rules_4, game_size, game_status, Rules_3x3x3, Rules_4x4x4, win_player, win_player, win_computer, S_Jucator, S_Calculator
		iTimeStart = time.time()
		if (debug_mode): print ("[DebugMode]: Start Check if exist winner. ")
		# Game size: 3x3x3
		if (game_size == 3):
			for r in range(0, Rules_3):
				# Get all type of index {intex}
				Index_1 = self.GetIndexFromArea(Rules_3x3x3[r][0][0])
				Index_2 = self.GetIndexFromArea(Rules_3x3x3[r][1][0])
				Index_3 = self.GetIndexFromArea(Rules_3x3x3[r][2][0])
				# Get all position for {i}
				Pos1_i = int(Rules_3x3x3[r][0][1])
				Pos2_i = int(Rules_3x3x3[r][1][1])
				Pos3_i = int(Rules_3x3x3[r][2][1])
				# Get all position for {j}
				Pos1_j = int(Rules_3x3x3[r][0][2])
				Pos2_j = int(Rules_3x3x3[r][1][2])
				Pos3_j = int(Rules_3x3x3[r][2][2])
				# Show information about current game status
				#if (debug_mode): print ("[DebugMode]:", Rules_3x3x3[r], Game[Index_1][Pos1_i][Pos1_j], Game[Index_2][Pos2_i][Pos2_j], Game[Index_3][Pos3_i][Pos3_j])
				# Check if X win GAME
				if (sType == "X"):
					if (Game[Index_1][Pos1_i][Pos1_j] == TTT_X and Game[Index_2][Pos2_i][Pos2_j] == TTT_X and Game[Index_3][Pos3_i][Pos3_j] == TTT_X):
						if (debug_mode): print ("[DebugMode]: " +player_name+ " a castigat {X}.")
						# Play Sound for Win Game
						if (game_sound): PlaySoundWin()
						# Update Button color with win color
						A_Buttons[Index_1][Pos1_i][Pos1_j].config(bg = button_win)
						A_Buttons[Index_2][Pos2_i][Pos2_j].config(bg = button_win)
						A_Buttons[Index_3][Pos3_i][Pos3_j].config(bg = button_win)
						win_player += 1
						S_Jucator.config(text = "Jucator: {" +str(win_player)+ "}")
						Rqm.Send_POST(player_name, 1, 0, game_size)
						Sok.message_to_server("Acest joc a fost castigat de " +str(player_name)+ ".")
						game_status = False
						break
				# Check if O win GAME
				if (sType == "O"):
					if (Game[Index_1][Pos1_i][Pos1_j] == TTT_O and Game[Index_2][Pos2_i][Pos2_j] == TTT_O and Game[Index_3][Pos3_i][Pos3_j] == TTT_O):
						if (debug_mode): print ("[DebugMode]: Calculatorul a castigat {O}.")
						# Play Sound for Win Game
						if (game_sound): PlaySoundWin()
						# Update Button color with win color
						A_Buttons[Index_1][Pos1_i][Pos1_j].config(bg = button_win)
						A_Buttons[Index_2][Pos2_i][Pos2_j].config(bg = button_win)
						A_Buttons[Index_3][Pos3_i][Pos3_j].config(bg = button_win)
						win_computer += 1
						S_Calculator.config(text = "Calculator: {" +str(win_computer)+ "}")
						Rqm.Send_POST(player_name, 0, 1, game_size)
						Sok.message_to_server("Acest joc a fost castigat de calculator.")
						game_status = False
						break
		# Game size: 4x4x4
		else:
			for r in range(0, Rules_4):
				# Get all type of index {intex}
				Index_1 = self.GetIndexFromArea(Rules_4x4x4[r][0][0])
				Index_2 = self.GetIndexFromArea(Rules_4x4x4[r][1][0])
				Index_3 = self.GetIndexFromArea(Rules_4x4x4[r][2][0])
				Index_4 = self.GetIndexFromArea(Rules_4x4x4[r][3][0])
				# Get all position for {i}
				Pos1_i = int(Rules_4x4x4[r][0][1])
				Pos2_i = int(Rules_4x4x4[r][1][1])
				Pos3_i = int(Rules_4x4x4[r][2][1])
				Pos4_i = int(Rules_4x4x4[r][3][1])
				# Get all position for {j}
				Pos1_j = int(Rules_4x4x4[r][0][2])
				Pos2_j = int(Rules_4x4x4[r][1][2])
				Pos3_j = int(Rules_4x4x4[r][2][2])
				Pos4_j = int(Rules_4x4x4[r][3][2])
				# Show information about current game status
				#if (debug_mode): print ("[DebugMode]:", Rules_4x4x4[r], Game[Index_1][Pos1_i][Pos1_j], Game[Index_2][Pos2_i][Pos2_j], Game[Index_3][Pos3_i][Pos3_j])
				# Check if X win GAME
				if (sType == "X"):
					if (Game[Index_1][Pos1_i][Pos1_j] == TTT_X and Game[Index_2][Pos2_i][Pos2_j] == TTT_X and Game[Index_3][Pos3_i][Pos3_j] == TTT_X and Game[Index_4][Pos4_i][Pos4_j] == TTT_X):
						if (debug_mode): print ("[DebugMode]: " +player_name+ " a castigat {X}.")
						# Play Sound for Win Game
						if (game_sound): PlaySoundWin()
						# Update Button color with win color
						A_Buttons[Index_1][Pos1_i][Pos1_j].config(bg = button_win)
						A_Buttons[Index_2][Pos2_i][Pos2_j].config(bg = button_win)
						A_Buttons[Index_3][Pos3_i][Pos3_j].config(bg = button_win)
						A_Buttons[Index_4][Pos4_i][Pos4_j].config(bg = button_win)
						win_player += 1
						S_Jucator.config(text = "Jucator: {" +str(win_player)+ "}")
						Rqm.Send_POST(player_name, 1, 0, game_size)
						Sok.message_to_server("Acest joc a fost castigat de " +str(player_name)+ ".")
						game_status = False
						break
				# Check if O win GAME
				if (sType == "O"):
					if (Game[Index_1][Pos1_i][Pos1_j] == TTT_O and Game[Index_2][Pos2_i][Pos2_j] == TTT_O and Game[Index_3][Pos3_i][Pos3_j] == TTT_O and Game[Index_4][Pos4_i][Pos4_j] == TTT_O):
						if (debug_mode): print ("[DebugMode]: Calculatorul a castigat {O}.")
						# Play Sound for Win Game
						if (game_sound): PlaySoundWin()
						# Update Button color with win color
						A_Buttons[Index_1][Pos1_i][Pos1_j].config(bg = button_win)
						A_Buttons[Index_2][Pos2_i][Pos2_j].config(bg = button_win)
						A_Buttons[Index_3][Pos3_i][Pos3_j].config(bg = button_win)
						A_Buttons[Index_4][Pos4_i][Pos4_j].config(bg = button_win)
						win_computer += 1
						S_Calculator.config(text = "Calculator: {" +str(win_computer)+ "}")
						Rqm.Send_POST(player_name, 0, 1, game_size)
						Sok.message_to_server("Acest joc a fost castigat de calculator.")
						game_status = False
						break
		# Daca scorul celor doi este identic, vor avea aceeasi culoare
		if (game_status == False):
			if (win_player == win_computer):
				S_Jucator.config(fg = button_win)
				S_Calculator.config(fg = button_win)
			else:
				S_Jucator.config(fg = button_x)
				S_Calculator.config(fg = button_o)				
		if (debug_mode): print ("[DebugMode]: End find winner. {Time: ", (time.time() - iTimeStart), "s} \n")
		return 0
	
	def PlayerFirstPress(self, sArea):
		"""
		Cauta cu ce ID incep regulile pentru Zona in care a apasat jucatorul
		Este apelata doar pentru primele doua mutari
		"""
		global area_for_play
		total_move = game_size * game_size * game_size
		if (total_move - 1 <= AvailableMove):
			iStart = 0
			if (game_size == 3):
				for r in range(iStart, Rules_3):
					if (Rules_3x3x3[r][0][0] == sArea):
						iStart = r
						break
			else:
				for r in range(iStart, Rules_4):
					if (Rules_4x4x4[r][0][0] == sArea):
						iStart = r
						break
			area_for_play = iStart
			return iStart
		elif (total_move - 3 <= AvailableMove):
			return area_for_play
		elif (total_move - 5 <= AvailableMove and game_size == 4):
			return area_for_play
		else:
			return 0
	
	def FinishSolutionPress(self):
		"""
		Se foloseste atunci cand nu mai sunt variante de castig, iar jocul se va termina egal
		"""
		if (debug_mode): print("[DebugMode]: Find free position.")
		Index  = 0
		Pos_i = 0
		Pos_j = 0
		Gasit = False
		for z in range(0, game_size):
			for i in range(0, game_size):
				for j in range(0, game_size):
					if (Gasit == False):
						if (Game[z][i][j] == 0):
							Index = z
							Pos_i = i
							Pos_j = j
							Gasit = True
							break
		if (Gasit):
			sArea = "A" +str(Index+1)
			self.ButtonPress(sArea, Pos_i, Pos_j)
		return 0
	
	def ComputerPress(self, sArea):
		"""
		Calculatorul trebuie sa apase un buton cat mai bine posibil
		1) Se verifica daca prin apasarea unui buton calculatorul castiga
		2) Se verifica daca poate bloca miscarile jucatorului
		3) Cauta cea mai buna varianta pentru a apasa folosinduse de reguli
		"""
		global Rules_3, game_status, Rules_3x3x3, Rules_4, Rules_4x4x4
		iTimeStart = time.time()
		if (debug_mode): print ("[DebugMode]: Start Computer Press Button. ")
		presed_button = False
		# Game size: 3x3x3
		if (game_size == 3):
			for c in range(0,3):
				if (presed_button == False): 
					# Verifica in care plan va pune Jucatorul prima casuta.
					iStart = self.PlayerFirstPress(sArea)
					for r in range(iStart, Rules_3):
						# Get all area name
						sArea_1 = Rules_3x3x3[r][0][0]
						sArea_2 = Rules_3x3x3[r][1][0]
						sArea_3 = Rules_3x3x3[r][2][0]
						# Get all type of index {intex}
						Index_1 = self.GetIndexFromArea(sArea_1)
						Index_2 = self.GetIndexFromArea(sArea_2)
						Index_3 = self.GetIndexFromArea(sArea_3)
						# Get all position for {i}
						Pos1_i = int(Rules_3x3x3[r][0][1])
						Pos2_i = int(Rules_3x3x3[r][1][1])
						Pos3_i = int(Rules_3x3x3[r][2][1])
						# Get all position for {j}
						Pos1_j = int(Rules_3x3x3[r][0][2])
						Pos2_j = int(Rules_3x3x3[r][1][2])
						Pos3_j = int(Rules_3x3x3[r][2][2])
						
						# Check Player position
						if (c == 0):
							if (Game[Index_1][Pos1_i][Pos1_j] == TTT_O and Game[Index_2][Pos2_i][Pos2_j] == TTT_O and Game[Index_3][Pos3_i][Pos3_j] == 0):
								self.ButtonPress(sArea_3, Pos3_i, Pos3_j)
								presed_button = True
								break
							elif (Game[Index_1][Pos1_i][Pos1_j] == TTT_O and Game[Index_2][Pos2_i][Pos2_j] == 0 and Game[Index_3][Pos3_i][Pos3_j] == TTT_O):
								self.ButtonPress(sArea_2, Pos2_i, Pos2_j)
								presed_button = True
								break
							elif (Game[Index_1][Pos1_i][Pos1_j] == 0 and Game[Index_2][Pos2_i][Pos2_j] == TTT_O and Game[Index_3][Pos3_i][Pos3_j] == TTT_O):
								self.ButtonPress(sArea_1, Pos1_i, Pos1_j)
								presed_button = True
								break
						
						# Check Player position
						if (c == 1):
							if (Game[Index_1][Pos1_i][Pos1_j] == TTT_X and Game[Index_2][Pos2_i][Pos2_j] == TTT_X and Game[Index_3][Pos3_i][Pos3_j] == 0):
								self.ButtonPress(sArea_3, Pos3_i, Pos3_j)
								presed_button = True
								break
							elif (Game[Index_1][Pos1_i][Pos1_j] == TTT_X and Game[Index_2][Pos2_i][Pos2_j] == 0 and Game[Index_3][Pos3_i][Pos3_j] == TTT_X):
								self.ButtonPress(sArea_2, Pos2_i, Pos2_j)
								presed_button = True
								break
							elif (Game[Index_1][Pos1_i][Pos1_j] == 0 and Game[Index_2][Pos2_i][Pos2_j] == TTT_X and Game[Index_3][Pos3_i][Pos3_j] == TTT_X):
								self.ButtonPress(sArea_1, Pos1_i, Pos1_j)
								presed_button = True
								break
						
						# Find free position
						if (c == 2):
							if (Game[Index_1][Pos1_i][Pos1_j] == 0):
								self.ButtonPress(sArea_1, Pos1_i, Pos1_j)
								presed_button = True
								break
							elif (Game[Index_1][Pos1_i][Pos1_j] == TTT_O and Game[Index_2][Pos2_i][Pos2_j] == 0):
								self.ButtonPress(sArea_2, Pos2_i, Pos2_j)
								presed_button = True
								break
							elif (Game[Index_1][Pos1_i][Pos1_j] == TTT_O and Game[Index_2][Pos2_i][Pos2_j] == TTT_O and Game[Index_3][Pos3_i][Pos3_j] == 0):
								self.ButtonPress(sArea_3, Pos3_i, Pos3_j)
								presed_button = True
								break
		
		# Game size: 4x4x4
		else:
			for c in range(0,3):
				if (presed_button == False): 
					# Verifica in care plan va pune Jucatorul prima casuta.
					iStart = self.PlayerFirstPress(sArea)
					for r in range(iStart, Rules_4):
						# Get all area name
						sArea_1 = Rules_4x4x4[r][0][0]
						sArea_2 = Rules_4x4x4[r][1][0]
						sArea_3 = Rules_4x4x4[r][2][0]
						sArea_4 = Rules_4x4x4[r][3][0]
						# Get all type of index {intex}
						Index_1 = self.GetIndexFromArea(sArea_1)
						Index_2 = self.GetIndexFromArea(sArea_2)
						Index_3 = self.GetIndexFromArea(sArea_3)
						Index_4 = self.GetIndexFromArea(sArea_4)
						# Get all position for {i}
						Pos1_i = int(Rules_4x4x4[r][0][1])
						Pos2_i = int(Rules_4x4x4[r][1][1])
						Pos3_i = int(Rules_4x4x4[r][2][1])
						Pos4_i = int(Rules_4x4x4[r][3][1])
						# Get all position for {j}
						Pos1_j = int(Rules_4x4x4[r][0][2])
						Pos2_j = int(Rules_4x4x4[r][1][2])
						Pos3_j = int(Rules_4x4x4[r][2][2])
						Pos4_j = int(Rules_4x4x4[r][3][2])
						
						# Check Player position
						if (c == 0):
							if (Game[Index_1][Pos1_i][Pos1_j] == TTT_O and Game[Index_2][Pos2_i][Pos2_j] == TTT_O and Game[Index_3][Pos3_i][Pos3_j] == TTT_O and Game[Index_4][Pos4_i][Pos4_j] == 0):
								self.ButtonPress(sArea_4, Pos4_i, Pos4_j)
								presed_button = True
								break
							elif (Game[Index_1][Pos1_i][Pos1_j] == TTT_O and Game[Index_2][Pos2_i][Pos2_j] == TTT_O and Game[Index_3][Pos3_i][Pos3_j] == 0 and Game[Index_4][Pos4_i][Pos4_j] == TTT_O):
								self.ButtonPress(sArea_3, Pos3_i, Pos3_j)
								presed_button = True
								break
							elif (Game[Index_1][Pos1_i][Pos1_j] == TTT_O and Game[Index_2][Pos2_i][Pos2_j] == 0 and Game[Index_3][Pos3_i][Pos3_j] == TTT_O and Game[Index_4][Pos4_i][Pos4_j] == TTT_O):
								self.ButtonPress(sArea_2, Pos2_i, Pos2_j)
								presed_button = True
								break
							elif (Game[Index_1][Pos1_i][Pos1_j] == 0 and Game[Index_2][Pos2_i][Pos2_j] == TTT_O and Game[Index_3][Pos3_i][Pos3_j] == TTT_O and Game[Index_4][Pos4_i][Pos4_j] == TTT_O):
								self.ButtonPress(sArea_1, Pos1_i, Pos1_j)
								presed_button = True
								break

						# Check Player position
						if (c == 1):
							if (Game[Index_1][Pos1_i][Pos1_j] == TTT_X and Game[Index_2][Pos2_i][Pos2_j] == TTT_X and Game[Index_3][Pos3_i][Pos3_j] == TTT_X and Game[Index_4][Pos4_i][Pos4_j] == 0):
								self.ButtonPress(sArea_4, Pos4_i, Pos4_j)
								presed_button = True
								break
							elif (Game[Index_1][Pos1_i][Pos1_j] == TTT_X and Game[Index_2][Pos2_i][Pos2_j] == TTT_X and Game[Index_3][Pos3_i][Pos3_j] == 0 and Game[Index_4][Pos4_i][Pos4_j] == TTT_X):
								self.ButtonPress(sArea_3, Pos3_i, Pos3_j)
								presed_button = True
								break
							elif (Game[Index_1][Pos1_i][Pos1_j] == TTT_X and Game[Index_2][Pos2_i][Pos2_j] == 0 and Game[Index_3][Pos3_i][Pos3_j] == TTT_X and Game[Index_4][Pos4_i][Pos4_j] == TTT_X):
								self.ButtonPress(sArea_2, Pos2_i, Pos2_j)
								presed_button = True
								break
							elif (Game[Index_1][Pos1_i][Pos1_j] == 0 and Game[Index_2][Pos2_i][Pos2_j] == TTT_X and Game[Index_3][Pos3_i][Pos3_j] == TTT_X and Game[Index_4][Pos4_i][Pos4_j] == TTT_X):
								self.ButtonPress(sArea_1, Pos1_i, Pos1_j)
								presed_button = True
						
						# Find free position
						if (c == 2):
							if (Game[Index_1][Pos1_i][Pos1_j] == 0 and Game[Index_2][Pos2_i][Pos2_j] == 0 and Game[Index_3][Pos3_i][Pos3_j] == 0 and Game[Index_4][Pos4_i][Pos4_j] == 0):
								self.ButtonPress(sArea_1, Pos1_i, Pos1_j)
								presed_button = True
								break							
							elif (Game[Index_1][Pos1_i][Pos1_j] == TTT_O and Game[Index_2][Pos2_i][Pos2_j] == 0 and Game[Index_3][Pos3_i][Pos3_j] == 0 and Game[Index_4][Pos4_i][Pos4_j] == 0):
								self.ButtonPress(sArea_2, Pos2_i, Pos2_j)
								presed_button = True
								break							
							elif (Game[Index_1][Pos1_i][Pos1_j] == TTT_O and Game[Index_2][Pos2_i][Pos2_j] == TTT_O and Game[Index_3][Pos3_i][Pos3_j] == 0 and Game[Index_4][Pos4_i][Pos4_j] == 0):
								self.ButtonPress(sArea_3, Pos3_i, Pos3_j)
								presed_button = True
								break														
							elif (Game[Index_1][Pos1_i][Pos1_j] == TTT_O and Game[Index_2][Pos2_i][Pos2_j] == TTT_O and Game[Index_3][Pos3_i][Pos3_j] == TTT_O and Game[Index_4][Pos4_i][Pos4_j] == 0):
								self.ButtonPress(sArea_4, Pos4_i, Pos4_j)
								presed_button = True
								break
					
		# Cauta butonul liber, daca jocul se va termina remiza
		if (presed_button == False):
			self.FinishSolutionPress()
			presed_button = True
		return 0

