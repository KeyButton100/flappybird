import pygame, pyautogui, random
Width, Height= pyautogui.size()
screen=pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Flappy Bird Game")
background=pygame.transform.scale(pygame.image.load("pictures/background.png"), (Width, Height))
ground=pygame.transform.scale(pygame.image.load("pictures/ground.png"), (Width*2, Height/4))
groundscroll=0
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for i in range(3):
            img=pygame.image.load(f"pictures/bird{i+1}.png")
            img=pygame.transform.scale(img, (150, 100))
            self.images.append(img)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x, y]
    def update(self):
        self.counter+=1
        if self.counter==10:
            self.index+=1
            self.counter=0
        print (self.index)
        if self.index>2:
            self.index=0
        self.image=self.images[self.index]

BirdGroup=pygame.sprite.Group()
flappy=Bird(100, Height/2)
BirdGroup.add(flappy)
while True:
    screen.blit(background, (0, 0))
    screen.blit(ground, (groundscroll, Height-Height/4))
    groundscroll-=5
    BirdGroup.draw(screen)
    BirdGroup.update()
    if groundscroll<-Width:
        groundscroll=0
    for i in pygame.event.get():
        if i.type==pygame.QUIT: 
            pygame.quit()
    pygame.display.update()
