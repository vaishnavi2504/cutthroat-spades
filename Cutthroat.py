import pygame
from pygame.locals import *


def main():
    # init everything
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Cutthroat Killer Spades')
    clock = pygame.time.Clock()

    # show background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 102, 0))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    while 1:
        clock.tick(60)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        # allsprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        # allsprites.draw(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
