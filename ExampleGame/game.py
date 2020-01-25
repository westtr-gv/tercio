#!/usr/bin/env python3

import sys
sys.path.append("..")  # This line must be above 'import LeagueEngine'
import pygame
import LeagueEngine
from player import Player
from overlay import Overlay

"""This file is garbage. It was a hastily coded mockup
to demonstrate how to use the engine.  We will be creating
a Game class that organizes this code better (and is
reusable).
"""


# Function to call when colliding with zombie

def main():
    engine = LeagueEngine.Engine("Tercio")
    engine.init_pygame()

    sprites = LeagueEngine.Spritesheet("./assets/base_chip_pipo2.png", LeagueEngine.Settings.tile_size, 8)
    terrainFoliage = LeagueEngine.Tilemap("./assets/world.lvl", sprites, layer=1)
    terrainBackground = LeagueEngine.Tilemap("./assets/background.lvl", sprites, layer=0)
    world_size = (terrainFoliage.wide * LeagueEngine.Settings.tile_size, terrainFoliage.high * LeagueEngine.Settings.tile_size,)
    engine.drawables.add(terrainFoliage.passable.sprites())
    engine.drawables.add(terrainBackground.passable.sprites())
    ourPlayer = Player(2, 400, 300)
    o = Overlay(ourPlayer)
    ourPlayer.blocks.add(terrainFoliage.impassable)
    ourPlayer.world_size = world_size
    ourPlayer.rect = ourPlayer.image.get_rect()
    q = Player(10, 100, 100)
    q.image = ourPlayer.image
    engine.objects.append(ourPlayer)
    engine.objects.append(q)
    engine.drawables.add(ourPlayer)
    engine.drawables.add(q)
    engine.drawables.add(o)
    c = LeagueEngine.LessDumbCamera(800, 600, ourPlayer, engine.drawables, world_size)
    # c = LeagueEngine.DumbCamera(800, 600, p, e.drawables, world_size)

    engine.objects.append(c)
    engine.objects.append(o)

    engine.collisions[ourPlayer] = (q, ourPlayer.ouch)
    pygame.time.set_timer(pygame.USEREVENT + 1, 1000 // LeagueEngine.Settings.gameTimeFactor)
    engine.key_events[pygame.K_a] = ourPlayer.move_left
    engine.key_events[pygame.K_d] = ourPlayer.move_right
    engine.key_events[pygame.K_w] = ourPlayer.move_up
    engine.key_events[pygame.K_s] = ourPlayer.move_down
    engine.events[pygame.USEREVENT + 1] = q.move_right
    engine.events[pygame.QUIT] = engine.stop
    engine.run()


if __name__ == "__main__":
    main()
