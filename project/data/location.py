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

# class Border(Map_object):
#     def __init__(self,x,y,width,height,image):
#         super().__init__(x,y,image)
#         self.pos_x = x
#         self.pos_y = y
#         self.rect = pygame.Rect(x,y,width,height)


class Location(Map_object):
    def __init__(self,name,x,y,image):
        super().__init__(x,y,image)
        self.name = name
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))     #this draws the image and works as a hitbox

# (startX,startY,sizeX,sizeY, starts from top left corner)
willow = pygame.image.load('data/assets/edited_Willow.png')

bord_x0 = Map_object(-150,-150,pygame.image.load("data/assets/x-border-width.jpg"))
bord_x100 = Map_object(-150,mapsizeY+150,pygame.image.load("data/assets/x-border-width.jpg"))

bord_y0 = Map_object(-150,-120,pygame.image.load("data/assets/y-border-height.jpg"))
bord_y100 = Map_object(mapsizeX+150,-120,pygame.image.load("data/assets/y-border-height.jpg"))



# bord_x0 = Map_object(0,0,windowsizeX,7,pygame.image.load("data\\assets\\x-border-width.jpg"))
# bord_x100 = Map_object(0,windowsizeY-7,windowsizeX,7,pygame.image.load("data\\assets\\x-border-width.jpg"))

# bord_y0 = Map_object(0,0,7,windowsizeY,pygame.image.load("data\\assets\\y-border-height.jpg"))
# bord_y100 = Map_object(windowsizeX-7,0,7,windowsizeY,pygame.image.load("data\\assets\\y-border-height.jpg"))

borders.add(bord_x0,bord_x100,bord_y0,bord_y100)

for i in range(200):
    
    random_x = randint(50,mapsizeX-50)
    random_y = randint(50,mapsizeY-50)
    decor.add(Map_object(random_x,random_y,willow))
