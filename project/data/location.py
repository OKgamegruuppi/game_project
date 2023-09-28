import pygame
from random import randint
from data.settings import *
from data.init_groups import borders,decor


class Map_object(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.pos_x = x
        self.pos_y = y
        self.image = image
        self.rect = self.image.get_rect(topleft=(self.pos_x,self.pos_y))     #this draws the image and works as a hitbox
####TOPLEFT


# class Border(Map_object):
#     def __init__(self,x,y,width,height,image):
#         super().__init__(x,y,image)
#         self.pos_x = x
#         self.pos_y = y
#         self.rect = pygame.Rect(x,y,width,height)

class Decor(Map_object):
    def __init__(self,x,y,image): 
        super().__init__(x,y,image)
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))
    


class Location(Map_object):
    def __init__(self,name,x,y,image):
        super().__init__(x,y,image)
        self.name = name
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))     #this draws the image and works as a hitbox
###CENTER
