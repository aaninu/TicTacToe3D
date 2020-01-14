#!/usr/bin/python3

"""
Tic Tac Toe 3D
Cu ajutorul acestei librarii se adauga efecte de sunet in joc.

In cadrul acesteia se foloseste libraria de python: pygame.

Mai multe detalii: http://aninu.xyz/post/tic-tac-toe-3d-python3/
"""

__version__ = '1.2'
__date__    = '01.01.2018'
__author__  = 'Anghelina Alin <dev@aninu.ro>'

# Import
import pygame

# Setari generale

# Sound Status
sound_status = True

# Sound Location for Button Game Press
SoundNameNormal = "./Sound/button-29.mp3"

# Sound Location for Win Game
SoundNameWin = "./Sound/button-37.mp3"

# Sound available:
# [./Sound/beep-08b.mp3]
# [./Sound/beep-02.mp3]
# [./Sound/beep-06.mp3]
# [./Sound/beep-29.mp3]
# [./Sound/button-10.mp3]
# [./Sound/button-29.mp3]
# [./Sound/button-37.mp3]

#-------------------------------------------------------------------------#
if (sound_status):
	pygame.init()
	pygame.mixer.init()

def PlaySound():
	"""
	Aceasta functie este apelata atunci cand este ocupata una dintre casutele jocului.
	"""
	global SoundNameNormal
	if (sound_status):
		pygame.mixer.music.load(SoundNameNormal)
		pygame.mixer.music.play(0)
	return 0

def PlaySoundWin():
	"""
	Aceasta functie este apelata atunci cand unul dintre jucatori castiga.
	"""
	global SoundNameWin
	if (sound_status):
		pygame.mixer.music.load(SoundNameWin)
		pygame.mixer.music.play(0)
	return 0

#-------------------------------------------------------------------------#
