from threading import Thread
import random
from tkinter import *
from tkinter import messagebox

from socket import *

# Global variables
player = 0  # Indicates which player's turn it is (1 for client, 0 for server)
meScore = 100  # Score of the client
oppositeScore = 100  # Score of the server

# Function to check win condition
def check():
    if meScore <= 0:
        win("Client")
    elif oppositeScore <= 0:
        win("Server")

# Function to display winner and close the window
def win(player):
    messagebox.showinfo("Winner", player + " wins!")
    wind.destroy()

# Function for client's turn
def clicked1():
    global player
    global meScore
    if player == 1:
        player = 0  # Switch turn to server
        roll_value = random.randint(0, 20)
        meScore -= roll_value
        sendPlay(roll_value)
        check()

# Function to send play to the server
def sendPlay(roll_value):
    showStatus("You rolled: {}".format(roll_value))
    lbMe["text"] = "Client: {}".format(meScore)
    n = str(meScore).encode()
    soc.send(n)

# Function to handle server's play
def handlePlay(score):
    global player
    global oppositeScore
    oppositeScore = score
    lbServer["text"] = "Server: {}".format(oppositeScore)
    player = 1
    check()

# Function to apply play received from server
def applyPlay(play):
    showStatus("Your Turn")
    play = play.decode()
    play = int(play)
    handlePlay(play)

# Function to update status label
def showStatus(msg):
    lbStatus["text"] = msg

# GUI setup
wind = Tk()
wind.title("Dice Roll - Client")

lbMe = Label(wind, text="Me: 100", font=('Helvetica', 20))
lbMe.grid(row=0, column=0)

lbServer = Label(wind, text="Server: 100", font=('Helvetica', 20))
lbServer.grid(row=0, column=1)

lbStatus = Label(wind, text="Waiting", font=('Helvetica', 20))
lbStatus.grid(row=1, columnspan=2)

btn1 = Button(wind, text="Roll", fg="black", font='Helvetica', command=clicked1)
btn1.grid(row=2, columnspan=2, pady=10)

# Networking setup
soc = socket(AF_INET, SOCK_STREAM)
showStatus("Connecting to server...")

def connectServer():
    global soc
    soc.connect(("127.0.0.1", 6000))
    showStatus("Connected")
    t = Thread(target=rec)
    t.start()

def rec():
    while True:
        play = soc.recv(10)
        applyPlay(play)

tConnect = Thread(target=connectServer)
tConnect.start()

# Run the window
wind.mainloop()
