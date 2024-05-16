import socket
from _thread import *
import sys

server = "192.168.68.133"
port = 5555 # some useless port number that isn't being used by my router

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INIT is the type of address we're using, SOCK_STREAM is the type of connection we're using

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2) # 2 players, blank means unlimited connections
print("Waiting for a connection, Server Started")

def threaded_client(conn, player):
    reply = ""
    while True:
        try:
            data = conn.recv(2048) # ammount of data we're receiving
            reply = data.decode("utf-8")

            # if there's no data, break
            if not data:
                print("Disconnected")
                break
            else:
                print("Received:", reply)
                print("Sending:", reply)
            
            conn.sendall(str.encode(reply))
        except:
            break



# continuously look for connections
while True:
    conn, addr = s.accept() # conn is the connection object, addr is the ip address
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))



