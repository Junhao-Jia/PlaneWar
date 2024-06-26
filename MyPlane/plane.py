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
pygame.time.set_timer(CREATE_ENEMY,200)
#创建游戏窗口
screen = pygame.display.set_mode((800,600))
#游戏循环
pygame.display.set_caption("飞机大战")
#设置系统时钟
clock = pygame.time.Clock()

#添加背景音乐


#初始化英雄
class Hero(pygame.sprite.Sprite):
    def __init__(self,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/me1.png")
        self.rect = self.image.get_rect()
        self.rect.width *= 0.7
        self.rect.height *= 0.7
        self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))
        self.rect.x = 80
        self.rect.y = 60
        self.speed = speed
        self.ready_to_fire = 0
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
            if self.ready_to_fire == 0:
                self.fire()
            self.ready_to_fire += 1
            if self.ready_to_fire > 5:
                self.ready_to_fire = 0
        else:
            self.ready_to_fire = 0
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
        if self.rect.x > WIDTH:
            self.kill()

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
        if self.rect.x <= 0:
            self.kill()

class Explode(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = [pygame.image.load("./images/enemy1_down"+str(i)+".png") for i in range(1,4)]
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.ready_to_change = 0
    def update(self, *args):
        if self.image_index < 2:
            self.ready_to_change += 1
            if self.ready_to_change % 4 == 0:
                self.image_index += 1
                self.image = self.images[self.image_index]
        else:
            self.kill()

class BackGround(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./images/background.png")
        self.rect = self.image.get_rect()
        self.ready_to_move = 0
    def update(self, *args):
        if self.ready_to_move == 0:
            self.rect.x -= 1
            if self.rect.right <= 0:
                self.rect.x = self.rect.width
        if self.ready_to_move > 2:
            self.ready_to_move = 0
        else:
            self.ready_to_move += 1
#初始化英雄
hero = Hero(2)

#初始化背景
bg = BackGround()
bg1 = BackGround()
bg1.rect.x = bg1.rect.width
#初始化精灵组
bg_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
explode_group = pygame.sprite.Group()
hero_group.add(hero)
bg_group.add(bg,bg1)


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
    collision = pygame.sprite.groupcollide(enemy_group,bullet_group,True,True)
    for enemy in collision.keys():
        explode = Explode()
        explode.rect = enemy.rect
        explode_group.add(explode)

    #屏幕更新
    for group in [bg_group,hero_group, enemy_group, bullet_group,explode_group]:
        group.update()
        group.draw(screen)
    pygame.display.update()

