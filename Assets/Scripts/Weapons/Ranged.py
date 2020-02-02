"""

This script implements the Weapon class, and will
have unique default values, and new variables for
ranged weapons

"""

import pygame
import LeagueEngine
from Assets.Scripts.Weapons.Weapon import *

class Ranged(Weapon):
    def __init__(self):
        self.damage = 1
        self.attackSpeed = 2