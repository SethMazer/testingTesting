#Importing library
import socket
import time

#Setting up socket type (ipv4) and socket protocal (tcp)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Setting up host and port
host = "192.168.1.162"
port = 8080

#Binding endpoint to this server computer, and printing listening statement
server_socket.bind((host, port))
print(f"Server is listening on {host}:{port}")

#Listening for incoming connections using .listen
server_socket.listen(5)

#Accept incoming connections and printing acceptance statement
client_socket, client_adress = server_socket.accept()
print(f"Accepted connection from {client_adress}")

#Recieve data from client computer, and printing recieved statement
data = client_socket.recv(1024);
print(f"Received data: {data.decode('utf-8')}")


#Sending response back to client computer
response = "Hello, connected to blue laptop!"
client_socket.send(response.encode('utf-8'));

#Closing both client and server sockets

client_socket.close()
server_socket.close()

time.sleep(75)