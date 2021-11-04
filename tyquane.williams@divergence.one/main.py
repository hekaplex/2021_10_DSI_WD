import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False