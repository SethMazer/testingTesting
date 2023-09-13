from tkinter import *
import socket
import time
import os


#########################################
#Setting up client server and returned data variable
recievedData = None

def startConnection():

    #Setting up IPV4 and TCP protocol
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Defining server connection address/ip/port and connecting to server
    serverAddress = ("72.66.11.84", 8080)
    clientSocket.connect(serverAddress)
   
    #Sending test message to server
    message = "Hello, desktop computer!"
    clientSocket.send(message.encode('utf-8'));

    #Recieving data(message) from server
    global recievedData
    
    recievedData = clientSocket.recv(1024)
    recievedData = recievedData.decode('utf-8')
    
    
    #Closing process
    clientSocket.close()

    #Printing successful connection message:
    connectionMessage = f"Sucessfully connected to server @ {'192.168.1.181:8080'}"
    connectionMessageOut = Label(Window, text = connectionMessage, font = 10)
    clientCanvas.create_window(300,425, window = connectionMessageOut)

    #Printing data out to GUI
    dataMessage = recievedData
    dataMessageOut = Label(Window, text = dataMessage, font = 15)
    clientCanvas.create_window(300, 500, window = dataMessageOut)

   



##############################################
#Setting up tkinter gui
Window = Tk()

#Window Geometry
Window.geometry("600x600")
Window.title("Client Portal")

#Setting up Canvas
clientCanvas = Canvas(Window, width = 600, height = 600)
clientCanvas.pack()


#Decorating canvas, setting up buttons, setting up lables and such.

#Consturcting welcome message
getClientUserName = os.path.expanduser("~");
clientUserName = os.path.basename(getClientUserName)

welcomeMessage = f"Welcome {clientUserName}"

welcomeLabel = Label(Window, text = welcomeMessage, font=("Arial", 25))
clientCanvas.create_window(300,150, window = welcomeLabel)



#Constructing to connect button
connectButton = Button(Window, text="Connect", font = 25, border = 5, command = startConnection, height = 5, width = 20)
clientCanvas.create_window(300,300, window = connectButton)







































################################################
Window.resizable(False, False)
Window.mainloop()