# Import statements
from PIL import ImageTk,Image
import numpy as np
import pandas as pand
import matplotlib as mpl
import pendulum as pend

class Pilot:
    def __init__(self, name, points, upgrades=[], pAbility=''):
        self.name = name
        self.points = points
        self.upgrades = upgrades
        self.pAbility = pAbility