# Import statements
from PIL import ImageTk,Image
import numpy as np
import pandas as pand
import matplotlib as mpl
import pendulum as pend

class Pilot:
    def __init__(self, name, points, stype, tags=[], stats=[], actions=[], upgrades=[], conditions=[]):
        self.name = name
        self.points = points
        self.stype = stype
        self.tags = tags
        self.stats = stats
        self.actions = actions
        self.upgrades = upgrades
        self.conditions = conditions