import math
from player import *

class Creature():
    def __init__(self,name,pos_x,pos_y,dir_x,dir_y,speed,health,target,status,awareness):
        self.name = name
        self.pos_x = pos_x          #position X
        self.pos_y = pos_y          #position Y
        self.dir_x = dir_x          #direction X
        self.dir_y = dir_y          #direction Y
        self.speed = speed
        self.health = health
        self.target = target        #another Creature or map object
        self.awareness = awareness
        self.status = status

        ##status : dictionary, hostile, friendly,afraid, poisoned, running away etc

    def movement(self,pos_x,pos_y,dir_x,dir_y,speed):
        self.pos_x += dir_x * speed
        self.pos_y += dir_y * speed
    
    def notice(self,target):
        #awareness = 5 or something, in units of distance
        dist_x = target.pos_x - self.pos_x
        dist_y = target.pos_y - self.pos_y
        distance = math.hypot(dist_x,dist_y)

        if self.awareness - distance > 0:
            return True
        else: 
            return False

    def facing(self,pos_x,pos_y,dir_x,dir_y,target):
        if notice(target) == True:
            dist_x = target.pos_x - pos_x
            dist_y = target.pos_y - pos_y

    
        # dir_x = target.pos_x* trig
        # dir_y = target.pos_y* trig
        ## lisää mahdollinen trigonometria että dir X ja Y osoittaa pelaajan/targetin suuntaan
        ## target yleensä pelaaja

    def hp_change(self):
        pass

    def __str__(self):
        return f"{self.name}"

        
class Enemy(Creature):
    def __init__(self,name,pos_x,pos_y,dir_x,dir_y,speed,health,target,dmg):
        super().__init__(self,name,pos_x,pos_y,dir_x,dir_y,speed,health,target)
        self.dmg = dmg

    def attack(target):
        pass

class NPC(Creature):
    def __init__(self,name,pos_x,pos_y,dir_x,dir_y,speed,health,target,job):
        super().__init__(self,name,pos_x,pos_y,dir_x,dir_y,speed,health,target)
        self.job = job

    def interact(self,name,job,target,status):
        facing(target)
        dialouge(name,like)
        ##UI elements
        