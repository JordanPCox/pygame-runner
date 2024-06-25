import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50)
# 2 arguments are font type, and font size

sky_surface = pygame.image.load('graphics/sky.png').convert()
# .convert converts the image into something pygame can use more efficiently.
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')
# 3 arguments: text, anti-aliasing, color

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# adding _alpha after .convert to make the alpha (black/white) values transparent
snail_x_pos = 600

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
# the .get_rect method draws a rectangle around the surface

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # blit: block image transfer, aka putting one surface on another surface.
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= 4
    if snail_x_pos < -100: snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))
    screen.blit(player_surf,player_rect)

    pygame.display.update()
    clock.tick(60)
    # this is telling the while loop not to run more than 60 times per second