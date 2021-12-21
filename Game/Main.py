import pygame, sys # import pygame and sys

clock = pygame.time.Clock() # set up the clock

from pygame.locals import * # import pygame modules
pygame.init() # initiate pygame

pygame.display.set_caption('Project Neon') # set the window name

WINDOW_SIZE = (600,400) # set up window size

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen

display = pygame.Surface((300, 200)) # Set up screen size

playing = True # playing condition, will be used later on with multiple game states

while playing:

    for event in pygame.event.get(): # checks for events
        if event.type == QUIT: # quits game and window
            pygame.quit()
            sys.exit()
    

    pygame.display.update() # updates screen, used for blitting and movement
    clock.tick(60) # sets framerate to 60
