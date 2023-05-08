import pygame
pygame.init()

mw = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
FPS = 120
pygame.display.set_caption("Piano")

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, sound, button):
        super().__init__()
        self.image = pygame.transform.scale(image,(width,height))
        self.rect = pygame.Rect(x,y,w,h)
        self.sound = sound
        self.button = button
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))
    def clicked(self):
        k = pygame.key.get_pressed()
        if k[self.button]:
		    pygame.mixer.music.load(sound)
		    pygame.mixer.music.play()

key01 = Button(350,250,)

finish = False
game = True
while game:

    for ev in pygame.event.get():
        if not finish:
            if ev.type == pygame.QUIT:
                game = False
    pygame.display.update()
    clock.tick(FPS)

