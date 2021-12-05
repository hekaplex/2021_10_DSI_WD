import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

# Game Window
bottom_panel = 150 # This will represent the area that the bottom pictures takes up
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')


# Load Images
# Background Image
background_img = pygame.image.load('Assets/Battle/Background/background.png').convert_alpha()
# Panel Image
panel_img = pygame.image.load('Assets/Battle/Icons/panel.png').convert_alpha()


# Function for drawing background
def draw_bg():
    screen.blit(background_img, (0, 0))


# Function for drawing panel
def draw_panel():
    screen.blit(panel_img, (0, screen_height - bottom_panel))



# Fighter Class
class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions): # This is where you define the class
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_portions = potions
        self.portions = potions
        self.alive = True
        self.image = pygame.image.load(f'Assets/Battle/{self.name}/Idle/0.png') # {self.name} is the class for the Knight images located in the Assets/Battle/Knight. f is needed
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def draw(self):
        screen.blit(self.image, self.rect)


knight = Fighter(200, 260, 'Knight', 30, 10, 3)



run = True
while run:

    clock.tick(fps)

    # Draw Background
    draw_bg()

    # Draw Panel
    draw_panel()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()










