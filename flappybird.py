import pygame, pyautogui, random
Width, Height= pyautogui.size()
screen=pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Flappy Bird Game")
background=pygame.transform.scale(pygame.image.load("pictures/background.png"), (Width, Height))
ground=pygame.transform.scale(pygame.image.load("pictures/ground.png"), (Width*2, Height/4))
groundscroll=0
while True:
    screen.blit(background, (0, 0))
    screen.blit(ground, (groundscroll, Height-Height/4))
    groundscroll-=5
    if groundscroll<-Width:
        groundscroll=0
    for i in pygame.event.get():
        if i.type==pygame.QUIT: 
            pygame.quit()
    pygame.display.update()
