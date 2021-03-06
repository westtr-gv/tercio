from .settings import *
from .engine import *
from .game_objects import *

import csv
import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class Camera(UGameObject):
    def __init__(self, width, height, center_on, drawables, world_size):
        self.width = width
        self.height = height
        self.center_on = center_on
        self.drawables = drawables
        self.x = self.center_on.x
        self.y = self.center_on.y
        self.world_size = world_size

        # self.topLeft_x = (self.center_on.x - (self.width // 2))         # topLeft_x is the top left corner of the rendered screen
        # self.topLeft_y = (self.center_on.y - (self.height // 2))        # topLeft_y is the top left corner of the rendered screen
        # self.bottomRight_x = (self.center_on.x + (self.width // 2))     # bottomRight_x is the bottom right corner of the rendered screen
        # self.bottomRight_y = (self.center_on.y + (self.height // 2))    # bottomRight_y is the bottom right corner of the rendered screen

    def update(self, deltaTime):
        pass


class DumbCamera(Camera):
    def update(self, time):
        pass
        # self.x = self.center_on.x
        # self.y = self.center_on.y
        # offset_x = - (self.x - (self.width // 2))
        # offset_y = - (self.y - (self.height // 2))

        # for d in self.drawables:
        #     d.rect.x = d.x + offset_x
        #     d.rect.y = d.y + offset_y
        #     d.dirty = 1


class LessDumbCamera(Camera):
    def update(self, time):
        # self.dirty = 1
        if self.center_on.x - self.width // 2 > 0 and self.center_on.x + self.width // 2 < self.world_size[0] - Settings.tile_size:
            self.x = self.center_on.x
        if self.center_on.y - self.height // 2 > 0 and self.center_on.y + self.height // 2 < self.world_size[1] - Settings.tile_size:
            self.y = self.center_on.y
        self.offset_x = - (self.x - (self.width // 2))
        self.offset_y = - (self.y - (self.height // 2))
        self.topLeft_x = (self.x - (self.width // 2))      # topLeft_x is the top left corner of the rendered screen
        self.topLeft_y = (self.y - (self.height // 2))     # topLeft_y is the top left corner of the rendered screen
        self.bottomRight_x = (self.x + (self.width // 2))    # bottomRight_x is the bottom right corner of the rendered screen
        self.bottomRight_y = (self.y + (self.height // 2))   # bottomRight_y is the bottom right corner of the rendered screen
        # print("Top Left: (", self.topLeft_x, ", ", self.topLeft_y, ")")
        # print("Bottom Right: (", self.bottomRight_x, ", ", self.bottomRight_y, ")")

        # print(len(self.drawables))

        self.LoopThroughDrawables()

            # self.determineVisible(d)

            # # Remove sprites that are no longer visible
            # if (not d.isRendered and d in self.renderedDrawables):
            #     self.renderedDrawables.remove(d)
            # # Add sprites that are now visible
            # if (d.isRendered and d not in self.renderedDrawables):
            #     self.renderedDrawables.add(d)

            # # Remove sprites that are no longer visible
            # if (not d.isRendered):
            #     self.renderedDrawables.remove(d)
            # # Add sprites that are now visible
            # if (d.isRendered):
            #     self.renderedDrawables.add(d)

        # print("Rendered Drawables On-screen: ", len(self.renderedDrawables))
        # print("Drawables On-screen: ", len(self.drawables))
        # print("Should be at minimum: ", (Settings.width // Settings.tile_size) * (Settings.height // Settings.tile_size))

    def LoopThroughDrawables(self):
        for d in self.drawables:
            if ((d.x >= self.topLeft_x - 64 and d.y >= self.topLeft_y - 64) and (d.x <= self.bottomRight_x + 64 and d.y <= self.bottomRight_y + 64)):
                if(d.visible):
                # if ((d.x >= self.topLeft_x - 64 and d.y >= self.topLeft_y - 64) and (d.x <= self.bottomRight_x + 64 and d.y <= self.bottomRight_y + 64)):
                    if hasattr(d, 'static'):
                        continue

                    d.dirty = 1
                    d.rect.x = d.x + self.offset_x
                    d.rect.y = d.y + self.offset_y
                    # print("This bitch visible: (", d.x, ", ", d.y, ")")

    def determineVisible(self, drawable):
        # Check if the drawable we are scanning is within the camera view
        if ((drawable.x >= self.topLeft_x - 64 and drawable.y >= self.topLeft_y - 64) and (drawable.x <= self.bottomRight_x + 64 and drawable.y <= self.bottomRight_y + 64)):
            drawable.visible = True
        # If this drawable is not within view of our camera, flag it as not rendered
        else:
            drawable.visible = False

class Tilemap:
    """An object that represents an MxN list of tiles.  Give x, y
    returns various pieces of information about that tile, such as
    the image to draw, etc.

    Fields:
    path - A path to the file that holds the tilemap data.  Structure described below.
    path2 - A path to the file that holds our collidable objects reference numbers
    spritesheet - The spritesheet from which to get the images for the tiles.
    tile_size - The number of pixels wide and high (we are forcing squares) per tile.
    wide - The number of tiles wide the map holds.
    high - The number of tiles vertically the map holds.
    world - The MxN list of tile numbers.
    sprites - The sprites for drawing the world.

    File structure:
    A tilemap file begins with the width (an integer) of the map (in tiles, not pixels), a newline,
    the height (an integer; again in tiles, not pixels), a newline, followed by a comma-separated
    list of lists of integers that represent the sprite number from the spritesheet.  For instance,

    5
    7
    1, 1, 1, 1, 2, 1, 1
    1, 1, 1, 1, 2, 1, 1
    1, 1, 1, 2, 1, 2, 1
    1, 1, 1, 2, 1, 2, 2
    2, 2, 2, 2, 1, 2, 2
    """

    def __init__(self, path, path2, width, height, spritesheet, tile_size=Settings.tile_size, layer=0):
        self.path = path
        self.path2 = path2
        self.wide = width
        self.high = height
        self.collidables = []
        self.spritesheet = spritesheet
        self.tile_size = tile_size
        self.layer = layer
        self.world = []
        self.passable = pygame.sprite.Group()
        self.impassable = pygame.sprite.Group()
        self.__parse()

    def __parse(self):
        """This function begins the process of (attempting) to
        parse a level file.  The structure of the file is described above.
        """
        with open(self.path, 'r') as f:
            reader = csv.reader(f)
            contents = list(reader)
        # How many tiles wide is our world?
        # self.wide = int(contents[0][0])
        # And how tall?
        # self.high = int(contents[1][0])

        # Record which objects are collidables
        with open(self.path2, 'r') as f2:
            reader2 = csv.reader(f2)
            contents2 = list(reader2)
        self.collidables = list(map(int, contents2[0]))

        # Sprite numbers for all tiles are in the
        # multidimensional list "world".
        self.world = contents[0:]
        a = 0
        for i in self.world:
            b = 0
            for j in i:
                x = b * self.spritesheet.tile_size
                y = a * self.spritesheet.tile_size
                num = int(j)
                if(num != -1):
                    base_sprite = self.spritesheet.sprites[abs(num)]
                    sprite = Drawable(self.layer)
                    sprite.image = base_sprite.image
                    # Set rectangle coords (using top-left coords here)
                    rect = sprite.image.get_rect()
                    rect.x = x
                    rect.y = y
                    sprite.x = x
                    sprite.y = y
                    sprite.rect = rect
                    self.passable.add(sprite)
                    # if num < 0:
                    if num in self.collidables:
                        self.impassable.add(sprite)
                b = b + 1
            a = a + 1


class Spritesheet:
    """An object that represents a spritesheet and provides
    methods to access individual sprites from it.

    There are better ways to create spritesheets.  This code does
    not allow for packed sprites for instance.  Instead, it forces
    sprites to be in nice, tiled squares.

    Fields:
    path - The path to the spritesheet file.
    tile_size - The number of pixels wide and high the sprites are.  We are forcing square tiles for this engine.
    per_row - The number of sprites per row on the spritesheet.
    width - Number of pixels wide of the spritesheet image.
    height - Number of pixels high of the spritesheet image.
    sprites - A single-dimensional list of the sprites from the sheet.
    """

    def __init__(self, path, tile_size, per_row):
        self.path = path
        self.sheet = pygame.image.load(self.path).convert_alpha()
        self.tile_size = tile_size
        self.per_row = per_row
        self.width, self.height = self.sheet.get_size()
        self.sprites = self.__split_up()

    def __split_up(self):
        # This function splits the sheet up into equal-sized chunks,
        # and returns a list of the chunks.
        sprites = []
        for i in range((self.width * self.height) // (Settings.tile_size * Settings.tile_size)):
            image = self.__get_image_num(i)
            sprites.append(image)
        return sprites

    def __get_image_num(self, num):
        # This function copies an MxM image from x, y
        # to a new Sprite and returns it.
        y = self.tile_size * (num // self.per_row)
        x = self.tile_size * (num % self.per_row)
        sprite = Drawable()
        sprite.image = pygame.Surface((self.tile_size, self.tile_size), pygame.SRCALPHA).convert_alpha()
        sprite.image.blit(self.sheet, (0, 0), (x, y, x + self.tile_size, y + self.tile_size))
        return sprite

class CustomLayeredUpdates(pygame.sprite.LayeredUpdates):
    def __init__(self):
        super().__init__()
    
    def draw(self, surface):
        for layer in self.layers():
            for sprite in self.get_sprites_from_layer(layer):
                if(sprite.visible and sprite.dirty > 0):
                    sprite.draw(surface)