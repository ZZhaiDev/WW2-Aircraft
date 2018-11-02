import pygame
import time
from pygame.locals import *
import random


class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 210
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("feiji/hero1.png")
        self.bullet_list = []

        # 爆炸效果用的如下属性
        self.hit = False  # 表示是否要爆炸
        self.bomb_list = []  # 用来存储爆炸时需要的图片
        self.__crate_images()  # 调用这个方法向bomb_list中添加图片
        self.image_num = 0  # 用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0  # 用来记录当前要显示的爆炸效果的图片的序号

    def __crate_images(self):
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n1.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n2.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n3.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n4.png"))

    def display(self):
        if self.hit == True:
            self.screen.blit(self.bomb_list[self.image_index], (self.x, self.y))
            self.image_num += 1
            if self.image_num == 7:
                self.image_num = 0
                self.image_index += 1
            if self.image_index > 3:
                time.sleep(1)
                exit()  # 调用exit让游戏退出
                # self.image_index = 0
        else:
            self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

    def bomb(self):
        self.hit = True


class EnemyPlane(object):
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load("feiji/enemy0.png")
        self.bullet_list = []
        self.direction = "right"

    def display(self, hero):
        self.screen.blit(self.image, (self.x, self.y))
        self.move()
        self.fire()
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if hero.x < bullet.x < hero.x + 100 and hero.y < bullet.y < hero.y + 100:
                print(hero.x)
                print(hero.y)
                print(bullet.x)
                print(bullet.y)
                hero.bomb()
            if bullet.judge():
                self.bullet_list.remove(bullet)

    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5
        if self.x > 430:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(0, 100)
        if random_num == 8 or random_num == 20:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen_temp
        self.image = pygame.image.load("feiji/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 20

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False


class EnemyBullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 25
        self.y = y + 40
        self.screen = screen_temp
        self.image = pygame.image.load("feiji/bullet1.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False


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
                hero_temp.fire()
            elif event.key == K_b:
                print('b')
                hero_temp.bomb()


def main():

    # 1. create screen
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2. create background
    background = pygame.image.load("feiji/background.png")

    # 3. create airplane image
    hero = HeroPlane(screen)

    # 4. create a enemyplane
    enemy = EnemyPlane(screen)

    while True:
        pygame.event.get()  #returns a list of all events currently in the event queue. always not responding if not
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display(hero)
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == '__main__':
    main()
