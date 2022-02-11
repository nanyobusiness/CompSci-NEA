#Libraries
from turtle import back
import pygame, sys # import pygame and sys
from pygame.locals import * # import pygame modules

pygame.init() # initiate pygame
pygame.font.init() 



#Pygame main variables
pygame.display.set_caption('Project Neon') # set the window name
clock = pygame.time.Clock() # set up the clock
WINDOW_SIZE = (600,400) # set up window size
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen
display = pygame.Surface((300, 200)) # Set up screen size

background = pygame.image.load('Assets\Backgrounds\Start.png')
menuborder = pygame.image.load('Assets\Backgrounds\MenuBorder.png')
font = pygame.font.Font('Assets\Fonts\ThaleahFat_TTF.ttf', 15)
back_arrow = pygame.image.load('Assets\Icons\Backarrow.png')

player_image = pygame.image.load('Assets\Sprites\Player_50.png')
player_location = [50, 50]
player_momentum = [0, 0]

playerattacking = False
attacktimer = 10
cooldown = 0

enemy1_image = pygame.image.load('Assets\Sprites\EnemyOne.png')
enemy1_location = [50, 50]
enemy1_momentum = [0,0]

top_image = pygame.image.load('Assets\Map\purpletop.png') # loads tile
underground_image = pygame.image.load('Assets\Map\stone.png') # Loads tile
bottomleft_image = pygame.image.load('Assets\Map\BottomLeft.png')
righttop_image = pygame.image.load('Assets\Map\RightTop.png')
bottomright_image = pygame.image.load('Assets\Map\BottomRight.png')
lefttop_image = pygame.image.load('Assets\Map\LeftTop.png')
left_image = pygame.image.load('Assets\Map\left.png')
right_image = pygame.image.load('Assets\Map\Right.png')

runloop = ['Assets\Sprites\RunLoop\item1.png', 'Assets\Sprites\RunLoop\item2.png', 'Assets\Sprites\RunLoop\item3.png', 'Assets\Sprites\RunLoop\item4.png', 'Assets\Sprites\RunLoop\item5.png', 'Assets\Sprites\RunLoop\item6.png']
swingloop = ['Assets\Sprites\SwingLoop\item1.png', 'Assets\Sprites\SwingLoop\item1.png',  'Assets\Sprites\SwingLoop\item2.png', 'Assets\Sprites\SwingLoop\item2.png',  'Assets\Sprites\SwingLoop\item3.png', 'Assets\Sprites\SwingLoop\item3.png',  'Assets\Sprites\SwingLoop\item4.png', 'Assets\Sprites\SwingLoop\item4.png',  'Assets\Sprites\SwingLoop\item5.png', 'Assets\Sprites\SwingLoop\item5.png',  'Assets\Sprites\SwingLoop\item6.png', 'Assets\Sprites\SwingLoop\item6.png'] 
runningcount = 0
swingcount = 0

TILE_SIZE = top_image.get_width() # Gets width of tile

heart_image = pygame.image.load('Assets\Icons\heart.png') # Loads lives icon
lives = 5
enemydamage = 0

scroll = [0, 0]

game_map = [['5', '3', '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '5', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '8', '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '4', '3', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '8', '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '1', '4', '3', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '8', '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '1', '1', '8', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '8', '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '1', '1', '8', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '8', '0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '5', '6', '1', '1', '8', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '4', '2','2','2','3','0','0','0','0','0','0','0','0','0','0','0','0','0','5','2','2', '3', '0', '0', '0', '0', '0', '0', '0', '0', '5', '6', '1', '1', '1', '8', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '1', '1','1','1','4','2','2','2','2','2','2','2','2','2','2','2','2','2','6','1','1', '4', '2', '2', '2', '2', '2', '2', '2', '2', '6', '1', '1', '1', '1', '8', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '1', '1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '8', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '1', '1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '8', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '1', '1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '8', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '1', '1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '8', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '1', '1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '8', '0', '0', '0', '0', '0', '0', '0', '0']]

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
    if momentum < 0.2 and momentum > -0.2: # sets momentum to 0 after its close enough
        momentum = 0
    elif momentum < 0: # increments/decrements momentum such that it slowly nears 0
        momentum += 0.2
    elif momentum > 0:
        momentum -= 0.2
    return momentum

moving_right = False
moving_left = False

player_momentum[1] = 0
air_timer = 0

player_rect = pygame.Rect(50, -20, player_image.get_width(), player_image.get_height())
enemy1_rect = pygame.Rect(300, 50, enemy1_image.get_width(), enemy1_image.get_height())
test_rect = pygame.Rect(100,100,100,50)

while 1:
    end = False
    playing = False
    keybinds = False
    while 1:
        display.blit(background, (0,0))
        display.blit(menuborder, (0, 0))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get(): # checks for events
            if event.type == QUIT: # quits game and window
                pygame.quit() # stop pygame
                sys.exit() # stop script-
            if event.type == pygame.MOUSEBUTTONDOWN:
                if keybinds == False:
                    if 50 < mouse[0] < 230 and 120 < mouse[1] < 160:
                        playing = True
                    if 50 < mouse[0] < 250 and 200 < mouse[1] < 240:
                        keybinds = True
                else:
                    if 10 < mouse[0] < 40 and 10 < mouse[1] < 40:
                        keybinds = False

        if keybinds:
            display.blit(back_arrow, (8, 8))

            pygame.draw.rect(display, (56,28,84), [25, 60, 90, 65])
            pygame.draw.rect(display, (140,84,156), [25, 60, 90, 2])
            display.blit(font.render('Up = W/Space', True, (255,255,255)), (28, 65))
            display.blit(font.render('A = Left', True, (255,255,255)), (28, 80))
            display.blit(font.render('D = Right', True, (255,255,255)), (28, 95))
            display.blit(font.render('J = Attack', True, (255,255,255)), (28, 110))
        else:
            if 50 < mouse[0] < 230 and 120 < mouse[1] < 160:
                pygame.draw.rect(display, (140,84,156), [25, 60, 90, 20]) 
            else:
                pygame.draw.rect(display, (56,28,84), [25, 60, 90, 20])
            pygame.draw.rect(display, (140,84,156), [25, 60, 90, 2])
            display.blit(font.render('Start Game', True, (255,255,255)), (30, 65))

            if 50 < mouse[0] < 250 and 200 < mouse[1] < 240:
                pygame.draw.rect(display, (140,84,156), [25, 100, 100, 20]) 
            else:
                pygame.draw.rect(display, (56,28,84), [25, 100, 100, 20])
            pygame.draw.rect(display, (140,84,156), [25, 100, 100, 2])
            display.blit(font.render('Show Keybinds', True, (255,255,255)), (30, 105))


        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))
        pygame.display.update() # update display
        clock.tick(60) # maintain 60 fps   

        if playing == True:
            score = 0
            gameclock = 0
            break
    lives = 5
    pause = False
    lifecooldown = 0
    damagecooldown = 0

    while playing: # game loop

        damagecooldown += 1
        lifecooldown += 1
        gameclock += 1
        display.fill((82, 40, 112))

        scroll[0] += (player_rect.x-scroll[0]-120) # move the scroll by the difference of the player and 0,0 on the X
        scroll[1] += (player_rect.y-scroll[1]-86) # move the scroll by the difference of the player and 0,0 on the Y



        tile_rects = []
        y = 0
        for row in game_map: # for each individual list in the compound list
            x = 0
            for tile in row: # for each item in the individual list
                # scroll is subtracting so that all tiles in the screen move by the characters position, giving the illusion that the camera is following the player when really the tiles are just moving on the screen.
                if tile == '1': # if game item is 1, render this tile of according width 
                    display.blit(underground_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))  
                if tile == '2': # if game item is 2, render this tile of according width
                    display.blit(top_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                if tile == '3':
                    display.blit(bottomleft_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                if tile == '4':
                    display.blit(righttop_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                if tile == '5':
                    display.blit(bottomright_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                if tile == '6':
                    display.blit(lefttop_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                if tile == '7':
                    display.blit(left_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
                if tile == '8':
                    display.blit(right_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))

                if tile != '0': # if game item is 0, render nothing
                    tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                x += 1
            y += 1

        # Health
        healthpos = -2
        for i in range(lives):
            healthpos += 7
            display.blit(heart_image, (healthpos, 5))

        display.blit(font.render(f'Hits Dealt: {enemydamage}', True, (255,255,255)), (60, 3))


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
        
        # COLLISIONS BETWEEN PLAYER AND ENEMY

        if player_rect.colliderect(enemy1_rect): # function to test for collisions between two rects
            if playerattacking:
                enemy1_momentum[1] = -3 # sets the enemy's momentum to push them into the air
                if player_rect[0] - 16 < enemy1_rect[0]: # if the player is on the left of the enemy
                    player_momentum[0] -= 1 # send player leftward
                    enemy1_momentum[0] += 5 # send enemy rightward
                else:
                    player_momentum[0] += 1 # send player rightward
                    enemy1_momentum[0] -= 5 # send enemy leftward
                if damagecooldown > 10:
                    enemydamage += 1
                    damagecooldown = 0 
            else:
                player_momentum[1] = -3 # sets the players momentum to push them into the air
                if player_rect[0] - 16 < enemy1_rect[0]: # if the player is on the left of the enemy
                    player_momentum[0] -= 2 # send player leftward
                    enemy1_momentum[0] += 4 # send enemy rightward
                else:
                    player_momentum[0] += 2 # send player rightward
                    enemy1_momentum[0] -= 4 # send enemy leftward
                if lifecooldown > 10:
                    lives -= 1 # LOSE A LIFE
                    lifecooldown = 0

        player_momentum[0] = xmomentum_stabilise(player_momentum[0])
        player_movement[0] += player_momentum[0] # add momentum
        enemy1_momentum[0] = xmomentum_stabilise(enemy1_momentum[0])
        enemy1_movement[0] += enemy1_momentum[0] # add momentum

        enemy1_rect, enemy1_collisions = move(enemy1_rect, enemy1_movement, tile_rects)

        if enemy1_collisions['bottom']:
            enemy1_momentum[0] = 0
        
        if enemy1_collisions['left'] or enemy1_collisions['right']:
            enemy1_momentum[1] = -3


        player_rect, collisions = move(player_rect, player_movement, tile_rects)

        if collisions['bottom']:
            player_momentum[1] = 0
            air_timer = 0
        else:
            air_timer += 1


        #Animations
        runningcount += 1
        file = runloop[runningcount // 7]
        if runningcount == 36:
            runningcount = 0
        if moving_left:
            player_image = pygame.image.load(file)
        if moving_right:
            player_image = pygame.transform.flip(pygame.image.load(file), True, False)

        if playerattacking:
            file = swingloop[swingcount]
            swingcount += 1
            if swingcount == 12:
                swingcount = 0
            if moving_left:
                player_image = pygame.image.load(file)
            else:
                player_image = pygame.transform.flip(pygame.image.load(file), True, False)



        display.blit(enemy1_image, (enemy1_rect[0]-scroll[0], enemy1_rect[1]-scroll[1]))
        display.blit(player_image, (player_rect.x-scroll[0], player_rect.y-scroll[1]))
        

        for event in pygame.event.get(): # checks for events
            if event.type == QUIT: # quits game and window
                pygame.quit() # stop pygame
                sys.exit() # stop script
            if event.type == KEYDOWN: # If a key is put down
                if event.key == K_d: # If the key is right arrow
                    player_image = pygame.transform.flip(player_image, True, False)
                    moving_right = True 

                if event.key == K_a: # If the key is left arrow
                    player_image = pygame.transform.flip(player_image, True, False)
                    moving_left = True

                if event.key == K_w or event.key == K_SPACE: # If the key is up arrow
                    if air_timer < 6:
                        player_momentum[1] = -5 # As momentum is usually negative due to gravity this puts it up and at 5

                if event.key == K_j:
                    if cooldown < 0:
                        playerattacking = True
                if event.key == K_ESCAPE:
                    pause = True

            if event.type == KEYUP: # When key is released
                if event.key == K_d:
                    player_image = pygame.transform.flip(player_image, True, False)
                    moving_right = False  # No longer moving
                if event.key == K_a:
                    player_image = pygame.transform.flip(player_image, True, False)
                    moving_left = False # No longer moving

        if playerattacking: # if player is attacking
            player_image = pygame.image.load('Assets\Sprites\Player_attack.png') # show attacking sprite and begin countdown
            attacktimer -= 1 
            if attacktimer < 1: # when countdown hits 0
                player_image = pygame.image.load('Assets\Sprites\Player_50.png') # show normal sprite and disable attacking state
                playerattacking = False
                attacktimer = 10
                cooldown = 45
        cooldown -= 1
            
        display.blit(font.render(f'Score: {round(score, 3)}', True, (255,255,255)), (200, 3))
        if gameclock % 10 == 0:
            score += (0.2*lives)/10
            display.blit(font.render(f'Score: {round(score, 3)}', True, (255,255,255)), (200, 3))

        if lives < 1:
            # Code for the end screen phase
            finalscore = score
            end = True
            break


## CODE FOR PAUSE PHASE


        while pause:
            display.fill((0,0,0))
            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get(): # checks for events
                if event.type == QUIT: # quits game and window
                    pygame.quit() # stop pygame
                    sys.exit() # stop script-
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 15 < mouse[0] < 55 and 15 < mouse[1] < 55:
                        pause = False
                        break

            display.blit(back_arrow, (8, 8))
            pygame.draw.rect(display, (35,21,48), [60, 60, 180, 65])
            pygame.draw.rect(display, (255,255,255), [60, 60, 180, 2])
            display.blit(font.render('Game is paused, press', True, (255,255,255)), (63, 75))
            display.blit(font.render('back arrow to resume.', True, (255,255,255)), (63, 100))

            surf = pygame.transform.scale(display, WINDOW_SIZE)
            screen.blit(surf, (0, 0))
            pygame.display.update() # update display
            clock.tick(60) # maintain 60 fps   


        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))
        pygame.display.update() # update display
        clock.tick(60) # maintain 60 fps











    playing = False
    fullscore = False
    while end:
        display.blit(background, (0,0))
        display.blit(menuborder, (0, 0))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get(): # checks for events
            if event.type == QUIT: # quits game and window
                pygame.quit() # stop pygame
                sys.exit() # stop script-
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 50 < mouse[0] < 230 and 120 < mouse[1] < 160:
                    pygame.quit()
                    sys.exit()
                if 50 < mouse[0] < 250 and 200 < mouse[1] < 240:
                    fullscore = True
                else: 
                    fullscore = False

        if 50 < mouse[0] < 230 and 120 < mouse[1] < 160:
            pygame.draw.rect(display, (140,84,156), [25, 60, 90, 20]) 
        else:
            pygame.draw.rect(display, (56,28,84), [25, 60, 90, 20])
        pygame.draw.rect(display, (140,84,156), [25, 60, 90, 2])
        display.blit(font.render('Quit', True, (255,255,255)), (30, 65))

        if fullscore:
            pygame.draw.rect(display, (56,28,84), [25, 100, 100, 20])
            display.blit(font.render(f'{round(finalscore, 10)}...', True, (255,255,255)), (30, 105))
        else:
            pygame.draw.rect(display, (56,28,84), [25, 100, 100, 20])
            display.blit(font.render(f'Score = {round(finalscore, 3)}', True, (255,255,255)), (30, 105))


        surf = pygame.transform.scale(display, WINDOW_SIZE)
        screen.blit(surf, (0, 0))
        pygame.display.update() # update display
        clock.tick(60) # maintain 60 fps   
