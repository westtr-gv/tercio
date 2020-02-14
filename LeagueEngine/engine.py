import abc
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import LeagueEngine
from .settings import *


class Engine:
    """Engine is the definition of our game engine.  We want it to
    be as game agnostic as possible, and will try to emulate code
    from the book as much as possible.  If there are deviations they
    will be noted here.

    Fields:
    title - The name of the game.
    running - Whether or not the engine is currently in the main game loop.
    clock - The real world clock for elapsed time.
    events - A dictionary of events and handling functions.
    objects - A list of updateable game objects.
    drawable - A list of drawable game objects.
    screen - The window we are drawing upon.
    real_delta_time - How much clock time has passed since our last check.
    game_delta_time - How much game time has passed since our last check.
    visible_statistics - Whether to show engine statistics statistics.
    """

    def __init__(self, title, icon={}):
        self.title = title
        self.running = False
        self.clock = None
        self.events = {}
        self.key_events = {}
        self.key_events[Settings.statistics_key] = self.toggle_statistics
        self.objects = []
        self.drawables = pygame.sprite.LayeredUpdates()
        # self.drawables = pygame.sprite.LayeredDirty()
        # self.drawables = LeagueEngine.CustomLayeredUpdates()
        self.screen = None
        self.real_delta_time = 0
        self.visible_statistics = False
        self.statistics_font = None
        self.collisions = {}
        self.overlay = None
        self.icon = icon
        self.player = {}
        self.mainCamera = None

        self.iterations = 0

    def init_pygame(self):
        """This function sets up the state of the pygame system,
        including passing any specific settings to it."""

        # Startup the pygame system
        pygame.init()
        # Create our window
        self.screen = pygame.display.set_mode((Settings.width, Settings.height))
        # Set the title that will display at the top of the window.
        pygame.display.set_caption(self.title)

        # Load the game icon
        self.icon = pygame.image.load(self.icon)
        # Set the game icon
        pygame.display.set_icon(self.icon)

        # Create the clock
        self.clock = pygame.time.Clock()
        self.last_checked_time = pygame.time.get_ticks()
        # Startup the joystick system
        pygame.joystick.init()
        # For each joystick we find, initialize the stick
        for i in range(pygame.joystick.get_count()):
            pygame.joystick.Joystick(i).init()
        # Set the repeat delay for key presses
        pygame.key.set_repeat(Settings.key_repeat)
        # Create statistics font
        self.statistics_font = pygame.font.Font(None, 30)

    def run(self):
        """The main game loop.  As close to our book code as possible."""
        self.running = True

        background = pygame.Surface((Settings.width, Settings.height))
        background.convert()
        background.fill(Settings.fill_color)

        self.drawables.clear(self.screen, background)
        self.screen.fill(Settings.fill_color)

        counter = 0

        while self.running and counter < 30:
            counter = 0  # if you're debugging, set this to counter += 1 and configure your counter < value

            # The time since the last check
            now = pygame.time.get_ticks()
            self.real_delta_time = now - self.last_checked_time
            self.last_checked_time = now
            self.game_delta_time = self.real_delta_time * (0.001 * Settings.gameTimeFactor)

            #  ██╗  ██╗ █████╗ ███╗   ██╗██████╗ ██╗     ███████╗    ██╗███╗   ██╗██████╗ ██╗   ██╗████████╗
            #  ██║  ██║██╔══██╗████╗  ██║██╔══██╗██║     ██╔════╝    ██║████╗  ██║██╔══██╗██║   ██║╚══██╔══╝
            #  ███████║███████║██╔██╗ ██║██║  ██║██║     █████╗      ██║██╔██╗ ██║██████╔╝██║   ██║   ██║
            #  ██╔══██║██╔══██║██║╚██╗██║██║  ██║██║     ██╔══╝      ██║██║╚██╗██║██╔═══╝ ██║   ██║   ██║
            #  ██║  ██║██║  ██║██║ ╚████║██████╔╝███████╗███████╗    ██║██║ ╚████║██║     ╚██████╔╝   ██║
            #  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚══════╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝    ╚═╝
            # region

            # Process inputs
            self.handle_inputs()

            # change the player orientation
            self.mouse_move()
            # endregion

            #   █████╗ ███╗   ██╗██╗███╗   ███╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗
            #  ██╔══██╗████╗  ██║██║████╗ ████║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
            #  ███████║██╔██╗ ██║██║██╔████╔██║███████║   ██║   ██║██║   ██║██╔██╗ ██║███████╗
            #  ██╔══██║██║╚██╗██║██║██║╚██╔╝██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║
            #  ██║  ██║██║ ╚████║██║██║ ╚═╝ ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║███████║
            #  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
            # region

            # TODO : base only increment this if a certain amount of game time has elapsed
            self.iterations += 1

            # handle movement and animation at the same time
            if self.handle_keys():
                self.player.image = self.player.images[self.player.orient][(self.iterations % 8) + 1]
            else:
                self.player.image = self.player.images[self.player.orient][1]

            # reset to avoid big maths
            if self.iterations == 8:
                self.iterations == 0
            # endregion

            #  ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗███████╗
            #  ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝
            #  ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ███████╗
            #  ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚════██║
            #  ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗███████║
            #   ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝
            # region

            # Update game world
            # Each object must have an update(time) method
            # self.check_collisions()
            for o in self.objects:
                o.update(self.game_delta_time)

            # Generate outputs
            # self.drawables.update(self.game_delta_time)
            for each in self.drawables:
                if not isinstance(each, LeagueEngine.GameObject):
                    each.update(self.game_delta_time)

            self.mainCamera.update(self.game_delta_time)
            # endregion

            #  ██████╗ ███████╗███╗   ██╗██████╗ ███████╗██████╗ ██╗███╗   ██╗ ██████╗
            #  ██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗██║████╗  ██║██╔════╝
            #  ██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝██║██╔██╗ ██║██║  ███╗
            #  ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗██║██║╚██╗██║██║   ██║
            #  ██║  ██║███████╗██║ ╚████║██████╔╝███████╗██║  ██║██║██║ ╚████║╚██████╔╝
            #  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
            # region

            # Wipe screen
            # self.screen.fill(Settings.fill_color)
            self.drawables.clear(self.screen, background)

            rects = self.drawables.draw(self.screen)

            # Show statistics?
            if self.visible_statistics:
                self.show_statistics()

            # Show overlay?
            if self.overlay:
                self.show_overlay()

            # Could keep track of rectangles and update here, but eh.
            # pygame.display.flip()
            pygame.display.update(rects)
            # endregion

            #   ██████╗██╗      ██████╗  ██████╗██╗  ██╗
            #  ██╔════╝██║     ██╔═══██╗██╔════╝██║ ██╔╝
            #  ██║     ██║     ██║   ██║██║     █████╔╝
            #  ██║     ██║     ██║   ██║██║     ██╔═██╗
            #  ╚██████╗███████╗╚██████╔╝╚██████╗██║  ██╗
            #   ╚═════╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
            # region
            # Frame limiting code
            self.clock.tick(Settings.fps)
            # endregion

    def check_collisions(self):
        # print("Collisions: ", len(self.collisions))
        for i in self.collisions.keys():
            if pygame.sprite.collide_rect(i, self.collisions[i][0]):
                self.collisions[i][1]()

    # def add_group(self, group):
    #     self.drawables.add(group.sprites())

    def toggle_statistics(self, deltaTime):
        self.visible_statistics = not self.visible_statistics

    def show_statistics(self):
        statistics_string = "Version: " + str(Settings.version)
        statistics_string = statistics_string + " FPS: " + str(int(self.clock.get_fps()))
        fps = self.statistics_font.render(statistics_string, True, Settings.statistics_color)
        self.screen.blit(fps, (10, 10))

    def show_overlay(self):
        self.screen.blit(self.overlay, Settings.overlay_location)

    def stop(self, time):
        self.running = False

    def end(self, time):
        pygame.quit()

    def handle_inputs(self):
        for event in pygame.event.get():
            if event.type in self.events.keys():
                self.events[event.type](self.game_delta_time)
            if event.type == pygame.KEYDOWN:
                if event.key in self.key_events.keys():
                    self.key_events[event.key](self.game_delta_time)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('mousedown')
                pos = pygame.mouse.get_pos()
                print(pos)
            if event.type == pygame.MOUSEBUTTONUP:
                print('mouseup')
                pos = pygame.mouse.get_pos()
                print(pos)

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        pressed = False
        if keys[pygame.K_a]:
            self.player.move_left(self.game_delta_time)
            pressed = True
        elif keys[pygame.K_d]:
            self.player.move_right(self.game_delta_time)
            pressed = True

        if keys[pygame.K_w]:
            self.player.move_up(self.game_delta_time)
            pressed = True
        elif keys[pygame.K_s]:
            self.player.move_down(self.game_delta_time)
            pressed = True

        return pressed

    '''
    The screen is divided into 8 regions to determine the octal direction of the player.
    This funciton determines the compass direction of the player
    '''

    def mouse_move(self):
        mouseScreenPos = pygame.mouse.get_pos()

        # Getting the center of our player in screen space, 
        # rather than the top left of his sprite, nor his 
        # position in world space
        playerCenterX = self.player.rect.x + 32
        playerCenterY = self.player.rect.y + 32

        # Mouse positions relative to where our player is
        mouseRelativeX = mouseScreenPos[0] - playerCenterX
        mouseRelativeY = -1 * (mouseScreenPos[1] - playerCenterY)

        absMouseRelativeX = abs(mouseRelativeX)
        absMouseRelativeY = abs(mouseRelativeY)

        # Just a simple string variable that makes it easier to print out debug logs
        debugMode = False
        if(debugMode):
            temp = ""

        #region Cardinal-Quadrants
        # Checking which cardinal-quadrant we're facing
        if(absMouseRelativeX > absMouseRelativeY):
            # This means the mouse is either East or West of the player
            if(mouseRelativeX > 0):
                self.player.orient = "E"
                if(debugMode):
                    temp += "East"
            else:
                self.player.orient = "W"
                if(debugMode):
                    temp += "West"
        else:
            # This means the mouse is either North or South of the player
            if(mouseRelativeY > 0):
                self.player.orient = "N"
                if(debugMode):
                    temp += "North"
            else:
                self.player.orient = "S"
                if(debugMode):
                    temp += "South"
        #endregion

        #region Corner-Quadrants
        # # Checking which corner-quadrant our mouse is in
        # if(mouseRelativeY > 0):
        #     temp += "Top "
        # else:
        #     temp += "Bottom "

        # if(mouseRelativeX > 0):
        #     temp += "Right"
        # else:
        #     temp += "Left"
        #endregion

        if(debugMode):
            print(temp)

        #region Old Code
        # # Mouse is at or above the player
        # if mouseRelativeY <= self.player.y:
        #     # Orient top
        #     if mouseRelativeX > Settings.width / 3 and mouseRelativeX < Settings.width - (Settings.width / 3):
        #         self.player.orient = "N"

        #     # Mouse is left of the player
        #     elif mouseRelativeX < self.player.x:
        #         # Orient left
        #         if mouseRelativeY > Settings.height / 3 and mouseRelativeY < Settings.height - (Settings.height / 3):
        #             self.player.orient = "W"
        #         else:
        #             # Orient top-left
        #             self.player.orient = "NW"

        #     # Mouse is right of the player
        #     elif mouseRelativeX > self.player.x:
        #         # Orient right
        #         if mouseRelativeY > Settings.height / 3 and mouseRelativeY < Settings.height - (Settings.height / 3):
        #             self.player.orient = "E"
        #         else:
        #             # Orient top-right
        #             self.player.orient = "NE"

        # # Mouse is below the player
        # elif mouseRelativeY > self.player.y:
        #     # Orient bottow
        #     if mouseRelativeX > Settings.width / 3 and mouseRelativeX < Settings.width - (Settings.width / 3):
        #         self.player.orient = "S"

        #     # Mouse is left of the player
        #     elif mouseRelativeX < self.player.x:
        #         # Orient left
        #         if mouseRelativeY > Settings.height / 3 and mouseRelativeY < Settings.height - (Settings.height / 3):
        #             self.player.orient = "W"
        #         else:
        #             # Orient top-left
        #             self.player.orient = "SW"
        #     # Mouse is right of the player
        #     elif mouseRelativeX > self.player.x:
        #         # Orient right
        #         if mouseRelativeY > Settings.height / 3 and mouseRelativeY < Settings.height - (Settings.height / 3):
        #             self.player.orient = "E"
        #         else:
        #             # Orient top-right
        #             self.player.orient = "SE"
        #endregion