# Import statements
from PIL import ImageTk,Image
import numpy as np
import pandas as pand
import matplotlib as mpl
import pendulum as pend
from tkinter import *

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
SHIPS = [
    'Fireball',
    'MG-100 StarFortress',
    'T-70 X-Wing'
]

ship1 = StringVar(xwingRoot)
ship1.set(SHIPS[0]) # defualt value
w = OptionMenu(xwingRoot, ship1, *SHIPS)
w.pack()

# NOTE: get value from list: ship1.get()

# Display GUI until program ends
xwingRoot.mainloop()