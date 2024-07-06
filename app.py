import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time # Gives time in milliseconds, divides by 1,000 to get time in seconds, displays as an integer, and subtracts start time
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64)) # It expects a string, so we change current_time to an integer with f'{}'
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300: screen.blit(snail_surf,obstacle_rect)                
            else: screen.blit(fly_surf,obstacle_rect)                

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100] # this only copies each obstacle in the list if the x value is greater than -100 (aka, off the screen). This is called list comprehension.

        return obstacle_list
    else: return []

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50) # 2 arguments are font type, and font size
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/sky.png').convert() # .convert converts the image into something pygame can use more efficiently.
ground_surface = pygame.image.load('graphics/ground.png').convert()
# score_surf = test_font.render('My game', False, (64,64,64)) # 3 arguments: text, anti-aliasing, color
# score_rect = score_surf.get_rect(center = (400,50))


# Obstacles
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # adding _alpha after .convert to make the alpha (black/white) values transparent
fly_surf = pygame.image.load('graphics/fly/Fly1.png').convert_alpha()

obstacle_rect_list = []

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300)) # the .get_rect method draws a rectangle around the surface
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Runner',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,340))

# Timer
obstacle_timer = pygame.USEREVENT + 1 # Have to add + 1 to the event because USEREVENT has reserved events in pygame
pygame.time.set_timer(obstacle_timer,1500) # 2 arguments: event to trigger, and how often to trigger it (in milliseconds)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type== pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            if randint(0,2): # will give a value of 0 or 1. 0 will be false, 1 will be true.
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100),300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100),210)))

    if game_active:
        screen.blit(sky_surface, (0,0)) # blit: block image transfer, aka putting one surface on another surface.
        screen.blit(ground_surface, (0,300))
        # pygame.draw.rect(screen,'#c0e8ec',score_rect) # tells pygame we're going to draw something, then the type of shape, then put in 3 arguments: surface to draw on, color, and the rectangle we want to draw. You can add in a 4th and 5th argument for width and border radius.
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        # screen.blit(score_surf, (score_rect))
        score = display_score()

        # snail_rect.x -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surf,snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # Collision
        game_active = collisions(player_rect,obstacle_rect_list)
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear() # clears the enemies after a collision for a proper restart

        score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name,game_name_rect)

        if score == 0: screen.blit(game_message,game_message_rect)            
        else: screen.blit(score_message,score_message_rect)            


    pygame.display.update()
    clock.tick(60)
    # this is telling the while loop not to run more than 60 times per second