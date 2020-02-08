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

    world = "./Assets/World/Map1_SemiOptimized"
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

    # # cliffSprites = LeagueEngine.Spritesheet("./Assets/Sprites/Tilesets/Outside/Cliff_tileset.png", LeagueEngine.Settings.tile_size, 15)
    # # foliageSprites = LeagueEngine.Spritesheet("./Assets/Sprites/Tilesets/Outside/Outside_B.png", LeagueEngine.Settings.tile_size, 16)
    # # foliage2Sprites = LeagueEngine.Spritesheet("./Assets/Sprites/Tilesets/Outside/object- layer.png", LeagueEngine.Settings.tile_size, 14)
    # # graveyardSprites = LeagueEngine.Spritesheet("./Assets/Sprites/Tilesets/Outside/Graveyard/grave_markers-shadow.png", LeagueEngine.Settings.tile_size, 9)
    # # house1Sprites = LeagueEngine.Spritesheet("./Assets/Sprites/Tilesets/Outside/House/house1_Scaled.png", LeagueEngine.Settings.tile_size, 7)
    # # house2Sprites = LeagueEngine.Spritesheet("./Assets/Sprites/Tilesets/Outside/House2/House_Scaled.png", LeagueEngine.Settings.tile_size, 8)
    # # house3Sprites = LeagueEngine.Spritesheet("./Assets/Sprites/Tilesets/Outside/House3/house3x3_Scaled.png", LeagueEngine.Settings.tile_size, 8)
    # # lootChestSprites = LeagueEngine.Spritesheet("./Assets/Sprites/Loot/chest2_WithTransparent.png", LeagueEngine.Settings.tile_size, 5)
    # # terrainGroundSprites = LeagueEngine.Spritesheet("./Assets/Sprites/Tilesets/Outside/ground_tiles.png", LeagueEngine.Settings.tile_size, 21)
    # # treeSprites = LeagueEngine.Spritesheet("./Assets/Sprites/Tilesets/Outside/treesv6_0.png", LeagueEngine.Settings.tile_size, 21)

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

    # # house3Tilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/House3.lvl", house3Sprites, layer=12)
    # # house2Tilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/House2.lvl", house2Sprites, layer=11)
    # # house1Tilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/House1.lvl", house1Sprites, layer=10)
    # # desertTilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/DesertFoliage.lvl", treeSprites, layer=9)
    # # foliageLargeTilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/FoliageLarge.lvl", foliageSprites, layer=8)
    # # foliageMedTilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/FoliageMedium.lvl", foliage2Sprites, layer=7)
    # # foliageSmallTilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/FoliageSmall.lvl", foliage2Sprites, layer=6)
    # # lootChestTilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/LootChest.lvl", lootChestSprites, layer=5)
    # # graveyardTilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/Graveyard.lvl", graveyardSprites, layer=4)
    # # cliffTilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/Cliffside.lvl", cliffSprites, layer=3)
    # # roadsTilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/RoadsAndRocks.lvl", terrainGroundSprites, layer=2)
    # # terrainTilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/TerrainGround.lvl", terrainGroundSprites, layer=1)
    # # waterTilemap = LeagueEngine.Tilemap("./Assets/World/Map1/LVL/Water.lvl", , layer=0)

    lootChestTilemap = LeagueEngine.Tilemap((world + "/LVL/Map1_Over Player_Loot Chests.csv"), (world + "/LVL/Collidables.csv"), sprites, layer = 5)
    foregroundTilemap = LeagueEngine.Tilemap((world + "/LVL/Map1_Over Player_Foreground.csv"), (world + "/LVL/Collidables.csv"), sprites, layer = 4)
    smallFoliageTilemap = LeagueEngine.Tilemap((world + "/LVL/Map1_Under Player_Small Foliage.csv"), (world + "/LVL/Collidables.csv"), sprites, layer = 2)
    cliffsideTilemap = LeagueEngine.Tilemap((world + "/LVL/Map1_Under Player_Cliffside.csv"), (world + "/LVL/Collidables.csv"), sprites, layer = 1)
    terrainTilemap = LeagueEngine.Tilemap((world + "/LVL/Map1_Under Player_Background.csv"), (world + "/LVL/Collidables.csv"), sprites, layer = 0)




#  ██╗    ██╗ ██████╗ ██████╗ ██╗     ██████╗     ███████╗██╗███████╗███████╗
#  ██║    ██║██╔═══██╗██╔══██╗██║     ██╔══██╗    ██╔════╝██║╚══███╔╝██╔════╝
#  ██║ █╗ ██║██║   ██║██████╔╝██║     ██║  ██║    ███████╗██║  ███╔╝ █████╗  
#  ██║███╗██║██║   ██║██╔══██╗██║     ██║  ██║    ╚════██║██║ ███╔╝  ██╔══╝  
#  ╚███╔███╔╝╚██████╔╝██║  ██║███████╗██████╔╝    ███████║██║███████╗███████╗
#   ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝     ╚══════╝╚═╝╚══════╝╚══════╝
#                                                                            


    # worldSize = (terrainFoliage.wide * LeagueEngine.Settings.tile_size, terrainFoliage.high * LeagueEngine.Settings.tile_size,)
    
    # # worldSize = (terrainTilemap.wide * LeagueEngine.Settings.tile_size, terrainTilemap.high * LeagueEngine.Settings.tile_size,)

    worldSize = (terrainTilemap.wide * LeagueEngine.Settings.tile_size, terrainTilemap.high * LeagueEngine.Settings.tile_size,)


#  ██████╗ ██████╗  █████╗ ██╗    ██╗ █████╗ ██████╗ ██╗     ███████╗███████╗
#  ██╔══██╗██╔══██╗██╔══██╗██║    ██║██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝
#  ██║  ██║██████╔╝███████║██║ █╗ ██║███████║██████╔╝██║     █████╗  ███████╗
#  ██║  ██║██╔══██╗██╔══██║██║███╗██║██╔══██║██╔══██╗██║     ██╔══╝  ╚════██║
#  ██████╔╝██║  ██║██║  ██║╚███╔███╔╝██║  ██║██████╔╝███████╗███████╗███████║
#  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝
#                                                                            


    # engine.drawables.add(terrainFoliage.passable.sprites())
    # engine.drawables.add(terrainBackground.passable.sprites())
    
    # # engine.drawables.add(house3Tilemap.passable.sprites())
    # # engine.drawables.add(house2Tilemap.passable.sprites())
    # # engine.drawables.add(house1Tilemap.passable.sprites())
    # # engine.drawables.add(desertTilemap.passable.sprites())
    # # engine.drawables.add(foliageLargeTilemap.passable.sprites())
    # # engine.drawables.add(foliageMedTilemap.passable.sprites())
    # # engine.drawables.add(foliageSmallTilemap.passable.sprites())
    # # engine.drawables.add(lootChestTilemap.passable.sprites())
    # # engine.drawables.add(graveyardTilemap.passable.sprites())
    # # engine.drawables.add(cliffTilemap.passable.sprites())
    # # engine.drawables.add(roadsTilemap.passable.sprites())
    # # engine.drawables.add(terrainTilemap.passable.sprites())
    # # engine.drawables.add(waterTilemap.passable.sprites())

    engine.drawables.add(lootChestTilemap.passable.sprites())
    engine.drawables.add(foregroundTilemap.passable.sprites())
    engine.drawables.add(smallFoliageTilemap.passable.sprites())
    engine.drawables.add(cliffsideTilemap.passable.sprites())
    engine.drawables.add(terrainTilemap.passable.sprites())




#  ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ 
#  ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
#  ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝
#  ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
#  ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║
#  ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
#                                                   


    ourPlayer = Player(3, 1000, 1000)
    ourOverlay = Overlay(ourPlayer)
    # ourPlayer.blocks.add(terrainFoliage.impassable)
    # # ourPlayer.blocks.add(cliffTilemap.impassable)
    # # ourPlayer.blocks.add(desertTilemap.impassable)
    # # ourPlayer.blocks.add(foliageLargeTilemap.impassable)
    # # ourPlayer.blocks.add(foliageMedTilemap.impassable)
    # # ourPlayer.blocks.add(foliageSmallTilemap.impassable)
    # # ourPlayer.blocks.add(graveyardTilemap.impassable)
    # # ourPlayer.blocks.add(house1Tilemap.impassable)
    # # ourPlayer.blocks.add(house2Tilemap.impassable)
    # # ourPlayer.blocks.add(house3Tilemap.impassable)
    # # ourPlayer.blocks.add(lootChestTilemap.impassable)
    # # ourPlayer.blocks.add(roadsTilemap.impassable)
    # # ourPlayer.blocks.add(terrainTilemap.impassable)
    # # ourPlayer.blocks.add(waterTilemap.impassable)
    ourPlayer.blocks.add(lootChestTilemap.impassable)
    ourPlayer.blocks.add(foregroundTilemap.impassable)
    ourPlayer.blocks.add(smallFoliageTilemap.impassable)
    ourPlayer.blocks.add(cliffsideTilemap.impassable)
    ourPlayer.blocks.add(terrainTilemap.impassable)
    ourPlayer.world_size = worldSize
    ourPlayer.rect = ourPlayer.image.get_rect()
    engine.objects.append(ourPlayer)
    engine.drawables.add(ourPlayer)
    engine.player = ourPlayer


#  ███████╗███╗   ██╗███████╗███╗   ███╗██╗   ██╗
#  ██╔════╝████╗  ██║██╔════╝████╗ ████║╚██╗ ██╔╝
#  █████╗  ██╔██╗ ██║█████╗  ██╔████╔██║ ╚████╔╝ 
#  ██╔══╝  ██║╚██╗██║██╔══╝  ██║╚██╔╝██║  ╚██╔╝  
#  ███████╗██║ ╚████║███████╗██║ ╚═╝ ██║   ██║   
#  ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝   ╚═╝   
#                                                

    
    ourEnemy = Player(10, 100, 100)
    ourEnemy.image = ourPlayer.image
    engine.objects.append(ourEnemy)
    engine.drawables.add(ourEnemy)
    engine.events[pygame.USEREVENT + 1] = ourEnemy.move_right
    

#   ██████╗ █████╗ ███╗   ███╗███████╗██████╗  █████╗ 
#  ██╔════╝██╔══██╗████╗ ████║██╔════╝██╔══██╗██╔══██╗
#  ██║     ███████║██╔████╔██║█████╗  ██████╔╝███████║
#  ██║     ██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗██╔══██║
#  ╚██████╗██║  ██║██║ ╚═╝ ██║███████╗██║  ██║██║  ██║
#   ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
#                                                     


    mainCamera = LeagueEngine.LessDumbCamera(800, 600, ourPlayer, engine.drawables, worldSize)
    # c = LeagueEngine.DumbCamera(800, 600, p, e.drawables, world_size)
    engine.objects.append(mainCamera)


#   ██████╗ ██╗   ██╗███████╗██████╗ ██╗      █████╗ ██╗   ██╗
#  ██╔═══██╗██║   ██║██╔════╝██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝
#  ██║   ██║██║   ██║█████╗  ██████╔╝██║     ███████║ ╚████╔╝ 
#  ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗██║     ██╔══██║  ╚██╔╝  
#  ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║███████╗██║  ██║   ██║   
#   ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   
#                                                             


    engine.drawables.add(ourOverlay)
    engine.objects.append(ourOverlay)

    
#   ██████╗ ██████╗ ██╗     ██╗     ██╗███████╗██╗ ██████╗ ███╗   ██╗███████╗
#  ██╔════╝██╔═══██╗██║     ██║     ██║██╔════╝██║██╔═══██╗████╗  ██║██╔════╝
#  ██║     ██║   ██║██║     ██║     ██║███████╗██║██║   ██║██╔██╗ ██║███████╗
#  ██║     ██║   ██║██║     ██║     ██║╚════██║██║██║   ██║██║╚██╗██║╚════██║
#  ╚██████╗╚██████╔╝███████╗███████╗██║███████║██║╚██████╔╝██║ ╚████║███████║
#   ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
#                                                                            


    engine.collisions[ourPlayer] = (ourEnemy, ourPlayer.ouch)



    pygame.time.set_timer(pygame.USEREVENT + 1, 1000 // LeagueEngine.Settings.gameTimeFactor)

    # engine.key_events[pygame.K_a] = ourPlayer.move_left
    # engine.key_events[pygame.K_d] = ourPlayer.move_right
    # engine.key_events[pygame.K_w] = ourPlayer.move_up
    # engine.key_events[pygame.K_s] = ourPlayer.move_down

    engine.events[pygame.QUIT] = engine.stop
    engine.run()


if __name__ == "__main__":
    main()
