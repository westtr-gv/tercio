"""

This script will handle any base functionality that isn't
unique to the an individual player. Things like rendering
objects to the screen, handling scoreboard, alive/dead
players, etc.

Below is copied from the ExampleGame

"""

import sys
# sys.path.append("../..")  # This line is necessary if you are simply running GameManager.py, and all of the 

import pygame
import LeagueEngine
from Assets.Scripts.Player.PlayerManager import *
from Assets.Scripts.UI.UserInterfaceOverlay import *

"""This file is garbage. It was a hastily coded mockup
to demonstrate how to use the engine.  We will be creating
a Game class that organizes this codegame better (and is
reusable).
"""

# Function to call when colliding with zombie


def main():
    engine = LeagueEngine.Engine("Tercio", './Assets/Sprites/Branding/icon.png')
    engine.init_pygame()

    sprites = LeagueEngine.Spritesheet("./ExampleGame/assets/base_chip_pipo.png", LeagueEngine.Settings.tile_size, 8)
    terrainFoliage = LeagueEngine.Tilemap("./ExampleGame/assets/world.lvl", sprites, layer=1)
    terrainBackground = LeagueEngine.Tilemap("./ExampleGame/assets/background.lvl", sprites, layer=0)
    worldSize = (terrainFoliage.wide * LeagueEngine.Settings.tile_size, terrainFoliage.high * LeagueEngine.Settings.tile_size,)
    engine.drawables.add(terrainFoliage.passable.sprites())
    engine.drawables.add(terrainBackground.passable.sprites())
    ourPlayer = Player(2, 400, 300)
    ourOverlay = Overlay(ourPlayer)
    ourPlayer.blocks.add(terrainFoliage.impassable)
    ourPlayer.world_size = worldSize
    ourPlayer.rect = ourPlayer.image.get_rect()
    ourEnemy = Player(10, 100, 100)
    ourEnemy.image = ourPlayer.image
    engine.objects.append(ourPlayer)
    engine.objects.append(ourEnemy)
    engine.drawables.add(ourPlayer)
    engine.drawables.add(ourEnemy)
    engine.drawables.add(ourOverlay)
    mainCamera = LeagueEngine.LessDumbCamera(800, 600, ourPlayer, engine.drawables, worldSize)
    # c = LeagueEngine.DumbCamera(800, 600, p, e.drawables, world_size)

    engine.objects.append(mainCamera)
    engine.objects.append(ourOverlay)

    engine.collisions[ourPlayer] = (ourEnemy, ourPlayer.ouch)
    pygame.time.set_timer(pygame.USEREVENT + 1, 1000 // LeagueEngine.Settings.gameTimeFactor)

    # engine.key_events[pygame.K_a] = ourPlayer.move_left
    # engine.key_events[pygame.K_d] = ourPlayer.move_right
    # engine.key_events[pygame.K_w] = ourPlayer.move_up
    # engine.key_events[pygame.K_s] = ourPlayer.move_down

    engine.player = ourPlayer

    engine.events[pygame.USEREVENT + 1] = ourEnemy.move_right
    engine.events[pygame.QUIT] = engine.stop
    engine.run()


if __name__ == "__main__":
    main()
