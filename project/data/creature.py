import math
import pygame
from random import randint
from player import *

class Creature():
    def __init__(self,name,pos_x,pos_y,dir,speed,health=0,target=None,status={},awareness=0):
        self.name = name
        self.pos_x = pos_x          #position X
        self.pos_y = pos_y          #position Y
        self.dir = dir              #direction
        self.speed = speed          #speed on negatiicinen jos käevelee takaperin
        self.health = health
        self.target = target        #another Creature or map object
        self.awareness = awareness
        self.status = status

        ##status : dictionary, hostile, friendly,afraid, poisoned, running away etc

    def movement(self,dir,target=None):

        if target is not None:
            self.pos_x += dir * self.speed
            self.pos_y += dir * self.speed
        else:
            #define dir
            # target.pos_x
            # target.pos_y
            # # ....

            # self.pos_x += dir * self.speed
            # self.pos_y += dir * self.speed
            pass
    
    def notice(self,target):
        #awareness = 5 or something, in units of distance
        dist_x = abs(target.pos_x - self.pos_x)
        dist_y = abs(target.pos_y - self.pos_y)
        distance = math.hypot(dist_x,dist_y)

        if self.awareness - distance > 0:
            return True
        else: 
            return False

    ##bonus 1 
    def facing(self,pos_x,pos_y,dir,target):
        if self.notice(target) == True:
            dist_x = target.pos_x - pos_x
            dist_y = target.pos_y - pos_y
            if abs(dist_x) < abs(dist_y):
                dir = target.pos_x/abs(target.pos_x) #pos vai neg x
                ##jos 8-directional move niin silti tarvii xdir ja ydir? think

    
        # dir = target.pos_x* trig
        # = target.pos_y* trig
        ## lisää mahdollinen trigonometria että dir X ja Y osoittaa pelaajan/targetin suuntaan
        ## target yleensä pelaaja

    def hp_change(self):
        pass

    def __str__(self):
        return f"{self.name}"

        
class Enemy(Creature):
    def __init__(self,name,pos_x,pos_y,dir,speed,health,target,status,awareness,dmg):
        super().__init__(self,name,pos_x,pos_y,dir,speed,health,target,status,awareness)
        self.dmg = dmg
        status.append = {"walking" : 120 }


    def movement(self, dir, target=None):
        if self.status.walking == 120:
            dir = (randint(-1,1),randint(-1,1))

        if self.status.walking > 0:
            self.pos_x += dir(0) * self.speed
            self.pos_y += dir(1) * self.speed
            self.status.walking -= 1
        else:
            self.status.walking == 120
 
    def attack(target):
        pass

class NPC(Creature):
    def __init__(self,name,pos_x,pos_y,dir,speed,health,target,job):
        super().__init__(self,name,pos_x,pos_y,dir,speed,health,target)
        self.job = job

    def interact(self,name,job,target,status):
        facing(target)
        dialouge(name,like)
        ##UI elements
        