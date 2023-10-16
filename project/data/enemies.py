import math
import pygame
from random import randint,choices
from data.settings import windowsizeX, windowsizeY
from data.settings import fps as onesecond
from data.creature import Creature
from data.items import Currency, Healing
from data.effects import Effect
from data.init_groups import *
from data.assets.images import *


class Enemy(Creature):
                
    def __init__(self,name,image,pos_x,pos_y,dir,speed=1,health=1,awareness=10,dmg=1):
        super().__init__(name,image,pos_x,pos_y,dir,speed,health,None,awareness)
        # pygame.sprite.Sprite.__init__(self,camera_group[0],enemies,collidables)
        self.status = {"walking":self.wander_dur, "standing":0, "attack_cooldown":0}
        self.hurt_cd_dur = 5
        self.targeting_dur = 2*onesecond
        self.dmg = dmg
        self.attackspeed = int(0.5*onesecond)
        # Add loot table to creature: item and chance to drop!
        self.loot_table = {"heart":40,"gold":10,"nothing":50}

        self.hurt_icon = wood_chips_icon


    def select_target(self,player):
        if self.target and self.target.alive() == False:
            self.target = None

        ##Prioritise targeting the player
        ##notice already checks for .alive()
        if self.notice(player):        
            self.target = player
            return
        
        #if Player is too far, find the closest friendly
        if self.target == None:

            #closest has 0: the distance, 1: the creature
            closest = [self.awareness+1,None]

            #npc = potential target, not a player
            for npc in friendlies:
                if self.notice(npc):
                    distance= math.dist( (npc.pos_x,npc.pos_y) , (self.pos_x,self.pos_y) )
                    if closest[0] > distance:
                        closest[0:1] = [distance,npc]

            # make the closest friendly the new target
            self.target = closest[1]       #a creature

            if self.target: print(f"{self.name} started targeting {self.target.name}!")
        #print(self.target)


######## OLD CODE!!!!!!!!!!
    # def collisions(self):
    #     #muista päivittää hitbox ennen ku testaat collisionit
    #     self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
        
    #     for group in collidables:

    #         if group == enemies:
    #             continue
            
    #         elif pygame.sprite.spritecollideany(self,group):
    #             #print(f"{self.name} got hit by {group}!")

    #             return True
    #         else:
    #             continue

        
    def interact(self,target):
        self.attack(target) #SIKE

    def attack(self,target):
        if self.status["attack_cooldown"] == 0:
            print(f"{self.name} attacked {target.name}!")
            target.hp_change(-self.dmg,self)
            self.status["attack_cooldown"] = self.attackspeed

            #effects
            attack = Effect("Enemy Attack",player_attack_icon,target.pos_x,target.pos_y,int(0.5*onesecond))
            attack.add(effectsgroup)
            attack.add(camera_group[0])

        self.status["attack_cooldown"] -= 1

        ##target doesnt despawn just stops being rendered
            
        #target.kill()
        #at least 0.5s cooldown after succesful hit
        #enemy attack cooldown in player function??

    def drop_loot(self):
        testitem = pygame.image.load("data/assets/gold_pile.png")
        testheart = pygame.image.load("data/assets/heart.png")
        loot = choices(list(self.loot_table.keys()),weights=self.loot_table.values(),k=1)
        # print(loot)
        if loot[0] == "heart":
            drop = Healing("Small Heal",testheart_icon,self.pos_x,self.pos_y,randint(1,5))
            drop.add(itemgroup)
            drop.add(camera_group[0])
        elif loot[0] == "gold":
            drop = Currency("Pile-o-Gold",testitem_icon,self.pos_x,self.pos_y,randint(10,50))
            drop.add(itemgroup)
            drop.add(camera_group[0])
        else:
            print("No loot this time!")


    def hp_change(self,change,source=None):
        super().hp_change(change,source)
        if self.health <= 0:
            self.drop_loot()

    def update(self,player):
        self.collisions()
        self.select_target(player)
        self.targeting()
        self.movement()
        

        if self.target in self.collidedwith:
            self.attack(self.target)

        self.status_update()

        # if self.collisions(groups) and self.target:
        #     self.attack(self.target)
        #self.attack(camera_group)
        
     
class Spy(Enemy):
    def __init__(self,name,image,pos_x,pos_y,dir,speed=1,health=1,awareness=50,dmg=4):
        super().__init__(name,image,pos_x,pos_y,dir,speed,health,awareness)
        self.wander_dur = int(0.2*onesecond)
        self.wait_dur = 3*onesecond + randint(-30,31)
        self.targeting_dur = 1*onesecond
        self.attackspeed = int(0.2*onesecond)
        self.status = {"walking":self.wander_dur, "standing":0, "attack_cooldown":0}
        self.loot_table = {"heart":100,"gold":0}
        self.dmg = dmg

    # def update(self, player):
    #     print(self.target)
    #     return super().update(player)
    # def update(self,player):
    #     self.collisions()
    #     self.select_target(player)
    #     self.targeting()
    #     self.movement(5) if self.target else self.movement()
        
    #     if self.target in self.collidedwith:
    #         self.attack(self.target)