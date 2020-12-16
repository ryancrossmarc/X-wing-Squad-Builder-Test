# Import statements
import PIL as pil
import numpy as np
import pandas as pand
import matplotlib as mpl
import pendulum as pend
from tkinter import *

GUI = Tk()
GUI.title('X-Wing 2.0 Squad Builder Version 1.0')
GUI.configure(background='black')

photo = PhotoImage(file='Images/Pilots/poe-dameron-1.png')
labelphoto = Label(GUI, image=photo)
labelphoto.pack()

# Keep
GUI.mainloop()