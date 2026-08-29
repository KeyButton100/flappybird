import pygame, pyautogui, random
from pygame.locals import *
pygame.init()
clock=pygame.time.Clock()
fps=60
pipefrequency=2000
lastpipe=pygame.time.get_ticks()-pipefrequency
Width, Height= pyautogui.size()
screen=pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Flappy Bird Game")
background=pygame.transform.scale(pygame.image.load("pictures/background.png"), (Width, Height))
ground=pygame.transform.scale(pygame.image.load("pictures/ground.png"), (Width*2, Height/4))
pipegap=250
gamestate="start"
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
        self.rotation=0
        self.v=0
    def update(self):
        global gamestate
        if gamestate=="play":
            self.counter+=1
            self.v+=0.1
            if self.v>8:
                self.v=8
            if pygame.mouse.get_pressed()[0]==1:
               self.v=-7
            if self.rect.bottom<Height-Height/4:
                self.rect.y+=self.v
            

            if self.counter==10:
                self.index+=1
                self.counter=0
            print (self.v)
            if self.index>2:
                self.index=0
            self.image=self.images[self.index]
            self.image=pygame.transform.rotate(self.image, self.v*-2)
        if gamestate=="stop":
            self.image=pygame.transform.rotate(self.image, -90)
            gamestate="end"
            #print("gameover")

class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y,position):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("C:/Users/SAMUEL NIODE/Documents/Visual Studio Code/PyGame/pictures/pipe.png")
        self.rect=self.image.get_rect()
        self.imgae=pygame.transform.scale(self.image, (100, 200))
        if position=="top":
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-pipegap/2]
        if position=="bottom":
            self.rect.topleft=[x,y+pipegap/2]
    def update(self):
        self.rect.x-=5
        if self.rect.right<0:
            self.kill()

PipeGroup=pygame.sprite.Group()

BirdGroup=pygame.sprite.Group()
flappy=Bird(100, Height/2)
BirdGroup.add(flappy)
while True:
    screen.blit(background, (0, 0))
    screen.blit(ground, (groundscroll, Height-Height/4))
    
    BirdGroup.draw(screen)
    BirdGroup.update()
    if gamestate=="play":
        groundscroll-=5
        if groundscroll<-Width:
            groundscroll=0
        if flappy.rect.bottom>Height-Height/4:
            gamestate="stop"
        latesttime=pygame.time.get_ticks()
        if latesttime-lastpipe>pipefrequency:
            pipeheight=random.randint(-100,100)
            bottompipe=Pipe(Width, Height/2+pipeheight, "bottom")
            toppipe=Pipe(Width, Height/2+pipeheight, "top")
            PipeGroup.add(bottompipe)
            PipeGroup.add(toppipe)
            lastpipe=latesttime
        PipeGroup.update()
        PipeGroup.draw(screen)
    for i in pygame.event.get():
        if i.type==pygame.QUIT: 
            pygame.quit()
        if i.type==pygame.MOUSEBUTTONDOWN and gamestate=="start":
            gamestate="play"
    pygame.display.update()
