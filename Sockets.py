import socket
import sys

state = False
soc = None


def connect_to_server():
    global soc
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
    global soc
    soc.sendall(message.encode("utf8"))
    if soc.recv(5120).decode("utf8") == "-":
        print ("[Socket]: Received an invalid command.")
        pass

connect_to_server()
message_to_server("Un jucator nou s-a conectat pe server.")
