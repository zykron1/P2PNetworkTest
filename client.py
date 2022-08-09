"""
This client lives on port 3000.
Model:
    Client => Server: Hi, I'd like to book a meeting. Sure, your number is 0
    (Client waits for connections)
    Client2 => Server: Heyyyy, who's id is 0? Yeah its 127.0.0.1:3000
    Client2 => Client(aka 3000) Hello, can you hear me, I've been in california dreaming... SHUT UP LOSER!!!!!!!!!!!!! WHO GAVE YOU THIS NUMBER
"""
import socket

#Setup
obj = socket.socket()
obj.connect(('127.0.0.1',2000))
obj.send("MakeConn 3000".encode())

#Get response and end the call
output = obj.recv(1024).decode()
print(f"Output from server: {output}")
obj.close()
