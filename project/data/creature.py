import math
import pygame
from random import randint,choice
from data.settings import windowsizeX, windowsizeY
from data.settings import fps as onesecond
import data.effects as effectmod
from data.init_groups import *



class Creature(pygame.sprite.Sprite):
    def __init__(self,name,image,pos_x,pos_y,dir,speed,health=0,target=None,awareness=0):
        super().__init__()
        self.name = name
        self.image = image
        self.pos_x = pos_x          #position X
        self.pos_y = pos_y          #position Y
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))     #this draws the image and works as a hitbox
        self.dir = pygame.math.Vector2()              #direction 
        self.dir.xy = dir[0], dir[1]
        self.speed = speed          #jos speed on negatiivinen niin käevelee takaperin
        self.health = health
        self.maxhealth = health
        self.target = target        #another Creature or map object, is a SHALLOW COPY, remove with self.target = None
        self.awareness = awareness 
        self.wander_dur = 1*onesecond     
        self.status = {"walking":self.wander_dur,"standing":0}            #dictionary, ex:  "walking", "standing", "targeting", "attack_cooldown" 
        self.collidedwith = []      #includes a list of groups and self.target Creature

        ##status : dictionary, hostile, friendly,afraid, poisoned, running away etc



    # def __str__(self):
    #     return f"{self.name}"

    #Remember to add INFO: in start of every print command here.
    #info is called once per onesecond
    def info(self):
        print(f"INFO: {self.name} targeting {self.target.name if self.target else None}")
        #print(f"INFO: {self.name}{self.status}")
        pass


    def collisions(self):
        #muista päivittää hitbox ennen ku testaat collisionit
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
        self.collidedwith = []         #empty the list of collisions and recalculate every time
        collide_result = False

        for group in collidables:
            #if current group is a group that contains this sprite, test if more than 1 collision:
            # if sprite is in the same group the sprite itself counts as 1 collision to itself
            if group in self.groups() and len(pygame.sprite.spritecollide(self,group,False)) > 1:
                #print(f"{self.name} got hit by {group}!")
                self.collidedwith.append(group)
                collide_result = True
                continue
                #return True if mode=="y/n" else group #returns either a boolean or the group that was hit
            
            elif (group not in self.groups()) and pygame.sprite.spritecollideany(self,group):
                #print(f"{self.name} got hit by {group}!")
                self.collidedwith.append(group)
                collide_result = True
                continue
                #return True if mode=="y/n" else group
            else:
                continue
        if self.target and pygame.sprite.collide_rect(self,self.target):
            self.collidedwith.append(self.target)
        return collide_result
    
        

    def collisions_individual(self,group):
        #muista päivittää hitbox ennen ku testaat collisionit
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))

        for sprite in group:
            # if sprite is in the same group the sprite itself counts as 1 collision to itself
            if self != sprite and pygame.sprite.collide_rect(self,sprite):
                #print(f"{self.name} got hit by {sprite}!")
                self.collidedwith.append(sprite)
                return sprite
            else:
                continue


    def notice(self,target):

        #awareness = 5 or something, in units of distance
        if target.alive == False:
            return False
        
        distance= math.dist( (target.pos_x,target.pos_y) , (self.pos_x,self.pos_y) )
        
        if self.awareness > distance:
            return True
        else: 
            return False


    def targeting(self):
        if (self.target is None) or (self.target.alive == False):
            self.target = None
            if "targeting" in self.status: del self.status["targeting"]         #delete targeting status if target was removed elsewhere
            if self.status["walking"]<=0: self.status["walking"] = self.wander_dur
            return


        if self.notice(self.target):        #notice returns False if target is None
            self.status["targeting"] = math.floor(0.1 * self.awareness * onesecond)       #refresh targeting status if in notice range
            #better awareness = longer memory

        elif "targeting" in self.status:
            self.status["targeting"] -= 1
            if self.status["targeting"] == 0:
                del self.status["targeting"]       #clear status effect
                self.target = None                  #target is forgot
                


    def movement(self):
        speed_x = self.speed
        speed_y = self.speed

        orig_pos_x = self.pos_x 
        orig_pos_y = self.pos_y

######## select direction  #######################################

        '''targeting() is called before movement(), so at this point the Creature shouldn't have any "dead" targets
           targeting() removes dead targets.        '''
        
        if self.target and "targeting" in self.status:      
            '''set direction and speed for targeted movement''' 
            
            if self.target in self.collidedwith:
                #target is caught, do not move
                #print(self.name,"caught the target")
                return
            
            # if pygame.sprite.collide_rect(self,self.target):
            #     self.collidedwith.append(self.target)
            #     #target is caught, do not move
            #     return    
            

            #valitse suunta sen perusteella onko kohteen x tai y koordinaatti eri ku sun oma
            #self dir is 1, 0 or -1
            self.dir.x = 1 if self.target.pos_x > self.pos_x else\
                0 if self.target.pos_x == self.pos_x else -1
            
            self.dir.y = 1 if self.target.pos_y > self.pos_y else\
                0 if self.target.pos_y == self.pos_y else -1
            

            #IF distance from target is less than speed, only move the required distance
            #ELSE move speed amount of pixels in the directionof target
            if abs(self.target.pos_x - self.pos_x) < self.speed:
                speed_x = abs(self.target.pos_x - self.pos_x)

            
            if abs(self.target.pos_y - self.pos_y) < self.speed:
                speed_y = abs(self.target.pos_y - self.pos_y)
            

        else:  #    when target too far or doesn't have one

            #onesecond = game tickspeed
            if self.status["walking"] == self.wander_dur :       
                #valitse satunnainen suunta vain sillon kun ensimmäisen kerran alkaa liikkumaan
                self.dir.xy = randint(-1,1), randint(-1,1)
        
########    Direction has been selected     ###################################

        if (self.status["walking"] > 0) or "targeting" in self.status:

            self.pos_x += self.dir.x * speed_x
            self.pos_y += self.dir.y * speed_y

            ### update hitbox to match new location,      CENTER jos haluaa et se törmää kuvan reunoihin

            self.collisions()
            #self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
            if len(self.collidedwith) == 0:          #empty list is FALSE    
                if "walking" in self.status: self.status["walking"] -= 1
                return              #nothing collided, exit the function
            
            
            elif self.target in self.collidedwith:
                return
                """    movement is successful even if you're in an illegal position, as long as you're colliding with target"""
            
            else:

################    handling collisions,  targeted and not targeted movement      #############

                if self.target:
                    self.dir.xy = choice(( (0,self.dir.y) , (self.dir.x,0) ))

                else:
                    self.dir.x = choice((0,-self.dir.x))
                    self.dir.y = choice((0,-self.dir.y))
                
                self.pos_x = orig_pos_x + self.dir.x * speed_x
                self.pos_y = orig_pos_y + self.dir.y * speed_y

                #if still got collisions, stay still
                if self.collisions():
                    self.pos_x = orig_pos_x
                    self.pos_y = orig_pos_y

                self.status["walking"] -= 1
            
        elif self.status["walking"] == 0:

            self.status["standing"] += 1

            #kun seisonut 0.2s, määritä kävely taas 60 ticks
            if self.status["standing"] >= 0.2*onesecond:        #0.2*onesec is a float, remember this for later
                            
                #print("stood for ",self.status["standing"])
                self.status["walking"] = self.wander_dur
                self.status["standing"] = 0
                
        else: print(f"{self.name} has an error with movement")

        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
        ##muista päivittää self.rect joka hoitaa kuvan piirtämisen ja hitboxit

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
    def hp_change(self,change,source=None):
        self.health = min(self.maxhealth,self.health+change)
        if change > 0:
            damage = effectmod.Effect("Heal",effectmod.small_heart,self.pos_x,self.pos_y,int(onesecond/3))
            damage.add(effectsgroup)
            damage.add(camera_group)
            if source:
                print(f"{self.name} was healed {change}hp by {source.name}.")
            else:
                print(f"{self.name} was healed {change}hp.")
        elif change < 0:
            damage = effectmod.Effect("Ouchie",effectmod.blood_red,self.pos_x,self.pos_y,int(onesecond/2))
            damage.add(effectsgroup)
            damage.add(camera_group)
            if self in friendlies: self.speed += 1
            if source:
                print(f"{self.name} was dealt {-change} damage by {source.name}.")
            else:
                print(f"{self.name} was dealt {-change} damage.")
            if self.health <= 0:
                self.kill()
                print(f"{self.name}: Oops, I was killed by {source.name}")

        print(f"{self.name}: Current HP: {self.health}")


    '''Call interact() funcion from other creatures for NPC interaction, opening doors etc'''
    def interact(self,target):
        print(f"{self.name} interacted with {target}")
    

    def update(self):
        self.collisions()
        self.targeting()
        self.movement()

        #movement checks if your target's hitbox was reached and adds the target to the list self.collidedwith
        if self.target in self.collidedwith:
            self.interact(self.target)
        



class NPC(Creature):
    def __init__(self,name,image,pos_x,pos_y,dir,speed=1,health=0,target=None,awareness=1,job=None):
        super().__init__(name,image,pos_x,pos_y,dir,speed,health,target,awareness)
        self.job = job

    def interact(self,name,job,target,status):
        #facing(target)
        #dialouge(name,status)
        pass

        ##UI elements

        