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
score_surf = test_font.render('My game', False, (64,64,64))
# 3 arguments: text, anti-aliasing, color

score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# adding _alpha after .convert to make the alpha (black/white) values transparent
snail_rect = snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
# the .get_rect method draws a rectangle around the surface

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type== pygame.MOUSEMOTION:
        #     print(event.pos)

    # blit: block image transfer, aka putting one surface on another surface.
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    pygame.draw.rect(screen,'#c0e8ec',score_rect)
    # tells pygame we're going to draw something, then the type of shape, then put in 3 arguments: surface to draw on, color, and the rectangle we want to draw. You can add in a 4th and 5th argument for width and border radius.
    pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
    pygame.draw.ellipse(screen,'Brown',pygame.Rect(50,200,100,100))
    # Creating a rectangle within the method that takes 4 arguments: left, top, width, height
    screen.blit(score_surf, (score_rect))

    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
    # this is telling the while loop not to run more than 60 times per second