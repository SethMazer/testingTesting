#Importing necessary libraries
from tkinter import *
import socket
import struct
import os


#########################################
#Setting up client server and returned data variable
recievedData = None
currentPage = None

#Starting intitial connection with server
def startInitialConnection():
    global clientSocket

    #Setting up IPV4 and TCP protocol
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Defining server connection address/ip/port and connecting to server
    serverAddress = ("72.66.11.84", 8080)
    clientSocket.connect(serverAddress)
   
    #Recieving data(message) from server
    global recievedData
    
    recievedData = clientSocket.recv(1024)
    recievedData = recievedData.decode('utf-8')
    

    #Closing process
    #clientSocket.close()

    #Printing data out to GUI
    dataMessage = recievedData
    dataMessageOut = Label(Window, text = dataMessage, font = 15, bg = "cadetblue1")
    homePage.create_window(300, 400, window = dataMessageOut)

    createContinueButton()


#Getting data from server by sending row number to servers row variable, to then traverse row data and return the string at specified row
#Then recieving data back from server and displaying data at specified row
def getData():
    
    #getting row number, packing it to struct, turn int to bytes to send over
    dataRowLine = int(dataRow.get())
    dataForTransit = struct.pack("!I", dataRowLine)

    #Sending row num to server
    clientSocket.send(dataForTransit)

    #Recieving data back and printing it to GUI
    dataRecieved = clientSocket.recv(1024)
    dataRecieved = dataRecieved.decode('utf-8')

    print(dataRecieved)

    dataToDisplayFont = ("Helvetica", 12)
    dataToDisplay = dataRecieved
    dataToDisplayOut = Label(Window, text = dataToDisplay, font = dataToDisplayFont, bg = "cadetblue1")
    dataPage.create_window(300, 400, window = dataToDisplayOut)

    clientSocket.close()






#Logging client actions, if client clicks continue, send server message that client moved to data viewing else do sum else
def clientActions(clientActionCode):
    #Moved Page
    if(clientActionCode == 1):
        actionMessage = "Client moved to data viewing page"
        clientSocket.send(actionMessage.encode('utf-8'))
    elif(clientActionCode == 2):
        actionMessage = "Client did sum else ????"
        clientSocket.send(actionMessage.encode('utf-8'))



#Function for creating continueButton
def createContinueButton():

    #Commands for continueButton
    def continueButtonCommands():
        clientActions(1)
        changePage()

    #Constructing continue button
    continueButton = Button(Window, text = "Continue", height = 3, width = 8, command=continueButtonCommands)
    homePage.create_window(300, 450, window = continueButton)

    

##############################################
#Home page setup
def goHomePage():
    #Setting up Canvas
    global homePage
    homePage = Canvas(Window, width = 600, height = 600, bg = "cadetblue1")
    homePage.pack()

    #Decorating canvas, setting up buttons, setting up lables and such.
    #Consturcting welcome message
    getClientUserName = os.path.expanduser("~");
    clientUserName = os.path.basename(getClientUserName)

    #Welcome message/label
    welcomeFont = ("Helvetica", 25)
    welcomeMessage = f"Welcome {clientUserName}"
    welcomeLabel = Label(Window, text = welcomeMessage, font=welcomeFont, bg="cadetblue1")
    homePage.create_window(300,150, window = welcomeLabel)


    #Constructing connect button
    connectButton = Button(Window, text="Connect",font = 15  ,border = 5, command = startInitialConnection, height = 5, width = 20,)
    homePage.create_window(300,300, window = connectButton)


#Data page setup
def goDataPage():
    #Setting up canvas
    global dataPage
    dataPage = Canvas(Window, width = 600, height = 600, bg = "cadetblue1")
    dataPage.pack()

    #Get random car brand label
    getDataLabelFont = ("Helvetica", 25)
    getDataLabel = Label(Window, text = "Click button to get data from server", font = getDataLabelFont, bg = "cadetblue1")
    dataPage.create_window(300,150, window = getDataLabel)


    #Enter Row Label
    enterRowFont = ("Helvetica", 12)
    enterRowLabel = Label(Window, text = "Enter row for data field", font = enterRowFont, bg = "cadetblue1")
    dataPage.create_window(300, 200, window = enterRowLabel)

    #Enter row data entry field
    global dataRow
    dataRow = Entry(dataPage)
    dataPage.create_window(300, 250, window = dataRow)


    #Get data button
    getDataButton = Button(Window, text = "get Data", border = 5, height = 3, width = 8, command = getData)
    dataPage.create_window(300,300 , window = getDataButton)




#Changing pages, by hiding current widgets and showing next
def changePage():
    homePage.pack_forget()
    goDataPage()


#Setting up tkinter window a geometry
Window = Tk()
Window.geometry("600x600")
Window.title("Client Portal")

#Showing page
goHomePage()
































################################################
Window.resizable(False, False)
Window.mainloop()