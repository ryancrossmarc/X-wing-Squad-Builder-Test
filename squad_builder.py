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

class SquadBuilder:
    def __init__(self, faction, name):
        self.faction = faction
        self.name = name
        self.ships = []

    def addShip(self):
        return
    
    def getShip(self):
        return

    def cloneShip(self):
        return
    
    def deleteShip(self):
        return

    def upgradeShip(self):
        return