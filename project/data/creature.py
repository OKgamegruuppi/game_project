import math
import pygame
# import pygame
from random import randint

class Creature(pygame.sprite.Sprite):
    def __init__(self,name,image,pos_x,pos_y,dir,speed,health=0,target=None,status={},awareness=0):
        super().__init__()
    #def __init__(self,name,pos_x,pos_y,dir,speed,status={}):
        self.name = name
        self.image = image
        self.pos_x = pos_x          #position X
        self.pos_y = pos_y          #position Y
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
        self.dir = dir              #direction 
        self.speed = speed          #jos speed on negatiivinen niin käevelee takaperin
        self.health = health
        self.target = target        #another Creature or map object
        self.awareness = awareness
        self.status = status

        ##status : dictionary, hostile, friendly,afraid, poisoned, running away etc


        ## status walking pituus on 60 ticks
    def movement(self, target=None):

        #target on objektissa määritelty mutta VOI määritellä myös erikseen movement funktiossa jos haluat targetoida koordinaatteja
        target = self.target if self.target else target

        print(f"{self.name}, target {target}")
        if not target: 
            print(f"{self.name} is dumdum")   
            # print(f"{self.name}, no target")   

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
            else:
                self.status["standing"] += 1
                print(self.status["standing"])

            #kun seisonut 0.5s, määritä kävely taas 60 ticks
            if self.status["standing"] >= 30:
                self.status["walking"] =60
                self.status["standing"] = 0
                print(self.status["standing"])

        else:
            # print(f"{self.name}, target {target}")   

            #valitse suunta sen perusteella onko kohteen x tai y koordinaatti eri ku sun oma

            dir_x = 1 if target.pos_x > self.pos_x else\
                0 if target.pos_x == self.pos_x else -1
            
            dir_y = 1 if target.pos_y > self.pos_y else\
                0 if target.pos_y == self.pos_y else -1

            self.pos_x += dir_x * self.speed
            self.pos_y += dir_y * self.speed

        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
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

    def update(self):
        self.movement()
        

        
class Enemy(Creature):
    #def __init__(self,name,pos_x,pos_y,dir=(),speed=1,status={"walking":20,"cooldown":0}):
                
    def __init__(self,name,image,pos_x,pos_y,dir,speed=1,health=0,target=None,status={"walking":20,"standing":0},awareness=1,dmg=1):
        # super().__init__(name,image,pos_x,pos_y,dir,speed,health=0,target=None,status={"walking":20,"standing":0},awareness=1)
        super().__init__(name,image,pos_x,pos_y,dir,speed,health,target,status,awareness)
        # super().__init__(self,name,pos_x,pos_y,dir,speed,health,target,status,awareness)
        self.dmg = dmg


## Exact sama kopio suoreaan creaturessa

    # def movement(self, target=None):
    #     if self.status["walking"] == 60:
    #         #valitse satunnainen suunta vain sillon kun ensimmäisen kerran alkaa liikkumaan
    #         self.dir = (randint(-1,1),randint(-1,1))
    #         print(f"x {self.pos_x} y {self.pos_y} direction {self.dir[0]} ")

    #     #vähennä kävely-statuksen kestoa 1 per tick 
    #     if self.status["walking"] > 0:
    #         self.pos_x += self.dir[0] * self.speed
    #         self.pos_y += self.dir[1] * self.speed
    #         self.status["walking"] -= 1

    #         #kun kävelystatus on 0, seiso status hetken aikaa
    #     else:
    #         self.status["standing"] += 1
    #         print(self.status["standing"])

    #     #kun seisonut 0.5s, määritä kävely taas 60 ticks
    #     if self.status["standing"] >= 30:
    #         self.status["walking"] =60
    #         self.status["standing"] = 0
    #         print(self.status["standing"])
 
    def attack(target):
        pass

class NPC(Creature):
    def __init__(self,name,image,pos_x,pos_y,rect,dir,speed=1,health=0,target=None,status={"walking":20,"standing":0},awareness=1,job=None):
        super().__init__(name,image,pos_x,pos_y,rect,dir,speed,health,target,status,awareness)
        self.job = job

    def interact(self,name,job,target,status):
        #facing(target)
        #dialouge(name,status)
        pass
        ##UI elements


class Pickup(Creature):
    #technically not a creature, sue me

    def __init__(self,name,image,pos_x,pos_y,rect,timer=None):
        super().__init__(name,image,pos_x,pos_y,rect)
        self.timer = timer

    def spawn(self,timer=None):
        #chooses a random location in bounds (-10 from the edges atm, needs to have 
        # (10, display.width - 10 )

        self.pos_x = randint(10,1070)
        self.pos_y = randint(10,710)
        self.timer = timer
        #possible to set a timer when spawn() is called not just at init (for constantly appearing instances)

    def update(self):
        if self.timer and self.timer > 0:
            self.timer -= 1 
        else: self.spawn(60)       
        #spawn a "new" pickup with (number) amount of ticks in timer
        #visual effect only, actually teleports the same instance

        