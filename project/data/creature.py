import math
# import pygame
from random import randint

class Creature():
    # def __init__(self,name,pos_x,pos_y,dir,speed,health=0,target=None,status={},awareness=0):
    def __init__(self,name,pos_x,pos_y,dir,speed,status={}):
        self.name = name
        self.pos_x = pos_x          #position X
        self.pos_y = pos_y          #position Y
        self.dir = dir              #direction
        self.speed = speed          #speed on negatiicinen jos käevelee takaperin
        # self.health = health
        # self.target = target        #another Creature or map object
        # self.awareness = awareness
        self.status = status

        ##status : dictionary, hostile, friendly,afraid, poisoned, running away etc

    def movement(self,target=None):

        if not target:
            self.pos_x += self.dir * self.speed
            self.pos_y += self.dir * self.speed
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

    # def __str__(self):
    #     return f"{self.name}"

        
class Enemy(Creature):
    def __init__(self,name,pos_x,pos_y,dir=(),speed=1,status={"walking":20,"cooldown":0}):
    # def __init__(self,name,pos_x,pos_y,dir,speed,health,target,status={"walking":20},awareness,dmg):
        super().__init__(name,pos_x,pos_y,dir,speed,status)
        # super().__init__(self,name,pos_x,pos_y,dir,speed,health,target,status,awareness)
        # self.dmg = dmg


    ## status walking pituus on 60 ticks

    def movement(self, target=None):
        if self.status["walking"] == 60:
            #valitse satunnainen suunta vain sillon kun ensimmäisen kerran alkaa liikkumaan
            self.dir = (randint(-1,1),randint(-1,1))
            print(f"x {self.pos_x} y {self.pos_y} direction {self.dir[0]} ")

        #vähennä kävely-statuksen kestoa 1 per tick 
        if self.status["walking"] > 0:
            self.pos_x += self.dir[0] * self.speed
            self.pos_y += self.dir[1] * self.speed
            self.status["walking"] -= 1

        #kun kävelystatus on 0, seiso status hetken aikaa
        elif self.status["walking"] == 0:
            self.status["standing"] += 1
            print(self.status["walking"])

        #kun seisonut 0.5s, määritä kävely taas 60 ticks
        elif self.status["standing"] >= 30:
            self.status["walking"] =60
            self.status["standing"] = 0
            print(self.status["standing"])

        #should never reach this row
        else: self.status["walking"] =60
 
    def attack(target):
        pass

class NPC(Creature):
    def __init__(self,name,pos_x,pos_y,dir,speed,health,target,job):
        super().__init__(name,pos_x,pos_y,dir,speed,health,target)
        self.job = job

    def interact(self,name,job,target,status):
        facing(target)
        dialouge(name,status)
        ##UI elements
        