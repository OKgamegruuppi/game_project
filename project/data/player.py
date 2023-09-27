import pygame
from data.creature import Creature
from data.settings import fps
import data.effects as effectmod
from data.init_groups import *

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

class Player(Creature):
    def __init__(self,name,image,pos_x,pos_y,dir,speed=5,health=10,target=None,awareness=0,dmg=1):
        super().__init__(name,image,pos_x,pos_y,dir,speed,health,target,awareness)     
        self.status={"attack_cooldown":0}
        self.dmg = dmg

        # Determine if player is moving in any direction
        self.move = {
            "up" : False,
            "down": False,
            "left": False,
            "right": False
        }

        # Turn spritesheet into individual list for each direction
        self.sheet = spritesheet(self.image,3,3)
        self.image_up = self.sheet[:3]
        self.image_down = self.sheet[6:]
        self.image_right = self.sheet[3:6]
        # For left direction, need to flip images
        self.image_left = []
        templeft = self.sheet[3:6]
        for element in templeft:
            self.image_left.append(pygame.transform.flip(element,True,False))
        # Set starting image
        self.image = self.image_down[0]
        # Walking counter for animation
        self.walking = 0

        # Build hitbox for player
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))

        # Attackspeed tells how long the attack cooldown is 
        # (using game loop fps as clock)     
        self.attackspeed = int(fps/3)
        self.attackhitbox = pygame.sprite.Sprite()
        self.attackhitbox.rect = self.rect

        # Player has an inventory, which is a list containing
        # Item objects. Starts empty.
        self.inventory = []

    def __str__(self):
        print(self.name)
        
    #Function to determine which element of walking to display.
    def walk_animation(self,direction):
        element = int((self.walking//(fps/3) % 2)+1)
        return direction[element]
    
    # Move player character if self.move == True
    # Check if moving causes a collision, if so, don't move!
    def movement(self):
        # If all movements are False, set self.walking  to 0
        # Also reset the sprite to standing frame depending on dir
        if all(value == False for value in self.move.values()):
            self.walking = 0
            if self.dir.x == 1 and self.dir.y == 0:
                self.image = self.image_right[0]
            if self.dir.x == -1 and self.dir.y == 0:
                self.image = self.image_left[0]
            if self.dir.x == 0 and self.dir.y == -1:
                self.image = self.image_up[0]
            if self.dir.x == 0 and self.dir.y == 1:
                self.image = self.image_down[0]   
        # If even one of hte movements is true, check for collision,
        # move if able, and change the sprite to walking frame
        else:
            if self.move["right"] == True:
                self.pos_x += self.speed
                self.rect = self.rect.move(self.speed,0)
                if self.collisions():
                    self.pos_x -= self.speed
                    self.rect = self.rect.move(-self.speed,0)
                else:
                    self.dir.xy = 1,0
                    self.image = self.walk_animation(self.image_right)
                    # print(self.dir.x,self.dir.y)
            if self.move["left"] == True:
                self.pos_x -= self.speed
                self.rect = self.rect.move(-self.speed,0)
                if self.collisions():
                    self.pos_x += self.speed
                    self.rect = self.rect.move(self.speed,0)
                else:
                    self.dir.xy = -1,0
                    self.image = self.walk_animation(self.image_left)
                    # print(self.dir.x,self.dir.y)
            if self.move["up"] == True:
                self.pos_y -= self.speed
                self.rect = self.rect.move(0,-self.speed)
                if self.collisions():
                    self.pos_y += self.speed
                    self.rect = self.rect.move(0,self.speed)
                else:
                    self.dir.xy = 0,-1
                    self.image = self.walk_animation(self.image_up)
                    # print(self.dir.x,self.dir.y)
            if self.move["down"] == True:
                self.pos_y += self.speed
                self.rect = self.rect.move(0,self.speed)
                if  self.collisions():
                    self.pos_y -= self.speed
                    self.rect = self.rect.move(0,-self.speed)
                else:
                    self.dir.xy = 0,1
                    self.image = self.walk_animation(self.image_down)
                    # print(self.dir.x,self.dir.y)
            # Increase self.walking, so that frames change!
            self.walking += 1

    # Attack all enemies in a hitbox in front of the player
    def attack(self):
        # Check if attack on cooldown, if not, attack!
        if self.status["attack_cooldown"] == 0:
            # Determine attack hitbox based on player direction
            self.attackhitbox.rect = self.rect.move(self.dir.x*self.rect.width,self.dir.y*self.rect.height)
            #print(self.rect)
            #print(self.attackhitbox.rect)
            # Check if any enemies in the attack hitbox
            self.targets = pygame.sprite.spritecollide(self.attackhitbox,enemies,False)
            # If targets found, deal damage to each, otherwise nothing happens
            attack_x = self.pos_x + self.dir.x*self.rect.width
            attack_y = self.pos_y + self.dir.y*self.rect.height
            if self.targets:
                for target in self.targets:
                    target.hp_change(-self.dmg,self)
                    attack = effectmod.Effect("Player Attack",effectmod.player_attack,attack_x,attack_y,self.attackspeed)
                    attack.add(effectsgroup)
                    attack.add(camera_group[0])
            else:
                print("Nothing to attack!")
                attack = effectmod.Effect("Player Attack",effectmod.player_attack,attack_x,attack_y,self.attackspeed)
                attack.add(effectsgroup)
                attack.add(camera_group[0])
            # Clear target list
            self.targets = None
            # Start attack cooldown
            self.status["attack_cooldown"] += 1
        else:
            print("Attack on cooldown!")

    def check_inventory(self):
        if self.inventory:
            for item in self.inventory:
                print(item.name)
        else:
            print("Your Inventory is empty")

    def itempickup(self,target):
        pass

    def interact(self,target=None):
        print("Nothing to interact with!")
    
    # group = Groups of sprites that the player might collide with
    def update(self):
        # Check attack_cooldown, and reset or increase it if needed
        if self.status["attack_cooldown"] == self.attackspeed:
            self.status["attack_cooldown"] = 0
        elif self.status["attack_cooldown"] > 0:
            self.status["attack_cooldown"] += 1
        if self.status["attack_cooldown"] == 0:
            self.movement()      
        #pygame.draw.rect(screen,"#333333",self.hitbox)
        #screen.blit(self.image,(self.pos_x,self.pos_y))