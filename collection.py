# Import statements
from PIL import ImageTk,Image
import numpy as np
import pandas as pand
import matplotlib as mpl
import pendulum as pend
from upgrade import Upgrade
from pilot import Pilot

class Collection:

    # Constructs rudimentary database of all X-Wing 2.0 Pilot Cards and Upgrade Cards
    def __init__(self):
        # Contains all upgrades
        self.upgrades = [

            # All Talent Upgrades
            Upgrade(name='Composure', points=1, utype='Talent'),
            Upgrade(name='Deadeye Shot', points=1, utype='Talent'),
            Upgrade(name='Heroic', points=1, utype='Talent'),
            Upgrade(name='Marg Sabl Closure', points=1, utype='Talent')
        ]
        
        self.pilots = [
            Pilot('Poe Dameron [HoH]', 60, 'T-70 X-Wing', ['Resistance'], [3, 2, 4, 3], ['Focus', 'Target Lock', 'Boost'], ['Talent', 'Tech', 'Configuration', 'Hardpoint', 'Astromech', 'Modification', 'Title'])
        ]

    ### Function to return a list containing either Pilot or Upgrade objects that meet the search requirements
      # (ctype refers to Card Type)
      # (ctype = 0 means the function should return a list containing Pilot objects)
      # (ctype = 1 means the function should return a list containing Upgrade objects)
    def getOptions(self, ctype=0, name='None', stype='None', utype='None', tag='None'):
        options = []
        
        # ctype == 0 indicates that the returned list of options should contain entries of type Pilot
        if ctype == 0:
            for p in self.pilots:
                # If the search finds an Upgrade with the same 'name' as the one searched for, adds Upgrade to return options (the returned list of options)
                if p.name == name: 
                    options.append(p)
                # If the search finds an Upgrade with the same 'utype' as the one searched for, adds Upgrade to return options (the returned list of options)
                if p.stype == stype:
                    options.append(p)
                # If the search finds an Upgrade with one of the tags the same as the one searched for, adds Upgrade to return options (the returned list of options)
                for t in p.tags:
                    if t == tag:
                        options.append(p)

        # ctype == 1 indicates that the returned list of options should contain entries of type Upgrade
        elif ctype == 1:
            for u in self.upgrades:
                # If the search finds an Upgrade with the same 'name' as the one searched for, adds Upgrade to return options (the returned list of options)
                if u.name == name: 
                    options.append(u)
                # If the search finds an Upgrade with the same 'utype' as the one searched for, adds Upgrade to return options (the returned list of options)
                if u.utype == utype:
                    options.append(u)
        
        for e in options:
            print(e.name, e.points)

        return options


x = Collection()
x.getOptions(0, tag='Resistance')