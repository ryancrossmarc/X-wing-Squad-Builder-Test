# Import statements
from PIL import ImageTk,Image
import numpy as np
import pandas as pand
import matplotlib as mpl
import pendulum as pend
from upgrade import Upgrade
from pilot import Pilot
from ship import Ship

class Collection:

    # Constructs rudimentary database of all X-Wing 2.0 Pilot Cards and Upgrade Cards
    def __init__(self):
        # Contains all upgrades
        self.upgrades = [

            # All Talent Upgrades
            Upgrade('Composure', 1, 'Talent'),
            Upgrade('Deadeye Shot', 1, 'Talent'),
            Upgrade('Heroic', 1, 'Talent', ['Resistance']),
            Upgrade('Marg Sabl Closure', 1, 'Talent')
        ]
        
        self.ships = [
            ### REBEL SHIPS ###
            Ship(Pilot('Norra Wexley', 55, ['Talent', 'Crew', 'Astromech', 'Torpedo', 'Gunner', 'Modification'], 'While you defend, if there is an enemy ship at range 0-1, add 1 evade result to your dice results.')
                                                ,'ARC-170 Starfighter', ['Rebel'], '', [5, 3, 2, 1, 6, 3, '0', '2'], ['Focus', 'Target Lock', 'Red Boost', 'Red Rotate']),

            ### RESISTANCE SHIPS ###
            # Scavenged YT-1300 Pilots
            Ship(Pilot('Rey', 68, ['Force', 'Crew', 'Gunner', 'Modification', 'Missle', 'Crew', 'Ilicit', 'Title'], 'While you defend or perform an attack, if the enemy ship is in your forward arc, you my spend 1 force to change 1 of your blank results to an evade or hit result.')
                                                ,'Scavenged YT-1300', ['Resistance'], '', [5, 3, 1, 8, 3, '0', '2^'], ['Focus', 'Target Lock', 'Red Boost', 'Red Rotate']),
            # T-70 X-Wing Pilots
            Ship(Pilot('Poe Dameron [HoH]', 60, ['Talent', 'Tech', 'Configuration', 'Hardpoint', 'Astromech', 'Modification', 'Title'], 'After a friendly ship at range 0-2 performs an action during its activation, you may spend 2 charge. If you do, that ship may perform a white action, treating it as red.')
                                                ,'T-70 X-Wing', ['Resistance'], 'Weapon Hardpoint: You can equip 1 cannon, torpedo, or missle upgrade', [6, 3, 2, 4, 3, '2^', '0'], ['Focus', 'Target Lock', 'Boost']),
            Ship(Pilot('Poe Dameron', 62, ['Talent', 'Tech', 'Configuration', 'Hardpoint', 'Astromech', 'Modification', 'Title'], 'After you perform an action, you may spend 1 charge to perform a white action, treating it as red')
                                                ,'T-70 X-Wing', ['Resistance'], 'Weapon Hardpoint: You can equip 1 cannon, torpedo, or missle upgrade', [6, 3, 2, 4, 3, '1^', '0'], ['Focus', 'Target Lock', 'Boost']),
            Ship(Pilot('Nien Nunb', 55, ['Talent', 'Tech', 'Configuration', 'Hardpoint', 'Astromech', 'Modification', 'Title'], 'After you gain a stress token, if there is an enemy ship in your forward arc at range 0-1, you may remove that stress token.')
                                                ,'T-70 X-Wing', ['Resistance'], 'Weapon Hardpoint: You can equip 1 cannon, torpedo, or missle upgrade', [6, 3, 2, 4, 3, '0', '0'], ['Focus', 'Target Lock', 'Boost'])
        ]

    ### Function to return a list containing either Pilot or Upgrade objects that meet the search requirements
      # (cType refers to Card Type)
      # (cType = 0 means the function should return a list containing Ship objects)
      # (cType = 1 means the function should return a list containing Upgrade objects)
    def getOptions(self, cType=0, name='None', sType='None', uType='None', tag='None'):
        options = []

        # cType == 0 indicates that the returned list of options should contain entries of type Ship
        if cType == 0:
            for s in self.ships:
                # If the search finds a Ship with the same 'name' as the one searched for, adds Ship to return options (the returned list of options)
                if s.pilot.name == name: 
                    options.append(s)
                # If the search finds an Ship with the same 'utype' as the one searched for, adds Ship to return options (the returned list of options)
                if s.sType == sType:
                    options.append(s)
                # If the search finds an Ship with one of the tags the same as the one searched for, Ship to return options (the returned list of options)
                for t in s.tags:
                    if t == tag:
                        options.append(s)

        # cType == 1 indicates that the returned list of options should contain entries of type Upgrade
        elif cType == 1:
            for u in self.upgrades:
                # If the search finds an Upgrade with the same 'name' as the one searched for, adds Upgrade to return options (the returned list of options)
                if u.name == name: 
                    options.append(u)
                # If the search finds an Upgrade with the same 'utype' as the one searched for, adds Upgrade to return options (the returned list of options)
                if u.uType == uType:
                    options.append(u)
                # If the search finds an Upgrade with one of the tags the same as the one searched for, adds Upgrade to return options (the returned list of options)
                for t in u.tags:
                    if t == tag:
                        options.append(u)

        return options

    ### Function to create and return a list of Pilot names based on Ship type
    def getPilotNamesAndPoints(self, sType):
        PILOTS = []
        info = self.getOptions(0, sType=sType)
        for ship in info:
            PILOTS.append(ship.pilot.name + ' [' + str(ship.pilot.points) + ']')
        return PILOTS


# TEST CODE for getOptions()
#x = Collection()
#print(x.getPilotNames('ARC-170 Starfighter'))