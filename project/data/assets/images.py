import pygame

# Creature Assets:
marcos_icon = pygame.image.load("data/assets/slime_monster_spritesheet.png")
cat1_icon = pygame.image.load("data/assets/Cat-sprite-stand.png")
defaultEnemy_icon2 = pygame.image.load("data/assets/TEST_Light_balls_tree1.png")

# Item assets
testitem_icon = pygame.image.load("data/assets/gold_pile.png")
testheart_icon = pygame.image.load("data/assets/heart.png")

# Effect assets
player_attack_icon = pygame.image.load("data/assets/attack.png")
blood_red_icon = pygame.image.load("data/assets/blood_red1.png")
small_heart_icon = pygame.image.load("data/assets/small_heart.png")

# UI assets 
health_anim_icon = [pygame.image.load("data/assets/hp/0.png"), pygame.image.load("data/assets/hp/1.png"),
              pygame.image.load("data/assets/hp/2.png"), pygame.image.load("data/assets/hp/3.png"),
              pygame.image.load("data/assets/hp/4.png"), pygame.image.load("data/assets/hp/4.png"),
              pygame.image.load("data/assets/hp/6.png")]

# Function to split a spritesheet into a list of individual images
def spritesheet(img,sprite_rows,sprite_cols):
    sheet = []
    sheetwidth = int(img.get_width())
    sheetheight = int(img.get_height())
    sheet_x = int(sheetwidth/sprite_cols)
    sheet_y = int(sheetheight/sprite_rows)
    for y in range(0,sheetheight,sheet_y):
        for x in range(0,sheetwidth,sheet_y):
            sheet.append(img.subsurface(pygame.Rect(x,y,sheet_x,sheet_y)))
    return sheet