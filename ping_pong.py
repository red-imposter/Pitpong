from pygame import *
window = display.set_mode((500,500))


run = True
clock = time.Clock()
FPS = 60

back = (23, 11, 186)
window.fill(back)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(FPS)