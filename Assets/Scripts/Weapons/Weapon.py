"""

This script will be inherited by each type of weapon
(Melee and Ranged), and hold the basic information
that is relevant to any kind of weapon

"""

import pygame
from LeagueEngine import *

class Weapon(DUGameObject):
    def __init__(self):
        self.damage = 1
        self.attackSpeed = 2