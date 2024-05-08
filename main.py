import pygame.sprite
from pygame import *
from random import randint

init()

W = 700
H = 700

window = display.set_mode((W, H))
display.set_caption("maze")
display.set_icon(image.load('images/hero_r.png'))

bg = transform.scale(image.load('images/background.jpg'), (W, H))
clock = time.Clock()

mixer.init()
mixer.music.load('sounds/Yg Marley - Praise Jah In The Moonlight.mp3')
mixer.music.set_volume(0.1)
mixer.music.play()
class GameSprite(sprite.Sprite):
    # конструктор класу з властивостями
    def __init__(self, img, x, y, width, height, speed):
        super().__init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    # метод для малювання спрайту
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):#
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.image = transform.scale(image.load('images/hero_l.png'), (self.width, self.height))
        if keys_pressed[K_d] and self.rect.x < W - self.width:
            self.rect.x += self.speed
            self.image = transform.scale(image.load('images/hero_r.png'), (self.width, self.height))
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < H - self.height:
            self.rect.y += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, width, height, x, y):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    direction = 'right'
    def update_r_l(self, start, end):
        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed

        if self.direction == 'right' and self.rect.x >= end:
            self.direction = 'left'
            self.image = transform.scale(image.load('images/cyborg_l.png'), (self.width, self.height))
        if self.direction == 'left' and self.rect.x <= start:
            self.direction = 'right'
            self.image = transform.scale(image.load('images/cyborg.png'), (self.width, self.height))
    def update_u_p(self, start, end):
        if self.direction == 'up':
            self.rect.y += self.speed
        if self.direction == 'down':
            self.rect.y -= self.speed

        if self.direction == 'up' and self.rect.y >= end:
            self.direction = 'down'
        if self.direction == 'down' and self.rect.y <= start:
            self.direction = 'up'


player = Player('images/hero_r.png', W - 50, 50, 50, 50, 4)
enemy1 = Enemy('images/cyborg.png', 100, 340, 50, 50, 2)
enemy2 = Enemy('images/cyborg.png', 50, 600, 50, 50, 4)
enemy2.direction = 'up'

wall1 = Wall(102, 255, 102, 15, 4000, 20, 20)
wall2 = Wall(102, 255, 102, 15, 400, 120, 320)
wall3 = Wall(102, 255, 102, 4000, 15, 20, 20)
wall4 = Wall(102, 255, 102, 15, 400, 620, 20)
wall5 = Wall(102, 255, 102, 15, 300, 300, 20)
wall6 = Wall(102, 255, 102, 370, 15, 250, 405)
wall7 = Wall(102, 255, 102, 250, 15, 300, 305)
wall8 = Wall(102, 255, 102, 4000, 15, 250, 550)
wall9 = Wall(102, 255, 102, 15, 210, 550, 110)
wall10 = Wall(102, 255, 102, 150, 15, 400, 110)
wall11 = Wall(102, 255, 102, 15, 130, 400, 110)
wall12 = Wall(102, 255, 102, 300, 15, 250, 525)
wall13 = Wall(102, 255, 102, 15, 125, 250, 405)
wall14 = Wall(102, 255, 102, 15, 225, 620, 400)
wall15 = Wall(102, 255, 102, 375, 15, 250, 610)
wall16 = Wall(102, 255, 102, 15, 205, 120, 20)
wall17 = Wall(102, 255, 102, 125, 15, 120, 210)
wall18 = Wall(102, 255, 102, 15, 105, 230, 120)

walls_lst = sprite.Group(wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall10, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18)
coin1 = GameSprite('images/coin1.png', 300, 450, 50, 50, 0)
coin2 = GameSprite('images/coin1.png', 450, 150, 50, 50, 0)
coin3 = GameSprite('images/coin1.png', 150, 150, 50, 50, 0)
coins_lst = sprite.Group(coin1, coin2, coin3)

portal = GameSprite('images/portal.png', 50, 650, 50, 50, 4)
portal1 = GameSprite('images/portal1.png', W - 50, - 200, 50, 50, 0)

coins_count = 0
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish is False:
        window.blit(bg, (0, 0))
        player.reset()
        player.update()
        walls_lst.draw(window)
        coins_lst.draw(window)
        enemy1.reset()
        enemy1.update_r_l(150, 500)
        enemy2.reset()
        enemy2.update_u_p(50, 600)
        portal.reset()

        if player.rect.colliderect(portal.rect):
            skrime = GameSprite('images/skrimer.jpg', 0, 0, 700, 700, 4)
            skrime.reset()
            mixer.music.stop()
            music = mixer.Sound('sounds/skrimer.ogg')
            music.play()
            finish = True

        if sprite.spritecollide(player, walls_lst, False) or sprite.collide_rect(player, enemy1) or sprite.collide_rect(player, enemy2):
             font = pygame.font.Font(None, 64)
             text = font.render('Програв', True, (255, 0, 0))
             text_rect = text.get_rect(center=(350,250))
             window.blit(text, text_rect)
             finish = True

        if sprite.spritecollide(player, coins_lst, True):
            coins_count += 1
        if coins_count == 3:
            portal1.rect.y = 50
            portal1.reset()
        if player.rect.colliderect(portal1.rect):
            end = GameSprite('images/win.jpg', 0, 0, 700, 700, 4)
            end.reset()
            mixer.music.stop()
            music = mixer.Sound('sounds/02-little-angels.mp3')
            music.play()
            finish = True


    else:
        keys_pressed = key.get_pressed()
        if keys_pressed [K_r]:
            finish = False
            player.rect.x = W - 50
            player.rect.y = 50
            coins_count = 0
            coins_lst.empty()
            coins_lst = sprite.Group(coin1, coin2, coin3)
            portal1.rect.x = W - 50
            portal1.rect.y = - 200




    clock.tick(40)
    display.update()