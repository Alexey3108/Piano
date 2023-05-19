import pygame
pygame.init()
pygame.mixer.init()

mw = pygame.display.set_mode((743, 70))
clock = pygame.time.Clock()
FPS = 120
pygame.display.set_caption("Piano")
white = (230,230,230)
#sound_busy = pygame.mixer.get_busy()
keys = list()

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, sound, button, text):
        super().__init__()
        self.rect = pygame.Rect(x,y,w,h)
        self.sound = pygame.mixer.Sound(sound)
        self.button = button
        self.image = pygame.font.Font(None, 30).render(text, True, (0,0,0))
        keys.append(self)
    def reset(self):
        pygame.draw.rect(mw, white, self.rect)
        mw.blit(self.image, (self.rect.x + 10, self.rect.y + 25))
    def clicked(self,event):
        if event.key == self.button:
            self.sound.play()
    def unclicked(self,event):
        if event.key == self.button:
            self.sound.stop()
        #k = pygame.key.get_pressed()
        #if k[self.button]:
        #    self.sound.play()
        #else:
        #    pygame.mixer.stop()
            #pygame.mixer.music.load(self.sound)
            #pygame.mixer.music.play()

key1 = Button(0,0,30,70,'key01.ogg',pygame.K_q, 'q')
key2 = Button(31,0,30,70,'key02.ogg',pygame.K_w, 'w')
key3 = Button(62,0,30,70,'key03.ogg',pygame.K_e, 'e')
key4 = Button(93,0,30,70,'key04.ogg',pygame.K_r, 'r')
key5 = Button(124,0,30,70,'key05.ogg',pygame.K_t, 't')
key6 = Button(155,0,30,70,'key06.ogg',pygame.K_y, 'y')
key7 = Button(186,0,30,70,'key07.ogg',pygame.K_u, 'u')
key8 = Button(217,0,30,70,'key08.ogg',pygame.K_i, 'i')
key9 = Button(248,0,30,70,'key09.ogg',pygame.K_o, 'o')
key10 = Button(279,0,30,70,'key10.ogg',pygame.K_p, 'p')
key11 = Button(310,0,30,70,'key11.ogg',pygame.K_a, 'a')
key12 = Button(341,0,30,70,'key12.ogg',pygame.K_s, 's')
key13 = Button(372,0,30,70,'key13.ogg',pygame.K_d, 'd')
key14 = Button(403,0,30,70,'key14.ogg',pygame.K_f, 'f')
key15 = Button(434,0,30,70,'key15.ogg',pygame.K_g, 'g')
key16 = Button(465,0,30,70,'key16.ogg',pygame.K_h, 'h')
key17 = Button(496,0,30,70,'key17.ogg',pygame.K_j, 'j')
key18 = Button(527,0,30,70,'key18.ogg',pygame.K_k, 'k')
key19 = Button(558,0,30,70,'key19.ogg',pygame.K_l, 'l')
key20 = Button(589,0,30,70,'key20.ogg',pygame.K_z, 'z')
key21 = Button(620,0,30,70,'key21.ogg',pygame.K_x, 'x')
key22 = Button(651,0,30,70,'key22.ogg',pygame.K_c, 'c')
key23 = Button(682,0,30,70,'key23.ogg',pygame.K_v, 'v')
key24 = Button(713,0,30,70,'key24.ogg',pygame.K_b, 'b')

game = True
while game:
    for key in keys:
        key.reset()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = False
        if ev.type == pygame.KEYDOWN:
            for i in range(24):
                keys[i].clicked(ev)
        if ev.type == pygame.KEYUP:
            for i in range(24):
                keys[i].unclicked(ev)

        
    pygame.display.update()
    clock.tick(FPS)

