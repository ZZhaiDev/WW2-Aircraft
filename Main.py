import pygame
import time
from pygame.locals import *


def main():

    # 1. create screen
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2. create background
    background = pygame.image.load("feiji/background.png")

    # 3. create airplane image
    hero = pygame.image.load("feiji/hero1.png")

    x = 210
    y = 700

    while True:
        pygame.event.get()  #returns a list of all events currently in the event queue. always not responding if not
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    x -= 5
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x += 5
                elif event.key == K_SPACE:
                    print('space')

        time.sleep(0.01)


if __name__ == '__main__':
    main()