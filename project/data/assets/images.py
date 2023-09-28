import pygame

# Creature Assets:
marcos_icon = pygame.image.load("data/assets/slime_monster_spritesheet.png")
cat_icon = pygame.image.load("data/assets/quest-cat.png")
defaultEnemy_icon2 = pygame.image.load("data/assets/Light_balls_tree.png")
spywillow_icon = pygame.image.load("data/assets/Spy_Willow.png")

# Item assets
testitem_icon = pygame.image.load("data/assets/gold_pile.png")
testheart_icon = pygame.image.load("data/assets/heart.png")
quest_icon = pygame.image.load("data/assets/cat-collectible.png")

# Effect assets
player_attack_icon = pygame.image.load("data/assets/attack.png")
blood_red_icon = pygame.image.load("data/assets/blood_red1.png")
small_heart_icon = pygame.image.load("data/assets/small_heart.png")

# Map assets
willow_icon = pygame.image.load('data/assets/safe_Willow.png')

# UI assets 
health_anim_icon = [pygame.image.load("data/assets/hp/healthbar-00.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-01.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-02.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-03.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-04.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-05.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-06.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-07.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-08.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-09.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-10.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-11.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-12.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-13.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-14.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-15.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-16.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-17.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-18.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-19.png"), 	\
                    pygame.image.load("data/assets/hp/healthbar-20.png"), 	]

                    
            #          pygame.image.load("data/assets/hp/1.png"),
            #   pygame.image.load("data/assets/hp/2.png"), pygame.image.load("data/assets/hp/3.png"),
            #   pygame.image.load("data/assets/hp/4.png"), pygame.image.load("data/assets/hp/4.png"),
            #   pygame.image.load("data/assets/hp/6.png")]

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