#!/usr/bin/python3

"""
Tic Tac Toe 3D
In aceasta librarie se face legatura intre joc si serverul socket.

Mai multe detalii: http://aninu.xyz/post/tic-tac-toe-3d-python3/
"""

__version__ = '1.2'
__date__    = '15.01.2020'
__author__  = 'Anghelina Alin <dev@aninu.ro>'

# Import
import socket
import sys

# Variables
state = False
soc = None

def connect_to_server():
    global soc, state
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8888

    try:
        soc.connect((host, port))
        print ("[Socket]: Server is ready to use.")
        state = True
    except:
        print("[Socket]: Failed to connect to server.")

def message_to_server(message):
    global soc, state
    if (state == True):
        soc.sendall(message.encode("utf8"))
        if soc.recv(5120).decode("utf8") == "-":
            print ("[Socket]: Received an invalid command.")
            pass
    return

connect_to_server()
message_to_server("Un jucator nou s-a conectat pe server.")
