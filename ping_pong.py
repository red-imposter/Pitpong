from pygame import *
window = display.set_mode((500,500))

class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class racketka(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys_pressed[K_w]:
            if self.rect.y >0:
                self.rect.y -= 1
        if keys_pressed[K_s]:
            if self.rect.y <500:
                self.rect.y += 1
    def update2(self):
        keys = key.get_pressed()
        if keys_pressed[K_UP]:
            if self.rect.y >0:
                self.rect.y -= 1
        if keys_pressed[K_DOWN]:
            if self.rect.y <500:
                self.rect.y += 1
class Ball(GameSprite):
    def __init__(self,img,x,y,speed_x,speed_y):
        super().__init__(img,x,y,0,speed_x,speed_y)
        self.speed_x = speed_x
        self.speed.y = speed.y
    def update_position(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    def update_speeds(self,speed_x,speed_y):
        self.speed.x += self.speed_x
        self.speed.y += self.speed_y
#if sprite.collide_rect(racketka1,ball):

run = True
clock = time.Clock()
FPS = 60

finish = False
back = (23, 11, 186)
window.fill(back)

racketka1 = racketka('racket.png',50,250,4)
racketka2 = racketka('racket.png',450,250,4)
ball = Ball('tenis_ball.png',250,250,3,3,)


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        racketka1.draw()
        racketka2.draw()
        racketka1.update1()
        racketka2.update2()

        display.update()
        clock.tick(FPS)
