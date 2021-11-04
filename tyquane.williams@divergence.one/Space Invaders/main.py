import pygame

# Intialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 350
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))


# Game Loop
running = True
while running:
   
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



player()
pygame.display.update()
