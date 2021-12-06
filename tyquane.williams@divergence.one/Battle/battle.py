from os import truncate
import pygame
import random
import button # This is being imported from the button.py file in the Battle folder

pygame.init()

clock = pygame.time.Clock()
fps = 60

# Game Window
bottom_panel = 150 # This will represent the area that the bottom pictures takes up
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')


# Define Game Variables
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90
attack = False
potion = False
potion_effect = 15
clicked = False
game_over = 0

# Define Fonts
font = pygame.font.SysFont('Times New Roman', 26)

# Define Colors
red = (255, 0, 0)
green = (0, 255, 0)

# Load Images
# Background Image
background_img = pygame.image.load('Assets/Battle/Background/background.png').convert_alpha()
# Panel Image
panel_img = pygame.image.load('Assets/Battle/Icons/panel.png').convert_alpha()
# Button Image
potion_img = pygame.image.load('Assets/Battle/Icons/potion.png').convert_alpha()
restart_img = pygame.image.load('Assets/Battle/Icons/restart.png').convert_alpha()
# Load Victory and Defeat Image
victory_img = pygame.image.load('Assets/Battle/Icons/victory.png').convert_alpha()
defeat_img = pygame.image.load('Assets/Battle/Icons/defeat.png').convert_alpha()
# Sword Image
sword_img = pygame.image.load('Assets/Battle/Icons/sword.png').convert_alpha()


# Create Function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# Function for drawing background
def draw_bg():
    screen.blit(background_img, (0, 0))


# Function for drawing panel
def draw_panel():
    # Draw Panel Rectangle
    screen.blit(panel_img, (0, screen_height - bottom_panel))
    # Show Knight Stats
    draw_text(f'{knight.name} HP: {knight.hp}', font, red, 100, screen_height - bottom_panel +  10)
    for count, i in enumerate(bandit_list):
        # Show name and health
        draw_text(f'{i.name} HP: {i.hp}', font, red, 550, (screen_height - bottom_panel + 10) + count * 60)



# Fighter Class
class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions): # This is where you define the class
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_portions = potions
        self.potions = potions
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
        # Load Hurt Images
        temp_list = []
        for i in range(3): # The number of images in list equals 3 but you can change that depending on the amount of images you want cycled through in the actual folder
            img = pygame.image.load(f'Assets/Battle/{self.name}/Hurt/{i}.png') # {self.name} is the class for the Knight images located in the Assets/Battle/Knight. f is needed
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        # Load Death Images
        temp_list = []
        for i in range(10): # The number of images in list equals 10 but you can change that depending on the amount of images you want cycled through in the actual folder
            img = pygame.image.load(f'Assets/Battle/{self.name}/Death/{i}.png') # {self.name} is the class for the Knight images located in the Assets/Battle/Knight. f is needed
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
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.idle()


    def idle(self):
        # Set variables to idle animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def attack(self, target):
        # Deal damage to enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        # Check if target has died
        target.hurt()
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.death()
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)
        # Set variables to attack animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def hurt(self):
        # Set variables to hurt animation
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def death(self):
        # Set variables to death animation
        self.action = 3
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()


    def reset(self):
        self.alive = True
        self.potions = self.start_portions
        self.hp = self.max_hp
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()


    def draw(self):
        screen.blit(self.image, self.rect)



class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp


    def draw(self, hp):
        # Update with new health
        self.hp = hp
        # Calculate Health Ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0


    def update(self):
        # Move Damage Text Up
        self.rect.y -= 1
        # Delete The Text After A Few Seconds
        self.counter += 1
        if self.counter > 30:
            self.kill()


damage_text_group = pygame.sprite.Group()



knight = Fighter(200, 260, 'Knight', 30, 10, 3) # This is where you can alter Knight's attributes: Fighter(x, y, name, max_hp, strength, potions)
bandit1 = Fighter(550, 270, 'Bandit', 15, 7, 1) # This is where you can alter Bandit1's attributes: Fighter(x, y, name, max_hp, strength, potions)
bandit2 = Fighter(700, 270, 'Bandit', 15, 7, 1) # This is where you can alter Bandit2's attributes: Fighter(x, y, name, max_hp, strength, potions)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

knight_health_bar = HealthBar(100, screen_height - bottom_panel + 40, knight.hp, knight.max_hp)
bandit1_health_bar = HealthBar(550, screen_height - bottom_panel + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = HealthBar(550, screen_height - bottom_panel + 100, bandit2.hp, bandit2.max_hp)

# Create Buttons
potion_button = button.Button(screen, 100, screen_height - bottom_panel + 70, potion_img, 64, 64)
restart_button = button.Button(screen, 330, 120, restart_img, 120, 30)


run = True
while run:

    clock.tick(fps)

    # Draw Background
    draw_bg()

    # Draw Panel
    draw_panel()
    knight_health_bar.draw(knight.hp)
    bandit1_health_bar.draw(bandit1.hp)
    bandit2_health_bar.draw(bandit2.hp)


    # Draw Fighters
    knight.update()
    knight.draw()
    for bandit in bandit_list:
        bandit.update()
        bandit.draw()

    # Draw The Damage Text
    damage_text_group.update()
    damage_text_group.draw(screen)

    # Control Action Variables
    # Reset Action Variables
    attack = False
    potion = False
    target = None
    # Make sure mouse id visible
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()
    for count, bandit in enumerate(bandit_list):
        if bandit.rect.collidepoint(pos):
            # Hide Mouse
            pygame.mouse.set_visible(False)
            # Show Sword in plce of mouse cursor
            screen.blit(sword_img, pos)
            if clicked == True and bandit.alive == True:
                attack = True
                target = bandit_list[count]
    if potion_button.draw():
        potion = True
    # Show number of potions remaining
    draw_text(str(knight.potions), font, red, 150, screen_height - bottom_panel + 70)


    if game_over == 0:
        # Player Action
        if knight.alive == True:
            if current_fighter == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    # Look For Player action
                    # Attack
                    if attack == True and target != None:
                        knight.attack(target) # This is who is being attacked. This is choosen by who the Player has clicked on.
                        current_fighter += 1
                        action_cooldown = 0
                    # Potion
                    if potion == True:
                        if knight.potions > 0:
                            # Check if the potion would heal the Player beyond max health
                            if knight.max_hp - knight.hp > potion_effect:
                                heal_amount = potion_effect
                            else:
                                heal_amount = knight.max_hp - knight.hp
                            knight.hp += heal_amount
                            knight.potions -= 1
                            damage_text = DamageText(knight.rect.centerx, knight.rect.y, str(heal_amount), green)
                            damage_text_group.add(damage_text)
                            current_fighter += 1
                            action_cooldown = 0
        else:
            game_over = -1                

        # Enemy Action
        for count, bandit in enumerate(bandit_list):
            if current_fighter == 2 + count:
                if bandit.alive == True:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        # Check if bandit needs to heal first
                        if (bandit.hp / bandit.max_hp) < 0.5 and bandit.potions > 0:
                            # Check if the potion would heal the Bandit beyond max health
                            if bandit.max_hp - bandit.hp > potion_effect:
                                heal_amount = potion_effect
                            else:
                                heal_amount = bandit.max_hp - bandit.hp
                            bandit.hp += heal_amount
                            bandit.potions -= 1
                            damage_text = DamageText(bandit.rect.centerx, bandit.rect.y, str(heal_amount), green)
                            damage_text_group.add(damage_text)
                            current_fighter += 1
                            action_cooldown = 0
                        # Attack
                        else:
                            bandit.attack(knight)
                            current_fighter += 1
                            action_cooldown = 0
                else:
                    current_fighter += 1

        # If all fighters have had a turn then reset
        if current_fighter > total_fighters:
            current_fighter = 1


    # Check if all of the Bandits are dead
    alive_bandits = 0
    for bandit in bandit_list:
        if bandit.alive == True:
            alive_bandits += 1
    if alive_bandits == 0:
        game_over = 1


    # Check if game is over
    if game_over != 0:
        if game_over == 1:
            screen.blit(victory_img, (250, 50))
        if game_over == -1:
            screen.blit(defeat_img, (290, 50))
        if restart_button.draw():
            knight.reset()
            for bandit in bandit_list:
                bandit.reset()
            current_fighter = 1
            action_cooldown
            game_over = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False

    pygame.display.update()

pygame.quit()









