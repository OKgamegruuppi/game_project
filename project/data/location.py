import pygame
from data.settings import windowsizeX, windowsizeY


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


bord_x0 = Map_object(0,0,pygame.image.load("data/assets/x-border-width.jpg"))
bord_x100 = Map_object(0,windowsizeY-7,pygame.image.load("data/assets/x-border-width.jpg"))

bord_y0 = Map_object(0,0,pygame.image.load("data/assets/y-border-height.jpg"))
bord_y100 = Map_object(windowsizeX-7,0,pygame.image.load("data/assets/y-border-height.jpg"))

# bord_x0 = Map_object(0,0,windowsizeX,7,pygame.image.load("data\\assets\\x-border-width.jpg"))
# bord_x100 = Map_object(0,windowsizeY-7,windowsizeX,7,pygame.image.load("data\\assets\\x-border-width.jpg"))

# bord_y0 = Map_object(0,0,7,windowsizeY,pygame.image.load("data\\assets\\y-border-height.jpg"))
# bord_y100 = Map_object(windowsizeX-7,0,7,windowsizeY,pygame.image.load("data\\assets\\y-border-height.jpg"))

borders = pygame.sprite.Group(bord_x0,bord_x100,bord_y0,bord_y100)
