# TicTacToe3D
Tic-tac-toe is a paper-and-pencil game for two players, X and O, who take turns marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

Versions of game (https://github.com/aaninu/TicTacToe3D/releases):

**1.0:** The game contain size of the window (3 or 4) and the style. Play with the computer. Change the name of player. 

**1.1:** Contain **1.0** and a REST API for share the informations about score to a web server.  

**1.2:** Contain **1.1** and a Client / Server Socket.

**1.3:** Contain **1.2** and using ***ipify.org*** will show the IPv4 Address when the game is open. 

# Packages
- pygame
- tkinter
- requests
- socket
- sys
- traceback
- threading

# Installation guide
Install python3 on your device (https://www.python.org/)

Check if you have all packages installed and is something not found use the command for install it: 

```shell
pip install {pachage_name}
```

# Play game
Open Terminal app or CMD and use the commands:

**Version 1.0 and 1.1 (Without Socket Server)**
```shell
cd {LocationOfGame}
python3 PyTicTacToe3D.py
```

**Version 1.2 (With Socket Server)** You will need two console open.
```shell
# Console 1
cd {LocationOfGame}
python3 Server.py

# Console 2
cd {LocationOfGame}
python3 PyTicTacToe3D.py
```

