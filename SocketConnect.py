import socket

#Startup
print("Weclome to SocketConnect")
host = input("Please specify a host ")
port = int(input("Please specify a port "))

#Make a socket
obj = socket.socket()
obj.connect((host,port))

#Send a message
message = input("Please enter your message:  ")
obj.send(message.encode())
data = obj.recv(1024).decode()
print('Received from server: ' + data)
obj.close()
