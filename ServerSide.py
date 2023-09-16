#Importing library
import socket
import struct
import time

#Setting up socket type (ipv4) and socket protocol(tcp)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Setting up host and port
host = "192.168.1.181"
port = 8080

#Binding endpoint to this server computer and printing listening statement
server_socket.bind((host, port))
print(f"Server is listening on {host}:{port}")

#Listening for inoming connections using .listen
server_socket.listen(5)

#Accept incoming connections and printing acceptance statement
clientSocket, client_address = server_socket.accept()
print(f"Accepted Connection from {client_address}")

#Recieve data from client and print recieved statement
# data = clientSocket.recv(1024)
# print(f"Recieved data: {data.decode('utf-8')}")


#Sending response back to client
response = "Sucessfully connected to server"
clientSocket.send(response.encode('utf-8'))

#Recieve data from client and print recieved statement
clientAction = clientSocket.recv(1024)
print(f"Client Action: {clientAction.decode('utf-8')}")

##############################################
#Accessing data

dataRowBytes = (clientSocket.recv(4))
dataRowInt = (struct.unpack("!I", dataRowBytes)[0])

print(f"Data row requested: {dataRowInt}")

#Traversing carData.txt

#Current row of file
currentRow = 0

data = None
with open(r"C:\Users\boomc\OneDrive\Documents\Server-Side\carData.txt", "r") as file:
    
    #Looping through each row in carData.txt
    for line in file:
        currentRow += 1
        if currentRow == dataRowInt:
            data = line.strip()
            print(data)
            
            
#Sending data back to client
dataForTransit = data.encode('utf-8')
clientSocket.send(dataForTransit)

    













#Closing client and server sockets
time.sleep(100)

clientSocket.close()
server_socket.close()

time.sleep(75)