import pygame
import random
#设置常量
#颜色
GREEN = (0, 197, 205)#python元组数据类型
BLACK = (0, 0, 0)
#窗口大小
WIDTH,HEIGHT = 800,600
#自定义敌机出现的时间
CREATE_ENEMY = pygame.USEREVENT
#初始化
pygame.init()
#创建游戏窗口
screen = pygame.display.set_mode((800,600))
#游戏循环
pygame.display.set_caption("飞机大战")
#设置系统时钟
clock = pygame.time.Clock()
pygame.time.set_timer(CREATE_ENEMY,1000)

#初始化英雄
class Hero(pygame.sprite.Sprite):
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/me1.png")
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 60
        self.speed = speed

    def update(self,*args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE]:
            self.fire()

    def fire(self):
        #发射子弹
        bullet = Bullet(10)
        bullet.rect.x += self.rect.right
        bullet.rect.centery += self.rect.centery
        bullet_group.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/bullet1.png")
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.x += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/enemy1.png")
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(0,HEIGHT)
        self.speed = speed

    def update(self, *args):
       self.rect.x -= self.speed


#初始化英雄
hero = Hero(2)
# enemy1 = Enemy(random.randint(1,4))
# enemy2 = Enemy(random.randint(1,4))
#初始化精灵组
hero_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
hero_group.add(hero)



#游戏循环
while True:
    #设置刷新率
    clock.tick(60)
    #玩家操作
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == CREATE_ENEMY:
            enemy_group.add(Enemy(random.randint(1,4)))
    #游戏更新
    screen.fill(BLACK)
    #碰撞检测
    pygame.sprite.groupcollide(enemy_group,bullet_group,True,True)

    # hero_group.update()
    # enemy_group.update()
    # bullet_group.update()
    # #屏幕更新
    # hero_group.draw(screen)
    # enemy_group.draw(screen)
    # bullet_group.draw(screen)
    # pygame.display.update()
    #屏幕更新
    for group in [hero_group, enemy_group, bullet_group]:
        group.update()
        group.draw(screen)
    pygame.display.update()

#1221323git测试所用
#789
#jkl
#15161718