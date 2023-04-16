#Создай собственный Шутер!

from pygame import *
from random import randint

lost = 0
score = 0 

class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_speed, x, y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x,y)) 
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
    
    def fire(self):
        bullet = Bullet("Jam.png", self.rect.x, self.rect.y, 20, 27, 37 )
        bullets.add(bullet)


class Enemy(GameSprite):
    def update(self):
        global lost
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.x = randint(0,700)
            self.rect.y = 0
            lost+=1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()




# #создай окно игры
window = display.set_mode((700,500))
display.set_caption('Аои френдзонит')
background = transform.scale(image.load('AlterEgo.jpg'),(700,500))


clock = time.Clock()
FPS = 70

mixer.init()
mixer.music.load('Traumerei.mp3')
#mixer.music.play()
font.init()
font1 = font.SysFont('Arial', 36)





player = Player('Aoi.png', 400, 400, 5, 54, 99 )

bullets = sprite.Group()



vragi = sprite.Group()
for i in range(5):
    vrag = Enemy('Tsubaki.png', randint(0,700), 0, randint(1,3), 79,124)
    vragi.add(vrag)

Vragi1 = sprite.Group()
for i in range(2):
    vrag = Enemy('Haruna.png', randint(0,700), 0, randint(1,3), 50,110)
    Vragi1.add(vrag)







game = True
finish = False 

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    if finish != True:
        window.blit(background,(0,0))
        player.reset()
        player.update()
        vragi.draw(window)
        vragi.update()
        Vragi1.draw(window)
        Vragi1.update()
        bullets.draw(window)
        bullets.update()
        sprite_list = sprite.groupcollide(vragi, bullets,True, True)
        for vr in sprite_list:
            score += 1
            vrag = Enemy('Tsubaki.png', randint(0,700), 0, randint(1,3), 96,128)
            vragi.add(vrag)

        text_lose = font1.render('Призналось в любви: '+ str(lost), 1, (255,255,255))
        window.blit(text_lose, (10,20))
        text_score = font1.render('Зафрендзонено: '+ str(score), 1, (255,255,255))
        window.blit(text_score, (10,50))
    

        if score >= 10:
            text_win = font1.render('Ура , победа! ' , 1, (0,0,0))
            window.blit(text_win, (270,250))
            finish = True

        if lost >= 15:
            text_lost = font1.render('Неееееет ' , 1, (0,0,0))
            window.blit(text_lost, (270,250))
            finish = True

        sprite_list1= sprite.spritecollide(player, vragi, False)
        if len(sprite_list1) > 0:
            text_lost1 = font1.render('Цубаки,я хочу твой голос ' , 1, (0,0,0))
            window.blit(text_lost1, (270,250))
            finish = True

        sprite_list2= sprite.spritecollide(player, Vragi1, False)
        if len(sprite_list2) > 0:
            text_lost2 = font1.render('ХарунаАои канон?' , 1, (0,0,0))
            window.blit(text_lost2, (270,250))
            finish = True
















    
    clock.tick(FPS)
    display.update()