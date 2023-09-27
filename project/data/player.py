import pygame
from data.creature import Creature
from data.settings import fps
import data.effects as effectmod
from data.init_groups import *

class Player(Creature):
    def __init__(self,name,image,pos_x,pos_y,dir,speed=5,health=10,target=None,status={"attack_cooldown":0},awareness=0,dmg=1):
        super().__init__(name,image,pos_x,pos_y,dir,speed,health,target,status,awareness)     
        self.dmg = dmg

        # Determine if player is moving in any direction
        self.move = {
            "up" : False,
            "down": False,
            "left": False,
            "right": False
        }
        self.image_up = self.image.subsurface(pygame.Rect(0,0,24,24))
        self.image_down = self.image.subsurface(pygame.Rect(0,48,24,24))
        self.image_left = pygame.transform.flip(self.image.subsurface(pygame.Rect(0,24,24,24)),True,False)
        self.image_right = self.image.subsurface(pygame.Rect(0,24,24,24))
        self.image = self.image_down
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
        # Attackspeed tells how long the attack cooldown is (using game loop fps as clock)        
        self.attackspeed = int(fps/3)
        self.attackhitbox = pygame.sprite.Sprite()
        #self.attackimage = pygame.image.load("data/assets/blood_red1.png").convert_alpha()
        #self.attackhitbox = Effect("Attack",hiticon,0,0,int(fps/3))
        self.attackhitbox.rect = self.rect

    def __str__(self):
        print(self.name)
        
    # Move player character if self.move == True
    # Check if moving causes a collision, if so, don't move!
    def movement(self):
        if self.move["right"] == True:
            self.pos_x += self.speed
            self.rect = self.rect.move(self.speed,0)
            if self.collisions():
                self.pos_x -= self.speed
                self.rect = self.rect.move(-self.speed,0)
            else:
                self.dir.xy = 1,0
                self.image = self.image_right
                # print(self.dir.x,self.dir.y)
        if self.move["left"] == True:
            self.pos_x -= self.speed
            self.rect = self.rect.move(-self.speed,0)
            if self.collisions():
                self.pos_x += self.speed
                self.rect = self.rect.move(self.speed,0)
            else:
                self.dir.xy = -1,0
                self.image = self.image_left
                # print(self.dir.x,self.dir.y)
        if self.move["up"] == True:
            self.pos_y -= self.speed
            self.rect = self.rect.move(0,-self.speed)
            if self.collisions():
                self.pos_y += self.speed
                self.rect = self.rect.move(0,self.speed)
            else:
                self.dir.xy = 0,-1
                self.image = self.image_up
                # print(self.dir.x,self.dir.y)
        if self.move["down"] == True:
            self.pos_y += self.speed
            self.rect = self.rect.move(0,self.speed)
            if self.collisions():
                self.pos_y -= self.speed
                self.rect = self.rect.move(0,-self.speed)
            else:
                self.dir.xy = 0,1
                self.image = self.image_down
                # print(self.dir.x,self.dir.y)

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
            if self.targets:
                for target in self.targets:
                    target.hp_change(-self.dmg)
                    attack = effectmod.Effect("Player Attack",effectmod.player_attack,target.pos_x,target.pos_y,self.attackspeed)
                    attack.add(effectsgroup)
                    attack.add(camera_group[0])
            else:
                print("Nothing to attack!")
                attack_x = self.pos_x + self.dir.x*self.rect.width
                attack_y = self.pos_y + self.dir.y*self.rect.height
                attack = effectmod.Effect("Player Attack",effectmod.player_attack,attack_x,attack_y,self.attackspeed)
                attack.add(effectsgroup)
                attack.add(camera_group[0])
            # Clear target list
            self.targets = None
            # Start attack cooldown
            self.status["attack_cooldown"] += 1
        else:
            print("Attack on cooldown!")

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