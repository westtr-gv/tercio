import pygame


# Settings
SIZE = WIDTH, HEIGHT = 800, 600  # the width and height of our screen
FPS = 30  # Frames per second


def main():
    # game setup
    pygame.init()
    pygame.display.set_caption('Tercio')
    screen = pygame.display.set_mode(SIZE)
    icon = pygame.image.load('./scenes/icon.png')
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


if __name__ == '__main__':
    main()
