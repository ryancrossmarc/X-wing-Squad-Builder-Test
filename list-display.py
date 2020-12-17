# Overhead imports
from PIL import ImageTk,Image
import numpy as np
import pandas as pand
import matplotlib as mpl
import pendulum as pend
from tkinter import *

# Local imports
from ship import Ship
from pilot import Pilot
from upgrade import Upgrade
from collection import Collection

# Create and initialize a black GUI
xwingRoot = Tk()
xwingRoot.title('X-Wing 2.0 Squad Builder (Version 1.0)')
xwingRoot.geometry('2000x1500')
xwingRoot.configure(background='black')

# Add photo to GUI
photo = PhotoImage(file='Images/Pilots/poe-dameron-1.png')
#labelphoto = Label(xwingRoot, image=photo)
#labelphoto.pack()

### Create dropdown menu ###
getDropDown = Collection()

### Get faction from dropdown ###
FACTIONS = ['Rebel', 'Empire', 'Scum', 'Resistance', 'First Order', 'Republic', 'Separtist']

factionDisplay = StringVar(xwingRoot) # Display faction dropdown
factionDisplay.set(FACTIONS[0]) # Set default dropdown value
factionLBL = OptionMenu(xwingRoot, factionDisplay, *FACTIONS)
factionLBL.pack()

var = IntVar()
button = Button(xwingRoot, text='ready', command=lambda: var.set(1))
button.place(relx=.5, rely=.5, anchor='c')
button.wait_variable(var)

### Get Ships based on faction ###
info = getDropDown.getOptions(0, tag=factionDisplay.get()) # Get whichever faction the user selected
SHIPS = []
for ship in info:
    if ship.sType not in SHIPS:
        SHIPS.append(ship.sType)

if not not SHIPS:
    info = SHIPS[0]
    del SHIPS[0]

    ship1 = StringVar(xwingRoot) # Display dropdown
    ship1.set(info) # Set default dropdown value
    w = OptionMenu(xwingRoot, ship1, info, *SHIPS)
    w.pack()

var = IntVar()
button = Button(xwingRoot, text='ready', command=lambda: var.set(1))
button.place(relx=.5, rely=.5, anchor='c')
button.wait_variable(var)

### Get Pilots based on Ship ###
PILOTS = getDropDown.getPilotNamesAndPoints(sType=ship1.get())

if not not PILOTS:
    info = PILOTS[0]
    del PILOTS[0]

    pilot1 = StringVar(xwingRoot) # Display dropdown
    pilot1.set(info) # Set default dropdown value
    w = OptionMenu(xwingRoot, pilot1, info, *PILOTS)
    w.pack()

# NOTE: get value from list: ship1.get()

# Display GUI until program ends
xwingRoot.mainloop()