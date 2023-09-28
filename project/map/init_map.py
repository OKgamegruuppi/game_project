from random import randint
from data.settings import mapsizeX as X
from data.settings import mapsizeY as Y
from data.settings import show_hitboxes
from data.location import Map_object,Decor
from data.creature import Creature
from data.enemies import Enemy, Spy
from data.player import Player
from data.items import Currency, Healing
from data.init_groups import *
from data.assets.images import *


import pygame


player = Player("Marcos Petriades",marcos_icon,int(X/2),int(Y/2),(0,0))
playergroup.add(player)

       
for i in range(3):
    ####################    name,                   image           pos_x           pos_y       dir,speed,health
    enemies.add(Enemy("Green"+str(int(i/3)),defaultEnemy_icon2,randint(20,X-20),randint(20,Y-20),[1,0],speed=3,health=3,awareness=150))             #make 3
    itemgroup.add(Healing("Small Heal"+str(int(i/3)),testheart_icon,randint(20,X-20),randint(20,Y-20)))
    

# Make objects, and add them to the Group    
                        ##(name,image,pos_x,pos_y,dir,speed,health=0,target=None,awareness=0)
for i in range(0,10):
    ########################    name,      image    pos_x           pos_y           dir     speed   health
    friendlies.add(Creature("Cat"+str(i),cat1_icon,randint(20,X-20),randint(20,Y-20),[1,0],randint(2,4),2))           #make 9
    itemgroup.add(Currency("Pile-o-Gold"+str(i),testitem_icon,randint(20,X-20),randint(20,Y-20)))
    enemies.add(Spy("Spy"+str(i),spywillow_icon,randint(20,X-20),randint(20,Y-20),[1,0],speed=1,health=1,awareness=50))             #make 3


# (startX,startY,sizeX,sizeY, starts from top left corner)

bord_x0 = Map_object(-150,-150,pygame.image.load("data/assets/x-border-width.jpg"))
bord_x100 = Map_object(-150,Y+150,pygame.image.load("data/assets/x-border-width.jpg"))

bord_y0 = Map_object(-150,-120,pygame.image.load("data/assets/y-border-height.jpg"))
bord_y100 = Map_object(X+150,-120,pygame.image.load("data/assets/y-border-height.jpg"))


borders.add(bord_x0,bord_x100,bord_y0,bord_y100)

for i in range(200):
    
    random_x = randint(50,X-50)
    random_y = randint(50,Y-50)
    decor.add(Decor(random_x,random_y,willow_icon))


def add_to_camera():
#####add all creatures to camera_group
    for i in borders:
        camera_group[0].add(i)
    for i in decor:
        camera_group[0].add(i)
    for i in enemies:
        camera_group[0].add(i)
    for i in friendlies:
        camera_group[0].add(i)
    for i in itemgroup:
        camera_group[0].add(i)
    camera_group[0].add(player)


######TBD
    # if show_hitboxes:
    #     for list in grouplist:
    #         for sprite in list:
    #             camera_group.add(sprite.rect)
