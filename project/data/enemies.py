import math
import pygame
from random import randint,choice
from data.settings import windowsizeX, windowsizeY
from data.settings import fps as onesecond
from data.creature import Creature
import data.effects as effectmod
from data.init_groups import *


class Enemy(Creature):
                
    def __init__(self,name,image,pos_x,pos_y,dir,speed=1,health=0,target=None,status={"walking":20,"standing":0,"attack_cooldown":0},awareness=1,dmg=1):
        super().__init__(name,image,pos_x,pos_y,dir,speed,health,target,status,awareness)

        self.dmg = dmg


    def select_target(self,player):
        if self.target and self.target.alive == False:
            self.target = None

        ##Prioritise targeting the player
        ##notice already checks for .alive
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
    ######### end select target ##########

    def targeting(self):
        if self.target is None:
            if "targeting" in self.status: del self.status["targeting"]         #delete targeting status if target was removed elsewhere
            return


        if self.notice(self.target):
            self.status["targeting"] = math.floor(0.1 * self.awareness * onesecond)       #refresh targeting status if in notice range
            #better awareness = longer memory

        elif "targeting" in self.status:
            self.status["targeting"] -= 1
            if self.status["targeting"] == 0:
                del self.status["targeting"]       #clear status effect
                self.target = None                  #target is forgot


    def collisions(self,groups):
        #muista päivittää hitbox ennen ku testaat collisionit
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
        
        for group in grouplist:

            if group == enemies:
                continue
            
            elif pygame.sprite.spritecollideany(self,group):
                #print(f"{self.name} got hit by {group}!")

                return True
            else:
                continue

        
    def interact(self,target,groups):
        self.attack(target) #SIKE

    def attack(self,target):
        if pygame.sprite.collide_rect(self,target) and self.status["attack_cooldown"] == 0:
            target.hp_change(-1,effects)
            self.status["attack_cooldown"] = int(0.5*onesecond)
            print(f"{self.name} attacked {target.name}!")

            #effects
            attack = effectmod.Effect("Enemy Attack",effectmod.player_attack,target.pos_x,target.pos_y,int(0.5*onesecond))
            attack.add(effects)
            'attack.add(camera_group)'

        self.status["attack_cooldown"] -= 1

        ##target doesnt despawn just stops being rendered
            
        #target.kill()
        #at least 0.5s cooldown after succesful hit
        #enemy attack cooldown in player function??

    def update(self,player,groups):
        self.select_target(player)
        # if self.collisions(groups) and self.target:
        #     self.attack(self.target)
        self.movement(groups)
        #self.attack(camera_group)
        

