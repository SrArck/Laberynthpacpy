from pygame import *



class MainSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_speed):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(p_image), (80, 80))
       self.speed = p_speed
       self.rect = self.image.get_rect()
       self.rect_x = p_x
       self.rect_y = p_y
    def reset(self):
        window.blit(self.image, (self.rect_x, self.rect_y))

class Player(MainSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect_x > 5:
            self.rect_x -= self.speed
        if keys[K_RIGHT] and self.rect_x < SCREEN_WIDTH - 80:
            self.rect_x += self.speed
        if keys[K_UP] and self.rect_y > 5:
            self.rect_y -= self.speed
        if keys[K_DOWN] and self.rect_y < SCREEN_WIDTH - 80:
            self.rect_y += self.speed

init()
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
FPS = 144
clock = time.Clock()
display.set_caption("Carlitos Screen")
window = display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))

hero = Player('hero.png', SCREEN_WIDTH, 5, 5)

finish = False

running = True
while running:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            running = False
    
    if not finish:
        window.fill((0,0,0))

        hero.update()
        hero.reset()

    display.update()
