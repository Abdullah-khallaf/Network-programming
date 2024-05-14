from threading import Thread
import random
from tkinter import *
from tkinter import messagebox

from socket import *

# Global variables
player = 0  # Indicates which player's turn it is (1 for server, 0 for client)
meScore = 100  # Score of the server
oppositeScore = 100  # Score of the client

# Function to check win condition
def check():
    if meScore <= 0:
        win("Server")
    elif oppositeScore <= 0:
        win("Client")

# Function to display winner and close the window
def win(player):
    messagebox.showinfo("Winner", player + " wins!")
    wind.destroy()

# Function for server's turn
def clicked1():
    global player
    global meScore
    if player == 1:
        player = 0  # Switch turn to client
        roll_value = random.randint(0, 20)
        meScore -= roll_value
        sendPlay(roll_value)
        check()

# Function to send play to the client
def sendPlay(roll_value):
    showStatus("You rolled: {}".format(roll_value))
    lbMe["text"] = "Server: {}".format(meScore)
    n = str(meScore).encode()
    c.send(n)

# Function to handle client's play
def handlePlay(score):
    global player
    global oppositeScore
    oppositeScore = score
    lbClient["text"] = "Client: {}".format(oppositeScore)
    player = 1
    check()

# Function to apply play received from client
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
wind.title("Dice Roll - Server")

lbMe = Label(wind, text="Me: 100", font=('Helvetica', 20))
lbMe.grid(row=0, column=0)

lbClient = Label(wind, text="Opponent: 100", font=('Helvetica', 20))
lbClient.grid(row=0, column=1)

lbStatus = Label(wind, text="Waiting", font=('Helvetica', 20))
lbStatus.grid(row=1, columnspan=2)

btn1 = Button(wind, text="Roll", fg="black", font='Helvetica', command=clicked1)
btn1.grid(row=2, columnspan=2, pady=10)

# Networking setup
soc = socket(AF_INET, SOCK_STREAM)
soc.bind(("127.0.0.1", 6000))
soc.listen(5)
c = None

# Function to handle client connection
def handleClient():
    global player
    global c
    player = 1
    c, ad = soc.accept()
    showStatus("A player connected\nYour Turn")
    t = Thread(target=rec, args=[c,])
    t.start()

# Function to receive data from client
def rec(c):
    while True:
        play = c.recv(10)
        applyPlay(play)

# Thread to handle client connection
acc = Thread(target=handleClient)
acc.start()

showStatus("Waiting...")

# Run the window
wind.mainloop()
