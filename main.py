"""
This socket is a middle man to help clients connect
"""
import socket

#Create a socket
s = socket.socket()
print("Socket successfully created")

#Define the port
port = 2000

#Bind the port to the socket
s.bind(('', port))        
print("socket binded to %s" %(port))

#Have the socket into Listen Mode
s.listen(5)

while True:
    # Establish connection with client.
    c, addr = s.accept()    
    print ('Got connection from', addr )

    # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())
    
    #Print the clients message
    request = c.recv(1024).decode()
    print(f"[MESSAGE] {addr} sent {request}")

    # Close the connection with the client
    c.close() 
