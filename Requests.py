import requests 

# URL API POST Requrst
API_ENDPOINT = "http://demo.aninu.ro/PyTicTacToe3D/post.php"
  
# Define function
def Send_POST(player, win, fail, mode): 
    data = {'api_player':player, 'api_win':win, 'api_fail':fail, 'api_mode':mode} 
    r = requests.post(url = API_ENDPOINT, data = data) 
    print ("[Request]: Received: {" + str(r.text) + "}")
    return 0
