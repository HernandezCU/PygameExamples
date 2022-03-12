import pygame, sys, time
from pygame.locals import *

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()

width=400
height=300
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Animation')
background=pygame.image.load('up.png')


UP='up'
LEFT='left'
RIGHT='right'
DOWN='down'

sprite=pygame.image.load('down.png')
spritex=200
spritey=130
direction=DOWN


while True:
    DISPLAYSURF.blit(background,(0,0))

    DISPLAYSURF.blit(sprite,(spritex,spritey))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if (event.key == pygame.K_LEFT):
                sprite=pygame.image.load('left.png')
            elif (event.key == pygame.K_RIGHT):
                sprite=pygame.image.load('right.png')
            elif (event.key == pygame.K_UP):
                sprite=pygame.image.load('up.png')
            elif (event.key == pygame.K_DOWN):
                sprite=pygame.image.load('down.png')

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        spritex -= 5

    if keys_pressed[pygame.K_RIGHT]:
        spritex += 5

    if keys_pressed[pygame.K_UP]:
        spritey -= 5

    if keys_pressed[pygame.K_DOWN]:
        spritey += 5

    pygame.display.update()
    fpsClock.tick(FPS)