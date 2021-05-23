from pygame import *
window = display.set_mode((950,700))

class GameSprite(sprite.Sprite):
    def __init__(self,img,x,y,speed,width,height):
        super().__init__()
        self.image = transform.scale(image.load(img),(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class racketka(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            if self.rect.y >0:
                self.rect.y -= self.speed
        if keys_pressed[K_s]:
            if self.rect.y < 600:
                self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            if self.rect.y >0:
                self.rect.y -= self.speed
        if keys_pressed[K_DOWN]:
            if self.rect.y < 600:
                self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self,img,x,y,speed_x,speed_y,width,height):
        super().__init__(img,x,y,0,width,height)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update_position(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    def update_speeds(self,speed_x,speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y

run = True
clock = time.Clock()
FPS = 60

speed_x = 6
speed_y = 6

finish = False

font.init()
font1 = font.Font(None,70)
win1 = font1.render('Player 1 win!', True, (255,0,0))
font2 = font.Font(None,70)
win2 = font2.render('Player 2 win!', True, (255,0,0))


racketka1 = racketka('racket.png',5,250,4,50,100)
racketka2 = racketka('racket.png',895,250,4,50,100)
ball = Ball('tenis_ball.png',250,250,1,1,50,50)


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        back = (23, 11, 186)
        window.fill(back)
        racketka1.draw()
        racketka2.draw() 
        ball.draw()
        racketka1.update1()
        racketka2.update2()
        ball.update_speeds(speed_x,speed_y)
        ball.update_position()
        if sprite.collide_rect(racketka1,ball) or sprite.collide_rect(racketka2,ball):
            speed_x *= -1
        if ball.rect.y > 650 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > 950:
            window.blit(win1,(340,350))
            finish = True
        if ball.rect.x < 0:
            window.blit(win2,(340,350))
            finish = True

        display.update()
        clock.tick(FPS)
