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
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 # This is where you can decide which motions the characters will do onscreen by cycling through that image folder 0: idle, 1: attack, 2: hurt, 3: dead
        self.update_time = pygame.time.get_ticks()
        # Load Idle Images
        temp_list = []
        for i in range(8): # The number of images in list equals 8 but you can change that depending on the amount of images you want cycled through in the actual folder
            img = pygame.image.load(f'Assets/Battle/{self.name}/Idle/{i}.png') # {self.name} is the class for the Knight images located in the Assets/Battle/Knight. f is needed
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        # Load Attack Images
        temp_list = []
        for i in range(8): # The number of images in list equals 8 but you can change that depending on the amount of images you want cycled through in the actual folder
            img = pygame.image.load(f'Assets/Battle/{self.name}/Attack/{i}.png') # {self.name} is the class for the Knight images located in the Assets/Battle/Knight. f is needed
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self):
        animation_cooldown = 100
        # Handle Animation
        # Update Image
        self.image = self.animation_list[self.action][self.frame_index]
        # Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # If the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
        


    def draw(self):
        screen.blit(self.image, self.rect)


knight = Fighter(200, 260, 'Knight', 30, 10, 3)
bandit1 = Fighter(550, 270, 'Bandit', 20, 6, 1)
bandit2 = Fighter(700, 270, 'Bandit', 20, 6, 1)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)


run = True
while run:

    clock.tick(fps)

    # Draw Background
    draw_bg()

    # Draw Panel
    draw_panel()

    # Draw Fighters
    knight.update()
    knight.draw()
    for bandit in bandit_list:
        bandit.update()
        bandit.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()










