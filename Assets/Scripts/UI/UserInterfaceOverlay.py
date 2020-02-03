"""

This script handles the UI overlay and things like: 
Displaying Player Health, current armour, current weapons, and NPC Dialogue

Below is copied from the ExampleGame

"""

import LeagueEngine
import pygame

class Overlay(LeagueEngine.DUGameObject):
    def __init__(self, player):
        super().__init__(self)
        self._layer = 1000
        self.player = player
        self.font = pygame.font.Font('./ExampleGame/assets//fonts/font2.ttf',32)
        self.image = pygame.Surface([800, 32], pygame.SRCALPHA)
        self.image.fill((127, 127, 127, 127))
        self.text = self.font.render("Health: " + str(self.player.health), True, (0,0,0))
        self.image.blit(self.text, (0, -5))
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.static = True

    def update(self, deltaTime):
        self.image.fill((127, 127, 127, 127))
        self.text = self.font.render("Health: " + str(self.player.health), True, (0,0,0))
        self.image.blit(self.text, (0, -5))