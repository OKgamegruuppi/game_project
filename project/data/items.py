import pygame
from random import randint
from data.settings import mapsizeX, mapsizeY
from data.settings import fps as onesecond
from data.init_groups import *

class Item(pygame.sprite.Sprite):
    def __init__(self,name,image,pos_x,pos_y,timer=None,tangible=False):
        super().__init__()
        self.name = name
        self.image = image
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.timer = timer
        # Determine if the item goes into the inventory or not
        self.tangible = tangible

        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))

    def info(self):
        if self.timer:
            print(f"{self.name} has {int(self.timer/onesecond)} seconds left.")

    def spawn(self,x=None,y=None,timer=None):
        # If no position is given, choose randomly
        if x == None:
            self.pos_x = randint(10,mapsizeX-10)
            self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
        else:
            self.pos_x = x
            self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
        if y == None:
            self.pos_y = randint(10,mapsizeY-10)
            self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
        else:
            self.pos_y = y
            self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
            

        # Possible to set a timer when spawn() is called not just at 
        # init (for constantly appearing instances)
        self.timer = timer

    # Function that applies an effect on pickup
    def on_pick_up(self,target=None):
        pass

    def update(self):
        # If no timer, do nothing, else reduce timer and relocate
        if self.timer == None:
            pass
        elif self.timer > 0:
            self.timer -= 1
        else: 
            self.spawn(None,None,20*onesecond)  
        #spawn a "new" pickup with (number) amount of ticks in timer
        #visual effect only, actually teleports the same instance

# Class for Currency Items
class Currency(Item):
    def __init__(self,name,image,pos_x,pos_y,value=None,timer=None,tangible=None):
        super().__init__(name,image,pos_x,pos_y,timer,tangible)
        if value:
            self.value = value
        else:
            self.value = randint(1,100)

        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))

    def on_pick_up(self,target=None):
        target.currency += self.value

# Class for Healing Items
class Healing(Item):
    def __init__(self,name,image,pos_x,pos_y,heal=3,timer=None,tangible=None):
        super().__init__(name,image,pos_x,pos_y,timer,tangible)
        self.heal = heal

        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))

    def on_pick_up(self,target=None):
        target.hp_change(self.heal,self)