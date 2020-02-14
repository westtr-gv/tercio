"""

This script should handle all the references
from one player script to another, as well
as any miscellaneous connections and actions

This starting script is copied from the ExampleGame

"""

import pygame
from LeagueEngine import *


class Player(Character):
    """This is a sample class for a player object.  A player
    is a character, is a drawable, and an updateable object.
    This class should handle everything a player does, such as
    moving, throwing/shooting, collisions, etc.  It was hastily
    written as a demo but should direction.
    """

    def __init__(self, layer=0, x=0, y=0, world_size=(0, 0)):
        super().__init__(layer, x, y)
        # This unit's health
        self.health = 100
        # Last time I was hit
        self.last_hit = pygame.time.get_ticks()
        # A unit-less value.  Bigger is faster.
        self.delta = 420
        # Where the player is positioned
        self.x = x
        self.y = y
        # The image to use.  This will change frequently
        # in an animated Player class.
        self.images = {
            "N": {
                1: pygame.image.load('./Assets/Sprites/Player/walking/N_1.png').convert_alpha(),
                2: pygame.image.load('./Assets/Sprites/Player/walking/N_2.png').convert_alpha(),
                3: pygame.image.load('./Assets/Sprites/Player/walking/N_3.png').convert_alpha(),
                4: pygame.image.load('./Assets/Sprites/Player/walking/N_4.png').convert_alpha(),
                5: pygame.image.load('./Assets/Sprites/Player/walking/N_5.png').convert_alpha(),
                6: pygame.image.load('./Assets/Sprites/Player/walking/N_6.png').convert_alpha(),
                7: pygame.image.load('./Assets/Sprites/Player/walking/N_7.png').convert_alpha(),
                8: pygame.image.load('./Assets/Sprites/Player/walking/N_8.png').convert_alpha(),
                9: pygame.image.load('./Assets/Sprites/Player/walking/N_9.png').convert_alpha(),
            },
            "E": {
                1: pygame.image.load('./Assets/Sprites/Player/walking/E_1.png').convert_alpha(),
                2: pygame.image.load('./Assets/Sprites/Player/walking/E_2.png').convert_alpha(),
                3: pygame.image.load('./Assets/Sprites/Player/walking/E_3.png').convert_alpha(),
                4: pygame.image.load('./Assets/Sprites/Player/walking/E_4.png').convert_alpha(),
                5: pygame.image.load('./Assets/Sprites/Player/walking/E_5.png').convert_alpha(),
                6: pygame.image.load('./Assets/Sprites/Player/walking/E_6.png').convert_alpha(),
                7: pygame.image.load('./Assets/Sprites/Player/walking/E_7.png').convert_alpha(),
                8: pygame.image.load('./Assets/Sprites/Player/walking/E_8.png').convert_alpha(),
                9: pygame.image.load('./Assets/Sprites/Player/walking/E_9.png').convert_alpha(),
            },
            "S": {
                1: pygame.image.load('./Assets/Sprites/Player/walking/S_1.png').convert_alpha(),
                2: pygame.image.load('./Assets/Sprites/Player/walking/S_2.png').convert_alpha(),
                3: pygame.image.load('./Assets/Sprites/Player/walking/S_3.png').convert_alpha(),
                4: pygame.image.load('./Assets/Sprites/Player/walking/S_4.png').convert_alpha(),
                5: pygame.image.load('./Assets/Sprites/Player/walking/S_5.png').convert_alpha(),
                6: pygame.image.load('./Assets/Sprites/Player/walking/S_6.png').convert_alpha(),
                7: pygame.image.load('./Assets/Sprites/Player/walking/S_7.png').convert_alpha(),
                8: pygame.image.load('./Assets/Sprites/Player/walking/S_8.png').convert_alpha(),
                9: pygame.image.load('./Assets/Sprites/Player/walking/S_9.png').convert_alpha(),
            },
            "W": {
                1: pygame.image.load('./Assets/Sprites/Player/walking/W_1.png').convert_alpha(),
                2: pygame.image.load('./Assets/Sprites/Player/walking/W_2.png').convert_alpha(),
                3: pygame.image.load('./Assets/Sprites/Player/walking/W_3.png').convert_alpha(),
                4: pygame.image.load('./Assets/Sprites/Player/walking/W_4.png').convert_alpha(),
                5: pygame.image.load('./Assets/Sprites/Player/walking/W_5.png').convert_alpha(),
                6: pygame.image.load('./Assets/Sprites/Player/walking/W_6.png').convert_alpha(),
                7: pygame.image.load('./Assets/Sprites/Player/walking/W_7.png').convert_alpha(),
                8: pygame.image.load('./Assets/Sprites/Player/walking/W_8.png').convert_alpha(),
                9: pygame.image.load('./Assets/Sprites/Player/walking/W_9.png').convert_alpha(),
            },
            "NE": {
                1: pygame.image.load('./Assets/Sprites/Player/walking/N_1.png').convert_alpha(),
                2: pygame.image.load('./Assets/Sprites/Player/walking/N_2.png').convert_alpha(),
                3: pygame.image.load('./Assets/Sprites/Player/walking/N_3.png').convert_alpha(),
                4: pygame.image.load('./Assets/Sprites/Player/walking/N_4.png').convert_alpha(),
                5: pygame.image.load('./Assets/Sprites/Player/walking/N_5.png').convert_alpha(),
                6: pygame.image.load('./Assets/Sprites/Player/walking/N_6.png').convert_alpha(),
                7: pygame.image.load('./Assets/Sprites/Player/walking/N_7.png').convert_alpha(),
                8: pygame.image.load('./Assets/Sprites/Player/walking/N_8.png').convert_alpha(),
                9: pygame.image.load('./Assets/Sprites/Player/walking/N_9.png').convert_alpha(),
            },
            "NW": {
                1: pygame.image.load('./Assets/Sprites/Player/walking/N_1.png').convert_alpha(),
                2: pygame.image.load('./Assets/Sprites/Player/walking/N_2.png').convert_alpha(),
                3: pygame.image.load('./Assets/Sprites/Player/walking/N_3.png').convert_alpha(),
                4: pygame.image.load('./Assets/Sprites/Player/walking/N_4.png').convert_alpha(),
                5: pygame.image.load('./Assets/Sprites/Player/walking/N_5.png').convert_alpha(),
                6: pygame.image.load('./Assets/Sprites/Player/walking/N_6.png').convert_alpha(),
                7: pygame.image.load('./Assets/Sprites/Player/walking/N_7.png').convert_alpha(),
                8: pygame.image.load('./Assets/Sprites/Player/walking/N_8.png').convert_alpha(),
                9: pygame.image.load('./Assets/Sprites/Player/walking/N_9.png').convert_alpha(),
            },
            "SE": {
                1: pygame.image.load('./Assets/Sprites/Player/walking/S_1.png').convert_alpha(),
                2: pygame.image.load('./Assets/Sprites/Player/walking/S_2.png').convert_alpha(),
                3: pygame.image.load('./Assets/Sprites/Player/walking/S_3.png').convert_alpha(),
                4: pygame.image.load('./Assets/Sprites/Player/walking/S_4.png').convert_alpha(),
                5: pygame.image.load('./Assets/Sprites/Player/walking/S_5.png').convert_alpha(),
                6: pygame.image.load('./Assets/Sprites/Player/walking/S_6.png').convert_alpha(),
                7: pygame.image.load('./Assets/Sprites/Player/walking/S_7.png').convert_alpha(),
                8: pygame.image.load('./Assets/Sprites/Player/walking/S_8.png').convert_alpha(),
                9: pygame.image.load('./Assets/Sprites/Player/walking/S_9.png').convert_alpha(),
            },
            "SW": {
                1: pygame.image.load('./Assets/Sprites/Player/walking/S_1.png').convert_alpha(),
                2: pygame.image.load('./Assets/Sprites/Player/walking/S_2.png').convert_alpha(),
                3: pygame.image.load('./Assets/Sprites/Player/walking/S_3.png').convert_alpha(),
                4: pygame.image.load('./Assets/Sprites/Player/walking/S_4.png').convert_alpha(),
                5: pygame.image.load('./Assets/Sprites/Player/walking/S_5.png').convert_alpha(),
                6: pygame.image.load('./Assets/Sprites/Player/walking/S_6.png').convert_alpha(),
                7: pygame.image.load('./Assets/Sprites/Player/walking/S_7.png').convert_alpha(),
                8: pygame.image.load('./Assets/Sprites/Player/walking/S_8.png').convert_alpha(),
                9: pygame.image.load('./Assets/Sprites/Player/walking/S_9.png').convert_alpha(),
            },
        }

        # pygame.transform.flip(self.image, True, False)

        self.image = self.images["N"][1]

        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        # How big the world is, so we can check for boundries
        self.world_size = world_size
        # What sprites am I not allowd to cross?
        self.blocks = pygame.sprite.Group()
        # Which collision detection function?
        self.collide_function = pygame.sprite.collide_circle
        self.collisions = []
        # For collision detection, we need to compare our sprite
        # with collideable sprites.  However, we have to remap
        # the collideable sprites coordinates since they change.
        # For performance reasons I created this sprite so we
        # don't have to create more memory each iteration of
        # collision detection.
        self.collider = Drawable(20)
        self.collider.image = pygame.Surface([Settings.tile_size, Settings.tile_size], pygame.SRCALPHA)
        self.collider.image.fill((127, 127, 127, 127))
        self.collider.rect = self.collider.image.get_rect()
        # Overlay
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.overlay = self.font.render(str(self.health) + "        4 lives", True, (0, 0, 0))

    def move_left(self, time):
        amount = self.delta * time
        try:
            if self.x - amount < 0:
                raise OffScreenLeftException
            else:
                self.x = self.x - amount
                self.update(0)
                while(len(self.collisions) != 0):
                    self.x = self.x + amount
                    self.update(0)
        except:
            pass

    def move_right(self, time):
        self.collisions = []
        amount = self.delta * time
        try:
            if self.x + amount > self.world_size[0] - Settings.tile_size:
                raise OffScreenRightException
            else:
                self.x = self.x + amount
                self.update(0)
                while(len(self.collisions) != 0):
                    self.x = self.x - amount
                    self.update(0)
        except:
            pass

    def move_up(self, time):
        self.collisions = []
        amount = self.delta * time
        try:
            if self.y - amount < 0:
                raise OffScreenTopException
            else:
                self.y = self.y - amount
                self.update(0)
                if len(self.collisions) != 0:
                    self.y = self.y + amount
                    self.update(0)
                    self.collisions = []
        except:
            pass

    def move_down(self, time):
        amount = self.delta * time
        try:
            if self.y + amount > self.world_size[1] - Settings.tile_size:
                raise OffScreenBottomException
            else:
                self.y = self.y + amount
                self.update(0)
                if len(self.collisions) != 0:
                    self.y = self.y - amount
                    self.update(0)
                    self.collisions = []
        except:
            pass

    def update(self, time):
        self.dirty = 1
        self.rect.x = self.x
        self.rect.y = self.y
        self.collisions = []
        self.checkCollisions()

    def checkCollisions(self):
        for sprite in self.blocks:
            self.collider.rect.x = sprite.x
            self.collider.rect.y = sprite.y
            if pygame.sprite.collide_rect(self, self.collider):
                self.collisions.append(sprite)
        # print("Collider Rect: (", self.collider.rect.x, ", ",self.collider.rect.y, ")")
        # print(len(self.collisions))
        # This is for debugging our collider
        # self.image.blit(self.collider.image, (0,0), (0,0, Settings.tile_size * 2, Settings.tile_size * 2))

    def ouch(self):
        now = pygame.time.get_ticks()
        if now - self.last_hit > 1000:
            self.health = self.health - 10
            self.last_hit = now
