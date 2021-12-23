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

player_image = pygame.image.load('Game\Assets\Sprites\Player.png')
player_location = [50, 50]
player_y_momentum = 0

grass_image = pygame.image.load('Game\grass.png') # loads grass
dirt_image = pygame.image.load('Game\dirt.png') # Loads dirt
TILE_SIZE = grass_image.get_width() # Gets width of grass

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

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

moving_right = False
moving_left = False

player_y_momentum = 0
air_timer = 0


playing = True # playing condition, will be used later on with multiple game states

player_rect = pygame.Rect(50, 50, player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100,100,100,50)

while playing: # game loop
    display.fill((146,244,255))

    tile_rects = []
    y = 0
    for row in game_map: 
        x = 0
        for tile in row:
            if tile == '1':
                display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '2':
                display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    player_movement = [0, 0] # initalises movement to 0 each tick
    if moving_right:
        player_movement[0] += 2 # sets movement to 2, player actually moves inside the move function
    if moving_left:
        player_movement[0] -= 2 # sets movement to 2
    player_movement[1] += player_y_momentum # incorporates gravity
    player_y_momentum += 0.2 # acceleration from gravity
    if player_y_momentum > 3: # if player is accelerating too fast
        player_y_momentum = 3 # limit acceleration

    player_rect, collisions = move(player_rect, player_movement, tile_rects)

    if collisions['bottom']:
        player_y_momentum = 0
        air_timer = 0
    else:
        air_timer += 1

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
                    player_y_momentum = -5 # As momentum is usually negative due to gravity this puts it up and at 5

        if event.type == KEYUP: # When key is released
            if event.key == K_RIGHT:

                moving_right = False  # No longer moving
            if event.key == K_LEFT:

                moving_left = False # No longer moving

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0, 0))
    pygame.display.update() # update display
    clock.tick(60) # maintain 60 fps

