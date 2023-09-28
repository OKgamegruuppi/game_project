from random import randint
from data.settings import windowsizeX as X
from data.settings import windowsizeY as Y
from data.settings import mapsizeX as mapX
from data.settings import mapsizeY as mapY
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

       
# def spawn(number,function):
#     for i in range(number):
#         function(i)

# spawn(3,\
#       itemgroup.add(Healing("Small Heal"+str(int(i/3)),testheart_icon,randint(20,mapX-20),randint(20,mapY-20)))
#           )
# spawn(5,\
#     enemies.add(Enemy("Green"+str(int(i/3)),defaultEnemy_icon2,randint(20,mapX-20),randint(20,mapY-20),[1,0],2,3,150)))

# spawn(10,\
#     friendlies.add(Creature("Cat"+str(i),cat1_icon,randint(20,mapX-20),randint(20,mapY-20),[1,0],randint(2,4),2)))

# spawn(10,\
#     itemgroup.add(Currency("Pile-o-Gold"+str(i),testitem_icon,randint(20,mapX-20),randint(20,mapY-20))))

# spawn(10,\
#     enemies.add(Spy("Spy"+str(i),spywillow_icon,randint(20,mapX-20),randint(20,mapY-20),[1,0],1,1,150)))




for i in range(3):
    ####################    name,                   image           pos_x           pos_y       dir,speed,health
    itemgroup.add(Healing("Small Heal"+str(int(i/3)),testheart_icon,randint(20,mapX-20),randint(20,mapY-20)))
    

# Make objects, and add them to the Group    
for i in range(0,10):
    ########################    name,      image    pos_x           pos_y           dir     speed   health
    friendlies.add(Creature("Cat"+str(i),cat1_icon,randint(20,mapX-20),randint(20,mapY-20),[1,0],randint(2,4),2))           #make 9
    itemgroup.add(Currency("Pile-o-Gold"+str(i),testitem_icon,randint(20,mapX-20),randint(20,mapY-20)))
    enemies.add(Enemy("Green"+str(int(i/3)),defaultEnemy_icon2,randint(20,mapX-20),randint(20,mapY-20),[1,0],2,3,150))             #make 3

# Make objects, and add them to the Group    
for i in range(0,30):
    ########################    name,      image    pos_x           pos_y           dir     speed   health
    enemies.add(Spy("Spy"+str(i),spywillow_icon,randint(20,mapX-20),randint(20,mapY-20),[1,0],1,1,400))             #make 3


# (startX,startY,sizeX,sizeY, starts from top left corner)

bord_x0 = Map_object(-150,-150,pygame.image.load("data/assets/x-border-width.jpg"))
bord_x100 = Map_object(-150,mapY+150,pygame.image.load("data/assets/x-border-width.jpg"))

bord_y0 = Map_object(-150,-120,pygame.image.load("data/assets/y-border-height.jpg"))
bord_y100 = Map_object(mapX+150,-120,pygame.image.load("data/assets/y-border-height.jpg"))


borders.add(bord_x0,bord_x100,bord_y0,bord_y100)

for i in range(200):
    
    random_x = randint(50,mapX-50)
    random_y = randint(50,mapY-50)
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
