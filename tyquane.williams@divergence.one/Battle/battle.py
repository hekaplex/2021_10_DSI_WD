import pygame

pygame.init()


# Game Window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')


# Load Images
# Background Image
background_img = pygame.image.load('Assets/Battle/Background/background.png').convert_alpha()

# Function for drawing background
def draw_bg():
    screen.blit(background_img, (0, 0))


run = True
while run:

    # Draw Background
    draw_bg()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()










