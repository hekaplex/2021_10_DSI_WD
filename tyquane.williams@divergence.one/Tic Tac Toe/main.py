# Part 1
import pygame
from pygame.locals import *

pygame.init()


screen_width = 300
screen_height = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')

run = True
while run:

    # Add Event Handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
pygame.quit()



#
#
#



# Part 2
#
#
#


# Part 3
#

#

# Reset Game
