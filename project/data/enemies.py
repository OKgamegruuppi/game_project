import math
import pygame
from random import randint,choice
from data.settings import windowsizeX, windowsizeY
from data.settings import fps as onesecond
from data.creature import Creature
import data.effects as effectmod
from data.init_groups import *


class Enemy(Creature):
                
    def __init__(self,name,image,pos_x,pos_y,dir,speed=1,health=0,target=None,awareness=1,dmg=1):
        super().__init__(name,image,pos_x,pos_y,dir,speed,health,target,awareness)
        self.status = {"walking":self.wander_dur, "standing":0, "attack_cooldown":0}
        self.dmg = dmg


    def select_target(self,player):
        if self.target and self.target.alive == False:
            self.target = None

        ##Prioritise targeting the player
        ##notice already checks for .alive
        if self.notice(player):        
            self.target = player
            print(f"{self.name} started targeting the player {self.target.name}!")
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
    ######### end select target ##########

    # def targeting(self):
    #     if (self.target is None) or (self.target.alive == False):
    #         if "targeting" in self.status: del self.status["targeting"]         #delete targeting status if target was removed elsewhere
    #         return


    #     if self.notice(self.target):
    #         self.status["targeting"] = math.floor(0.1 * self.awareness * onesecond)       #refresh targeting status if in notice range
    #         #better awareness = longer memory

    #     elif "targeting" in self.status:
    #         self.status["targeting"] -= 1
    #         if self.status["targeting"] == 0:
    #             del self.status["targeting"]       #clear status effect
    #             self.target = None                  #target is forgot



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
            target.hp_change(-1,self)
            self.status["attack_cooldown"] = int(0.2*onesecond)

            #effects
            attack = effectmod.Effect("Enemy Attack",effectmod.player_attack,target.pos_x,target.pos_y,int(0.5*onesecond))
            attack.add(effectsgroup)
            attack.add(camera_group[0])

        self.status["attack_cooldown"] -= 1

        ##target doesnt despawn just stops being rendered
            
        #target.kill()
        #at least 0.5s cooldown after succesful hit
        #enemy attack cooldown in player function??

    def update(self,player):
        self.collisions()
        self.select_target(player)
        self.targeting()
        self.movement()

        if self.target in self.collidedwith:
            self.attack(self.target)
        # if self.collisions(groups) and self.target:
        #     self.attack(self.target)
        #self.attack(camera_group)
        

