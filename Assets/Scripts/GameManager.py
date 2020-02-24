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

    world = "./Assets/World/Map1"
    sprites = "./Assets/Sprites"
    scripts = "./Assets/Scripts"


#  ███████╗██████╗ ██████╗ ██╗████████╗███████╗███████╗██╗  ██╗███████╗███████╗████████╗
#  ██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝██╔════╝██╔════╝██║  ██║██╔════╝██╔════╝╚══██╔══╝
#  ███████╗██████╔╝██████╔╝██║   ██║   █████╗  ███████╗███████║█████╗  █████╗     ██║
#  ╚════██║██╔═══╝ ██╔══██╗██║   ██║   ██╔══╝  ╚════██║██╔══██║██╔══╝  ██╔══╝     ██║
#  ███████║██║     ██║  ██║██║   ██║   ███████╗███████║██║  ██║███████╗███████╗   ██║
#  ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝
#

    # sprites = LeagueEngine.Spritesheet("./ExampleGame/assets/base_chip_pipo.png", LeagueEngine.Settings.tile_size, 8)

    sprites = LeagueEngine.Spritesheet((world + "/Spritesheet.png"), LeagueEngine.Settings.tile_size, 97)


#  ████████╗██╗██╗     ███████╗███╗   ███╗ █████╗ ██████╗
#  ╚══██╔══╝██║██║     ██╔════╝████╗ ████║██╔══██╗██╔══██╗
#     ██║   ██║██║     █████╗  ██╔████╔██║███████║██████╔╝
#     ██║   ██║██║     ██╔══╝  ██║╚██╔╝██║██╔══██║██╔═══╝
#     ██║   ██║███████╗███████╗██║ ╚═╝ ██║██║  ██║██║
#     ╚═╝   ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝
#

    # terrainFoliage = LeagueEngine.Tilemap("./ExampleGame/assets/world.lvl", sprites, layer=1)
    # terrainBackground = LeagueEngine.Tilemap("./ExampleGame/assets/background.lvl", sprites, layer=0)

    lootChestTilemap = LeagueEngine.Tilemap((world + "/CSV/Map1_Loot Chests.csv"), (world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=14)
    objectsForeground = LeagueEngine.Tilemap((world + "/CSV/Map1_Objects_Objects Foreground.csv"), (world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=13)
    desertForeground = LeagueEngine.Tilemap((world + "/CSV/Map1_Desert_Desert Foreground.csv"), (world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=12)
    graveyardForeground = LeagueEngine.Tilemap((world + "/CSV/Map1_Graveyard_Graveyard Foreground.csv"), (world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=11)
    largeFoliageForeground = LeagueEngine.Tilemap((world + "/CSV/Map1_Foliage_Large Foliage Foreground.csv"), (world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=10)
    mediumFoliageForeground = LeagueEngine.Tilemap((world + "/CSV/Map1_Foliage_Medium Foliage Foreground.csv"), (world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=9)

    objectsBackground = LeagueEngine.Tilemap((world + "/CSV/Map1_Objects_Objects Background.csv"),(world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=7)
    desertBackground = LeagueEngine.Tilemap((world + "/CSV/Map1_Desert_Desert Background.csv"),(world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=6)
    graveyardBackground = LeagueEngine.Tilemap((world + "/CSV/Map1_Graveyard_Graveyard Background.csv"),(world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=5)
    largeFoliageBackground = LeagueEngine.Tilemap((world + "/CSV/Map1_Foliage_Large Foliage Background.csv"), (world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=4)
    mediumFoliageBackground = LeagueEngine.Tilemap((world + "/CSV/Map1_Foliage_Medium Foliage Background.csv"), (world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=3)
    smallFoliageBackground = LeagueEngine.Tilemap((world + "/CSV/Map1_Foliage_Small Foliage Background.csv"), (world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=2)
    terrainForeground = LeagueEngine.Tilemap((world + "/CSV/Map1_Terrain_Terrain Foreground.csv"),(world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=1)
    terrainBackground = LeagueEngine.Tilemap((world + "/CSV/Map1_Terrain_Terrain Background.csv"),(world + "/CSV/Collidables.csv"), 128, 128, sprites, layer=0)


#  ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗     ███████╗██╗███████╗███████╗
#  ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗    ██╔════╝██║╚══███╔╝██╔════╝
#  ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║    ███████╗██║  ███╔╝ █████╗
#  ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║    ╚════██║██║ ███╔╝  ██╔══╝
#  ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝    ███████║██║███████╗███████╗
#   ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝     ╚══════╝╚═╝╚══════╝╚══════╝
#

    # worldSize = (terrainFoliage.wide * LeagueEngine.Settings.tile_size, terrainFoliage.high * LeagueEngine.Settings.tile_size,)

    worldSize = (terrainBackground.wide * LeagueEngine.Settings.tile_size, terrainBackground.high * LeagueEngine.Settings.tile_size,)


#  ██████╗ ██████╗  █████╗ ██╗    ██╗ █████╗ ██████╗ ██╗     ███████╗███████╗
#  ██╔══██╗██╔══██╗██╔══██╗██║    ██║██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝
#  ██║  ██║██████╔╝███████║██║ █╗ ██║███████║██████╔╝██║     █████╗  ███████╗
#  ██║  ██║██╔══██╗██╔══██║██║███╗██║██╔══██║██╔══██╗██║     ██╔══╝  ╚════██║
#  ██████╔╝██║  ██║██║  ██║╚███╔███╔╝██║  ██║██████╔╝███████╗███████╗███████║
#  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝
#

    # engine.drawables.add(terrainFoliage.passable.sprites())
    # engine.drawables.add(terrainBackground.passable.sprites())

    engine.drawables.add(lootChestTilemap.passable.sprites())
    engine.drawables.add(desertForeground.passable.sprites())
    engine.drawables.add(graveyardForeground.passable.sprites())
    engine.drawables.add(largeFoliageForeground.passable.sprites())
    engine.drawables.add(mediumFoliageForeground.passable.sprites())
    engine.drawables.add(objectsForeground.passable.sprites())
    engine.drawables.add(terrainForeground.passable.sprites())

    engine.drawables.add(desertBackground.passable.sprites())
    engine.drawables.add(graveyardBackground.passable.sprites())
    engine.drawables.add(largeFoliageBackground.passable.sprites())
    engine.drawables.add(mediumFoliageBackground.passable.sprites())
    engine.drawables.add(objectsBackground.passable.sprites())
    engine.drawables.add(smallFoliageBackground.passable.sprites())
    engine.drawables.add(terrainBackground.passable.sprites())


#  ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗
#  ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
#  ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝
#  ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
#  ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║
#  ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
#

    ourPlayer = Player(8, engine.viewportWidth // 2-50, engine.viewportHeight // 2-50)
    # ourPlayer = Player(8, 1000, 1000)
    # engine.drawables.add(ourPlayer.collider)

    ourPlayer.blocks.add(lootChestTilemap.impassable)
    ourPlayer.blocks.add(desertForeground.impassable)
    ourPlayer.blocks.add(graveyardForeground.impassable)
    ourPlayer.blocks.add(largeFoliageForeground.impassable)
    ourPlayer.blocks.add(mediumFoliageForeground.impassable)
    ourPlayer.blocks.add(objectsForeground.impassable)
    ourPlayer.blocks.add(terrainForeground.impassable)

    ourPlayer.blocks.add(desertBackground.impassable)
    ourPlayer.blocks.add(graveyardBackground.impassable)
    ourPlayer.blocks.add(largeFoliageBackground.impassable)
    ourPlayer.blocks.add(mediumFoliageBackground.impassable)
    ourPlayer.blocks.add(objectsBackground.impassable)
    ourPlayer.blocks.add(smallFoliageBackground.impassable)
    ourPlayer.blocks.add(terrainBackground.impassable)

    ourPlayer.world_size = worldSize
    ourPlayer.rect = ourPlayer.image.get_rect()
    ourPlayer.rect = ourPlayer.rect.inflate(-32, 0)
    ourPlayer.rect.inflate_ip(0, -32)
    engine.objects.append(ourPlayer)
    engine.drawables.add(ourPlayer)
    ourOverlay = Overlay(ourPlayer)
    engine.player = ourPlayer


#  ███████╗███╗   ██╗███████╗███╗   ███╗██╗   ██╗
#  ██╔════╝████╗  ██║██╔════╝████╗ ████║╚██╗ ██╔╝
#  █████╗  ██╔██╗ ██║█████╗  ██╔████╔██║ ╚████╔╝
#  ██╔══╝  ██║╚██╗██║██╔══╝  ██║╚██╔╝██║  ╚██╔╝
#  ███████╗██║ ╚████║███████╗██║ ╚═╝ ██║   ██║
#  ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝   ╚═╝
#

    # ourEnemy = Player(10, 100, 100)
    # ourEnemy.image = ourPlayer.image
    # engine.objects.append(ourEnemy)
    # engine.drawables.add(ourEnemy)
    # engine.events[pygame.USEREVENT + 1] = ourEnemy.move_right


#   ██████╗ █████╗ ███╗   ███╗███████╗██████╗  █████╗
#  ██╔════╝██╔══██╗████╗ ████║██╔════╝██╔══██╗██╔══██╗
#  ██║     ███████║██╔████╔██║█████╗  ██████╔╝███████║
#  ██║     ██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗██╔══██║
#  ╚██████╗██║  ██║██║ ╚═╝ ██║███████╗██║  ██║██║  ██║
#   ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
#

    mainCamera = LeagueEngine.LessDumbCamera(engine.viewportWidth, engine.viewportHeight, ourPlayer, engine.drawables, worldSize)
    # c = LeagueEngine.DumbCamera(800, 600, p, e.drawables, world_size)
    engine.mainCamera = mainCamera


#   ██████╗ ██╗   ██╗███████╗██████╗ ██╗      █████╗ ██╗   ██╗
#  ██╔═══██╗██║   ██║██╔════╝██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝
#  ██║   ██║██║   ██║█████╗  ██████╔╝██║     ███████║ ╚████╔╝
#  ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗██║     ██╔══██║  ╚██╔╝
#  ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║███████╗██║  ██║   ██║
#   ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝
#

    # engine.drawables.add(ourOverlay)
    # engine.objects.append(ourOverlay)


#   ██████╗ ██████╗ ██╗     ██╗     ██╗███████╗██╗ ██████╗ ███╗   ██╗███████╗
#  ██╔════╝██╔═══██╗██║     ██║     ██║██╔════╝██║██╔═══██╗████╗  ██║██╔════╝
#  ██║     ██║   ██║██║     ██║     ██║███████╗██║██║   ██║██╔██╗ ██║███████╗
#  ██║     ██║   ██║██║     ██║     ██║╚════██║██║██║   ██║██║╚██╗██║╚════██║
#  ╚██████╗╚██████╔╝███████╗███████╗██║███████║██║╚██████╔╝██║ ╚████║███████║
#   ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
#

    # engine.collisions[ourPlayer] = (ourEnemy, ourPlayer.ouch)

    pygame.time.set_timer(pygame.USEREVENT + 1, 1000 // LeagueEngine.Settings.gameTimeFactor)

    # engine.key_events[pygame.K_a] = ourPlayer.move_left
    # engine.key_events[pygame.K_d] = ourPlayer.move_right
    # engine.key_events[pygame.K_w] = ourPlayer.move_up
    # engine.key_events[pygame.K_s] = ourPlayer.move_down

    engine.events[pygame.QUIT] = engine.stop
    engine.run()


if __name__ == "__main__":
    main()
