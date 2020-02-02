import sys
sys.path.append("..")
import pygame
import LeagueEngine
from Assets.Scripts.Weapons.Ranged import *


class Bow(Ranged):
    def __init__(self):
        self.damage = 1
