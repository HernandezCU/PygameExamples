import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

Length = 600
Width = 600

display = pygame.display.set_mode((Length, Width))

img = pygame.image.load("hsq.jpg")

while True:

    display.fill(white)

    display.blit(img, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            quit()

        pygame.display.update()

