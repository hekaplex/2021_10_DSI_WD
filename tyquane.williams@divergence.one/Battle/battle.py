import pygame

pygame.init()


# Game Window
screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()










