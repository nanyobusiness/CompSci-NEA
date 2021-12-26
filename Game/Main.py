#Libraries
import pygame, sys # import pygame and sys
from pygame.locals import * # import pygame modules

pygame.init() # initiate pygame

#Pygame main variables
pygame.display.set_caption('Project Neon') # set the window name
clock = pygame.time.Clock() # set up the clock
WINDOW_SIZE = (600,400) # set up window size
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen
display = pygame.Surface((300, 200)) # Set up screen size

player_image = pygame.image.load('Game\Assets\Sprites\Player_50.png')
player_location = [50, 50]
player_momentum = [0, 0]

enemy1_image = pygame.image.load('Game\Assets\Sprites\EnemyOne.png')
enemy1_location = [50, 50]
enemy1_momentum = [0,0]

grass_image = pygame.image.load('Game\Assets\Map\grass.png') # loads grass
dirt_image = pygame.image.load('Game\Assets\Map\dirt.png') # Loads dirt
TILE_SIZE = grass_image.get_width() # Gets width of grass

scroll = [0, 0]

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']]

def collision_test(rect, tiles):
    hit_list = [] # list of tiles that have collided
    for tile in tiles: # checks all tiles in list 
        if rect.colliderect(tile): # if that rect has collided with the tile
            hit_list.append(tile) # add the tile to the hit list
    return hit_list # return the list of tiles that have undergone collisions

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False} # the side on which the tile has collided
    rect.x += movement[0] # move the rect on the x axis
    hit_list = collision_test(rect, tiles) # perform collision check only on X axis (this makes it easier to process and avoid glitches)
    for tile in hit_list:
        if movement[0] > 0: # if movement was to the right
            rect.right = tile.left # align my objects/sprites so that they aren't inside each other
            collision_types['right'] = True # set right collision to true
        elif movement[0] < 0: # if movement was to the left
            rect.left = tile.right # align my items, similar to above
            collision_types['left'] = True # set left collision to true
    rect.y += movement[1] # move the rect on its y axis
    hit_list = collision_test(rect, tiles) # perform collision check only on Y axis
    for tile in hit_list:
        if movement[1] > 0: # if movement was upwards
            rect.bottom = tile.top # align items
            collision_types['bottom'] = True # the player must've hit the bottom of an object if any collision happened
        elif movement[1] < 0: # if movement was downward
            rect.top = tile.bottom # align items
            collision_types['top'] = True # it must've landed on top of an object so top collision is true
    return rect, collision_types

def xmomentum_stabilise(momentum):
    if momentum < 0.4 and momentum > -0.4: # sets momentum to 0 after its close enough
        momentum = 0
    elif momentum < 0: # increments/decrements momentum such that it slowly nears 0
        momentum += 0.4
    elif momentum > 0:
        momentum -= 0.4
    return momentum

moving_right = False
moving_left = False

player_momentum[1] = 0
air_timer = 0


playing = True # playing condition, will be used later on with multiple game states

player_rect = pygame.Rect(50, 50, player_image.get_width(), player_image.get_height())
enemy1_rect = pygame.Rect(100, 50, enemy1_image.get_width(), enemy1_image.get_height())
test_rect = pygame.Rect(100,100,100,50)

while playing: # game loop
    display.fill((146,244,255))

    scroll[0] += (player_rect.x-scroll[0]-120) # move the scroll by the difference of the player and 0,0 on the X
    scroll[1] += (player_rect.y-scroll[1]-86) # move the scroll by the difference of the player and 0,0 on the Y



    tile_rects = []
    y = 0
    for row in game_map: # for each individual list in the compound list
        x = 0
        for tile in row: # for each item in the individual list
            # scroll is subtracting so that all tiles in the screen move by the characters position, giving the illusion that the camera is following the player when really the tiles are just moving on the screen.
            if tile == '1': # if game item is 1, render dirt tile of according width 
                display.blit(dirt_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))  
            if tile == '2': # if game item is 2, render grass tile of according width
                display.blit(grass_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
            if tile != '0': # if game item is 0, render nothing
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    player_movement = [0, 0] # initalises movement to 0 each tick
    if moving_right:
        player_movement[0] += 2 # sets movement to 2, player actually moves inside the move function
    if moving_left:
        player_movement[0] -= 2 # sets movement to 2
    player_movement[1] += player_momentum[1] # incorporates gravity
    player_momentum[1] += 0.2 # acceleration from gravity
    if player_momentum[1] > 3: # if player is accelerating too fast
        player_momentum[1] = 3 # limit acceleration

    enemy1_movement = [0, 0] # initalises movement to 0 each tick
    enemy1_movement[1] += enemy1_momentum[1] # incorporates gravity
    enemy1_momentum[1] += 0.4
    if enemy1_momentum[1] > 4:
        enemy1_momentum[1] = 4 # sets max acceleration
    if player_rect[0] > enemy1_rect[0]: # sets movement based on where the player is
        enemy1_movement[0] += 1
    else:
        enemy1_movement[0] -= 1
    
    if player_rect.colliderect(enemy1_rect): # function to test for collisions between two rects
        player_momentum[1] = -3 # sets the players momentum to push them into the air
        if player_rect[0] - 20 < enemy1_rect[0]: # if the player is on the left of the enemy
            player_momentum[0] -= 2 # send player leftward
            enemy1_momentum[0] += 4 # send enemy rightward
        else:
            player_momentum[0] += 2 # send player rightward
            enemy1_momentum[0] -= 4 # send enemy leftward

    player_momentum[0] = xmomentum_stabilise(player_momentum[0])
    player_movement[0] += player_momentum[0] # add momentum
    enemy1_momentum[0] = xmomentum_stabilise(enemy1_momentum[0])
    enemy1_movement[0] += enemy1_momentum[0] # add momentum

    enemy1_rect, enemy1_collisions = move(enemy1_rect, enemy1_movement, tile_rects)

    if enemy1_collisions['bottom']:
        enemy1_momentum[0] = 0

    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions['bottom']:
        player_momentum[1] = 0
        air_timer = 0
    else:
        air_timer += 1

    display.blit(enemy1_image, (enemy1_rect[0]-scroll[0], enemy1_rect[1]-scroll[1]))
    display.blit(player_image, (player_rect.x-scroll[0], player_rect.y-scroll[1]))
    

    for event in pygame.event.get(): # checks for events
        if event.type == QUIT: # quits game and window
            pygame.quit() # stop pygame
            sys.exit() # stop script
        if event.type == KEYDOWN: # If a key is put down
            if event.key == K_RIGHT: # If the key is right arrow
                moving_right = True 

            if event.key == K_LEFT: # If the key is left arrow
                moving_left = True

            if event.key == K_UP: # If the key is up arrow
                if air_timer < 6:
                    player_momentum[1] = -5 # As momentum is usually negative due to gravity this puts it up and at 5

        if event.type == KEYUP: # When key is released
            if event.key == K_RIGHT:

                moving_right = False  # No longer moving
            if event.key == K_LEFT:

                moving_left = False # No longer moving

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update() # update display
    clock.tick(60) # maintain 60 fps

