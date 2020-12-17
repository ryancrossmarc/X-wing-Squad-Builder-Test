# Import statements
from PIL import ImageTk,Image
import numpy as np
import pandas as pand
import matplotlib as mpl
import pendulum as pend

class Upgrade:
    def __init__(self, name, points, uType, tags='', conditions=''):
        self.name = name
        self.points = points
        self.uType = uType
        self.tags = tags
        self.conditions = conditions
