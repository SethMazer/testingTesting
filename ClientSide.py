#Importing libraries
import socket
import time

#Setting up ip protocol and data protocol (ipv4 and tcp)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Defining server adress and port
server_adress = ('192.168.1.162', 8080)

#Connecting to the server
client_socket.connect(server_adress)

#Sending data message to server
message = "Hello, desktop computer!"
client_socket.send(message.encode('utf-8'));

#Recieving data from server computer
data = client_socket.recv(1024)
recievedMessage = data.decode('utf-8');

#Closing client side socket and printing message
client_socket.close()
print("Recieved:", recievedMessage);

time.sleep(75)
