import abc
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
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
        self.screen = None
        self.real_delta_time = 0
        self.visible_statistics = False
        self.statistics_font = None
        self.collisions = {}
        self.overlay = None
        self.icon = icon
        self.player = {}

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

        while self.running:
            # The time since the last check
            now = pygame.time.get_ticks()
            self.real_delta_time = now - self.last_checked_time
            self.last_checked_time = now
            self.game_delta_time = self.real_delta_time * (0.001 * Settings.gameTimeFactor)

            # Wipe screen
            # self.screen.fill(Settings.fill_color)
            self.drawables.clear(self.screen, background)

            # Process inputs
            self.handle_inputs()

            self.handle_keys()

            self.mouse_move()

            # change player orientation
            self.iterations += 1
            self.player.image = self.player.images[self.player.orient][(self.iterations % 8) + 1]

            # Update game world
            # Each object must have an update(time) method
            self.check_collisions()
            for o in self.objects:
                o.update(self.game_delta_time)

            # Generate outputs
            # d.update()
            # self.drawables.update(self.game_delta_time)
            rects = self.drawables.draw(self.screen)
            # print(rects)
            # print(self.drawables)

            # Show statistics?
            if self.visible_statistics:
                self.show_statistics()

            # Show overlay?
            if self.overlay:
                self.show_overlay()

            # Could keep track of rectangles and update here, but eh.
            # pygame.display.flip()
            pygame.display.update(rects)

            # Frame limiting code
            self.clock.tick(Settings.fps)

    def check_collisions(self):
        for i in self.collisions.keys():
            if pygame.sprite.collide_rect(i, self.collisions[i][0]):
                self.collisions[i][1]()

    def add_group(self, group):
        self.drawables.add(group.sprites())

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
        if keys[pygame.K_a]:
            self.player.move_left(self.game_delta_time)
        elif keys[pygame.K_d]:
            self.player.move_right(self.game_delta_time)

        if keys[pygame.K_w]:
            self.player.move_up(self.game_delta_time)
        elif keys[pygame.K_s]:
            self.player.move_down(self.game_delta_time)

    '''
    The screen is divided into 8 regions to determine the octal direction of the player.
    This funciton determines the compass direction of the player
    '''

    def mouse_move(self):
        mouseCords = pygame.mouse.get_pos()

        # Mouse is at or above the player
        if mouseCords[1] <= self.player.y:
            # Orient top
            if mouseCords[0] > Settings.width / 3 and mouseCords[0] < Settings.width - (Settings.width / 3):
                self.player.orient = "N"

            # Mouse is left of the player
            elif mouseCords[0] < self.player.x:
                # Orient left
                if mouseCords[1] > Settings.height / 3 and mouseCords[1] < Settings.height - (Settings.height / 3):
                    self.player.orient = "W"
                else:
                    # Orient top-left
                    self.player.orient = "NW"

            # Mouse is right of the player
            elif mouseCords[0] > self.player.x:
                # Orient right
                if mouseCords[1] > Settings.height / 3 and mouseCords[1] < Settings.height - (Settings.height / 3):
                    self.player.orient = "E"
                else:
                    # Orient top-right
                    self.player.orient = "NE"

        # Mouse is below the player
        elif mouseCords[1] > self.player.y:
            # Orient bottow
            if mouseCords[0] > Settings.width / 3 and mouseCords[0] < Settings.width - (Settings.width / 3):
                self.player.orient = "S"

            # Mouse is left of the player
            elif mouseCords[0] < self.player.x:
                # Orient left
                if mouseCords[1] > Settings.height / 3 and mouseCords[1] < Settings.height - (Settings.height / 3):
                    self.player.orient = "W"
                else:
                    # Orient top-left
                    self.player.orient = "SW"
            # Mouse is right of the player
            elif mouseCords[0] > self.player.x:
                # Orient right
                if mouseCords[1] > Settings.height / 3 and mouseCords[1] < Settings.height - (Settings.height / 3):
                    self.player.orient = "E"
                else:
                    # Orient top-right
                    self.player.orient = "SE"
