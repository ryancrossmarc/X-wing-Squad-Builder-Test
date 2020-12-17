# Import statements
from PIL import ImageTk,Image
import numpy as np
import pandas as pand
import matplotlib as mpl
import pendulum as pend
from pilot import Pilot

class Ship:
    def __init__(self, pilot, sType, tags=[], sAbility='', stats=[], actions=[]):
        self.pilot = pilot
        self.sType = sType
        self.tags = tags
        self.sAbility = sAbility
        self.stats = stats
        self.actions = actions