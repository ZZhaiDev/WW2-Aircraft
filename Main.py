import pygame
import time
from pygame.locals import *


class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 210
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("feiji/hero1.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5


def key_control(hero_temp):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                hero_temp.move_right()
            elif event.key == K_SPACE:
                print('space')


def main():

    # 1. create screen
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2. create background
    background = pygame.image.load("feiji/background.png")

    # 3. create airplane image
    hero = HeroPlane(screen)

    while True:
        pygame.event.get()  #returns a list of all events currently in the event queue. always not responding if not
        screen.blit(background, (0, 0))
        hero.display()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == '__main__':
    main()
