from player import *

class Creature():
    def __init__(self,name,pos_x,pos_y,dir_x,dir_y,speed,health,target):
        self.name = name
        self.pos_x = pos_x          #position X
        self.pos_y = pos_y          #position Y
        self.dir_x = dir_x          #direction X
        self.dir_y = dir_y          #direction Y
        self.speed = speed
        self.health = health
        self.target = target        #another Creature or map object

    def movement(self,pos_x,pos_y,dir_x,dir_y,speed):
        pos_x += dir_x * speed
        pos_y += dir_y * speed

    def facing(self,pos_x,pos_y,dir_x,dir_y,target):
        dist_x = target.pos_x - pos_x
        dist_y = target.pos_y - pos_y

        # dir_x = target.pos_x* trig
        # dir_y = target.pos_y* trig
        ## lisää mahdollinen trigonometria että dir X ja Y osoittaa pelaajan/targetin suuntaan
        ## target yleensä pelaaja

    def hp_change():
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
    def __init__(self,name,pos_x,pos_y,dir_x,dir_y,speed,health,target,like,job):
        super().__init__(self,name,pos_x,pos_y,dir_x,dir_y,speed,health,target)
        self.like = like            ##relationship status to player, integer (-5 to +5?) etc
        self.job = job

    def interact(self,name,job,target,like):
        facing(target)
        dialouge(name,like)
        ##UI elements
        