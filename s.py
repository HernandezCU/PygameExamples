import pygame, sys, time
import pygame.rect
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

width = 400
height = 300
DISPLAYSURF = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Animation')


sprite = pygame.image.load('up.jpg')

spritex = 200
spritey = 130

white = (255, 255, 255)
black = (0, 0, 0)


# def check_collision(box: pygame.rect.Rect,player: pygame.rect.Rect):
#     oxv = [box.left, box.right]
#     oyv = [box.top, box.bottom]
#     pxv = [player.left, player.right]
#     pyv = [player.top, player.bottom]
#     print(oxv)
#     print(oyv)
#     print(pxv)
#     print(pyv)
#     if((pxv[0] > oxv[0]) and (pxv[0] < oxv[1])) or ((pxv[1] > oxv[0]) and (pxv[1] < oxv[1])):
#         if ((pyv[0] > oyv[0]) and (pyv[0] < oyv[1])) or ((pyv[1] > oyv[0]) and (pyv[1] < oyv[1])):
#             print("Collision")


def check_collision(box: pygame.rect.Rect, playerx, playery):
    oxv = [box.left, box.right]
    oyv = [box.top, box.bottom]
    pxv = [playerx, playerx + 74]
    pyv = [playery, playery + 74]

    if((pxv[0] > oxv[0]) and (pxv[0] < oxv[1])) or ((pxv[1] > oxv[0]) and (pxv[1] < oxv[1])):
        if ((pyv[0] > oyv[0]) and (pyv[0] < oyv[1])) or ((pyv[1] > oyv[0]) and (pyv[1] < oyv[1])):
            print("Collision")

# def calculate_points(rect: pygame.rect.Rect):
#     points = []
#
#     cmds = ['rect.topleft', 'rect.topright', 'rect.bottomleft', 'rect.bottomright',	'rect.midleft', 'rect.midright',
#             'rect.midtop', 'rect.midbottom']
#     for cmd in cmds:
#         x = eval(cmd)
#         points.append(x)
#
#     points.append((rect.centerx, rect.centery))
#     return points


while True:
    DISPLAYSURF.fill(black)

    DISPLAYSURF.blit(sprite, (spritex, spritey))
    r = pygame.Rect(30,30,60,60)
    x = pygame.draw.rect(DISPLAYSURF, white, r)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if (event.key == pygame.K_LEFT):
                sprite=pygame.image.load('left.jpg')
            elif (event.key == pygame.K_RIGHT):
                sprite=pygame.image.load('right.jpg')
            elif (event.key == pygame.K_UP):
                sprite=pygame.image.load('up.jpg')
            elif (event.key == pygame.K_DOWN):
                sprite=pygame.image.load('down.jpg')

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_LEFT]:
        spritex -= 5

    if keys_pressed[pygame.K_RIGHT]:
        spritex += 5

    if keys_pressed[pygame.K_UP]:
        spritey -= 5

    if keys_pressed[pygame.K_DOWN]:
        spritey += 5

    # sprite_points = calculate_points(sprite.get_rect())
    check_collision(r, spritex, spritey)

    # if x.colliderect(sprite.get_rect()):
    #     print("Collision Detected!")
    #     white = (255,0,0)
    # else:
    #     white = (255,255,255)

    pygame.display.update()
    fpsClock.tick(FPS)