# Overhead imports
import PIL.Image
import numpy as np
import pandas as pand
import matplotlib as mpl
import pendulum as pend
from tkinter import *
from tkmacosx import Button

# Local imports
from ship import Ship
from pilot import Pilot
from upgrade import Upgrade
from collection import Collection
from squad_builder import SquadBuilder

# Global Variables
factionGridCol = -1

# Create and initialize a black GUI
xwingRoot = Tk()
xwingRoot.title('X-Wing 2.0 Squad Builder (Version 1.0)')
xwingRoot.geometry('2000x1500')
xwingRoot.configure(background='black')

# Initialize a new list-builder

def addFactionButton(faction):
    global factionGridCol
    factionGridCol += 1
    imgLocation = 'Images/Factions/{}-icon.png'.format(faction)
    img = PhotoImage(file=imgLocation)
    factionButton = Button(xwingRoot, text='', height=50, width=60, bg='black', focuscolor='white', borderless=True, image=img, command=lambda: getFaction(faction, ''))
    factionButton.grid(row='0', column=str(factionGridCol))

def getFaction(faction, name):
    name = 'Unamed Squadron'
    print(faction)
    lb = SquadBuilder(faction, name)

addFactionButton('rebel')
addFactionButton('imperial')
addFactionButton('scum')
addFactionButton('resistance')
addFactionButton('firstorder')
addFactionButton('republic')
addFactionButton('separatist')

# Display GUI until program ends
xwingRoot.mainloop()



