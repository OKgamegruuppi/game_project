import math
import pygame
from random import randint,choice
from data.settings import windowsizeX, windowsizeY
from data.settings import fps as onesecond
import data.effects as effectmod
from data.init_groups import *



class Creature(pygame.sprite.Sprite):
    def __init__(self,name,image,pos_x,pos_y,dir,speed,health=0,target=None,status={},awareness=0):
        super().__init__()
    #def __init__(self,name,pos_x,pos_y,dir,speed,status={}):
        self.name = name
        self.image = image
        self.pos_x = pos_x          #position X
        self.pos_y = pos_y          #position Y
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))     #this draws the image and works as a hitbox
        self.dir = pygame.math.Vector2()              #direction 
        self.dir.xy = dir[0], dir[1]
        self.speed = speed          #jos speed on negatiivinen niin käevelee takaperin
        self.health = health
        self.target = target        #another Creature or map object
        self.awareness = awareness      
        self.status = status

        ##status : dictionary, hostile, friendly,afraid, poisoned, running away etc



    def info(self):
        print(f"{self.name} targeting {self.target.name if self.target else None}")
        pass


    def collisions(self,grouplist,mode="y/n"):
        #muista päivittää hitbox ennen ku testaat collisionit
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
        
        for group in grouplist:
            #if current group is a group that contains this sprite, test if more than 1 collision:
            # if sprite is in the same group the sprite itself counts as 1 collision to itself
            if group in self.groups() and len(pygame.sprite.spritecollide(self,group,False)) > 1:
                #print(f"{self.name} got hit by {group}!")

                return True if mode=="y/n" else group #returns either a boolean or the group that was hit
            
            elif (group not in self.groups()) and pygame.sprite.spritecollideany(self,group):
                #print(f"{self.name} got hit by {group}!")

                return True if mode=="y/n" else group
            else:
                continue

    def collisions_individual(self,group):
        #muista päivittää hitbox ennen ku testaat collisionit
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))

        for sprite in group:
            # if sprite is in the same group the sprite itself counts as 1 collision to itself
            if self != sprite and pygame.sprite.collide_rect(self,sprite):
                #print(f"{self.name} got hit by {sprite}!")
                return sprite
            else:
                continue


        ## status walking pituus on 60 ticks
    def movement(self,groups, target=None):

        #target on objektissa määritelty mutta VOI määritellä myös erikseen movement funktiossa jos haluat targetoida koordinaatteja
        target = self.target if self.target else target

        orig_pos_x = self.pos_x 
        orig_pos_y = self.pos_y

        if self.target and self.notice(self.target):       #when HAS a target
            
            if pygame.sprite.collide_rect(self,self.target):
                #target is caught, do not move
                self.interact(target,groups)
                return      #print(f"caught {target.name}")
            
            #valitse suunta sen perusteella onko kohteen x tai y koordinaatti eri ku sun oma
            #self dir is 1, 0 or -1
            self.dir.x = 1 if target.pos_x > self.pos_x else\
                0 if target.pos_x == self.pos_x else -1
            
            self.dir.y = 1 if target.pos_y > self.pos_y else\
                0 if target.pos_y == self.pos_y else -1
            
            #IF distance from target is less than speed, only move the required distance
            #ELSE move speed amount of pixels in the directionof target
            if abs(target.pos_x - self.pos_x) < self.speed:
                self.pos_x += self.dir.x * abs(target.pos_x - self.pos_x)
            else: self.pos_x += self.dir.x * self.speed
            

            if abs(target.pos_y - self.pos_y) < self.speed:
                self.pos_y += self.dir.y * abs(target.pos_y - self.pos_y)
            else: self.pos_y += self.dir.y * self.speed

            self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
            if pygame.sprite.collide_rect(self,target):
                self.interact(target,groups)
                return              #print(f"caught {target.name}")
            elif self.collisions(groups):

                self.dir.x = choice((0,-self.dir.x))
                self.dir.y = choice((0,-self.dir.y))
                self.pos_x = orig_pos_x + self.dir.x * self.speed
                self.pos_y = orig_pos_y + self.dir.y * self.speed
                
                #if still got collisions, stay still
                if self.collisions(groups):
                    self.pos_x = orig_pos_x 
                    self.pos_y = orig_pos_y

        else:           #when target too far or doesn't have one

            if self.status["walking"] == onesecond:
                #valitse satunnainen suunta vain sillon kun ensimmäisen kerran alkaa liikkumaan
                self.dir.xy = randint(-1,1), randint(-1,1)

            #vähennä kävely-statuksen kestoa 1 per tick 
            if self.status["walking"] > 0:

                self.pos_x += self.dir.x * self.speed
                self.pos_y += self.dir.y * self.speed  

                if self.collisions(groups):

                    self.dir.x = choice((0,-self.dir.x))
                    self.dir.y = choice((0,-self.dir.y))
                    
                    self.pos_x = orig_pos_x + self.dir.x * self.speed
                    self.pos_y = orig_pos_y + self.dir.y * self.speed
                    #if still got collisions, stay still
                    if self.collisions(groups):
                        self.pos_x = orig_pos_x
                        self.pos_y = orig_pos_y
                 

                self.status["walking"] -= 1

                #kun walking on 0, status standing hetken aikaa
            else:
                self.status["standing"] += 1

            #kun seisonut 0.5s, määritä kävely taas 60 ticks
            if self.status["standing"] >= 0.2*onesecond:
                            #0.2*onesec is a float, remember this for later
                #print("stood for ",self.status["standing"])
                self.status["walking"] = 1*onesecond
                self.status["standing"] = 0


        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
        ##muista päivittää self.rect joka hoitaa kuvan piirtämisen ja hitboxit


    def notice(self,target):

        '  Notice returns a tuple of, was it noticed and how far was it  '

        #awareness = 5 or something, in units of distance
        if target.alive == False:
            return False
        
        distance= math.dist( (target.pos_x,target.pos_y) , (self.pos_x,self.pos_y) )
        
        if self.awareness > distance:
            return True
        else: 
            return False
        
        # #add a targeting status that gets set to maximum value every time the target enters the awareness radius 
        # #"memory" of targeting is stored as a status effect
        # if self.awareness - distance > 0:
        #     self.status["targeting"] = 10*self.awareness
        #     return True
        # elif "targeting" in self.status:
        #     self.status["targeting"] -= 1
        #     if self.status["targeting"] == 0:
        #         del self.status["targeting"]        #clear status effect
        #     return True
        # else: 
        #     return False

    ##bonus 1 
    def facing(self,pos_x,pos_y,target):
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

    # Change HP of the Creature
    def hp_change(self,change,effects):
        self.health += change
        if change < 0:
            damage = effectmod.Effect("Ouchie",effectmod.blood_red,self.pos_x,self.pos_y,int(onesecond/2))
            damage.add(effects)
        if self.health <= 0:
            self.kill()
            print("Oops, I died!")
            print(self.groups)
            # Add a function to remove self from "alive" groups
            # And or completely remove Creature
        else:
            print(f"Current HP: {self.health}")

    # def __str__(self):
    #     return f"{self.name}"
    def interact(self,target,groups):
        print(f"{self.name}interacted with {self.target}")

    def update(self,groups):
        self.collisions(groups)
        self.movement(groups)
        



class NPC(Creature):
    def __init__(self,name,image,pos_x,pos_y,dir,speed=1,health=0,target=None,status={"walking":20,"standing":0},awareness=1,job=None):
        super().__init__(name,image,pos_x,pos_y,dir,speed,health,target,status,awareness)
        self.job = job

    def interact(self,name,job,target,status):
        #facing(target)
        #dialouge(name,status)
        pass

        ##UI elements




class Pickup(Creature):
    #technically not a creature, sue me

    def __init__(self,name,image,pos_x,pos_y,timer=None):
        super().__init__(name,image,pos_x,pos_y)
        self.timer = timer

    def spawn(self,timer=None):
        #chooses a random location in bounds (-10 from the edges atm)

        self.pos_x = randint(10,windowsizeX-10)
        self.pos_y = randint(10,windowsizeY-10)
        self.timer = timer
        #possible to set a timer when spawn() is called not just at init (for constantly appearing instances)

    def update(self):
        if self.timer and self.timer > 0:
            self.timer -= 1 
        else: self.spawn(onesecond)       
        #spawn a "new" pickup with (number) amount of ticks in timer
        #visual effect only, actually teleports the same instance

        