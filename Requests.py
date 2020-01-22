#!/usr/bin/python3

"""
Tic Tac Toe 3D
In aceasta librarie se face legatura cu REST API.

Mai multe detalii: http://aninu.xyz/post/tic-tac-toe-3d-python3/
"""

__version__ = '1.2'
__date__    = '15.01.2020'
__author__  = 'Anghelina Alin <dev@aninu.ro>'

# Import
import requests 

# URL API POST Requrst
API_ENDPOINT = "{YOUR_URL}/PyTicTacToe3D/post.php"
  
# Define function
def Send_POST(player, win, fail, mode): 
    data = {'api_player':player, 'api_win':win, 'api_fail':fail, 'api_mode':mode} 
    r = requests.post(url = API_ENDPOINT, data = data) 
    print ("[Request]: Received: {" + str(r.text) + "}")
    return 0

# Show My IP Address
def Get_IPAddress():
    print ("[Request.IPv4]: Show my IPv4")
    try:
        url = "http://api.ipify.org?format=json"
        r = requests.get(url = url) 
        print ("[Request.IPv4]: Received: {" + str(r.text) + "}")
    except Exception as ex:
        print ("[Request.IPv4]: Received an error: {" +str(ex)+ "}")
        
    return 0
  
