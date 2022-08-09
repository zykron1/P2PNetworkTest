"""
This socket is a middle man to help clients connect
"""
import socket

#Create a socket
s = socket.socket()
print("Socket successfully created")

#Define the port
port = 2000

#Setup QuickStore
QuickStore = []

#Bind the port to the socket
s.bind(('', port))        
print("Socket binded to %s" %(port))

#Have the socket into Listen Mode
s.listen(5)

while True:
    # Establish connection with client.
    c, addr = s.accept()    
    print ('Got connection from', addr ) 
    #Print the clients message
    request = c.recv(1024).decode()
    print(f"[MESSAGE] {addr} sent {request}")
    
    #Parse the request
    phrases = request.split(" ")
    if phrases[0] == "MakeConn":
        #Send a message back to the client
        QuickStore.append(addr)
        c.send(str(len(QuickStore)-1).encode())
    if phrases[0] == "GetConn":
        try:
            c.send(str(QuickStore[int(phrases[1])][).encode())
        except:
            c.send("Invalid Input".encode())
    # Close the connection with the client
    c.close() 
