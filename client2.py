"""
This model does not live on a port, instead it talks to the server
Model:
    (Client waits for connections)
    Client2 => Server: Heyyyy, who's id is 0? Yeah its 127.0.0.1:3000
    Client2 => Client(aka 3000) Hello, can you hear me, I've been in california dreaming... SHUT UP LOSER!!!!!!!!!!!!! WHO GAVE YOU THIS NUMBER
"""
import socket

#Setup
obj = socket.socket()
obj.connect(('127.0.0.1',2000))
obj.send("GetConn 0".encode())

#Get response and end the call
output = obj.recv(1024).decode()
print(f"Output from server: {output}")
obj.close()
