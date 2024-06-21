import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/sky.png')
ground_surface = pygame.image.load('graphics/ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    # blit: block image transfer, aka putting one surface on another surface.
    pygame.display.update()
    clock.tick(60)
    # this is telling the while loop not to run more than 60 times per second