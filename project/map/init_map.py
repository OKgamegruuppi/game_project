from random import randint
from data.settings import windowsizeX as X
from data.settings import windowsizeY as Y
from data.settings import mapsizeX as mapX
from data.settings import mapsizeY as mapY
from data.settings import show_hitboxes
from data.location import borders,decor
from data.creature import Creature
from data.enemies import Enemy
from data.player import Player
from data.items import Currency, Healing
from data.init_groups import *


import pygame


# Load test images
marcos = pygame.image.load("data/assets/slime_monster_spritesheet.png")
cat1_ico = pygame.image.load("data/assets/Cat-sprite-stand.png")
defaultEnemy_icon2 = pygame.image.load("data/assets/TEST_Light_balls_tree1.png")
testitem = pygame.image.load("data/assets/gold_pile.png")
testheart = pygame.image.load("data/assets/heart.png")

player = Player("Marcos Petriades",marcos,int(X/2),int(Y/2),(0,0))
playergroup.add(player)


# Make objects, and add them to the Group    
                        ##(name,image,pos_x,pos_y,dir,speed,health=0,target=None,awareness=0)
for i in range(1,10):
    ########################    name,      image    pos_x           pos_y           dir     speed   health
    friendlies.add(Creature("Cat"+str(i),cat1_ico,randint(20,X-20),randint(20,Y-20),[1,0],randint(2,4),2))           #make 9
    itemgroup.add(Currency("Pile-o-Gold"+str(i),testitem,randint(20,mapX-20),randint(20,mapY-20)))
    if i % 3 == 0 : 
        ####################    name,                   image           pos_x           pos_y       dir,speed,health
        enemies.add(Enemy("Green"+str(int(i/3)),defaultEnemy_icon2,randint(20,X-20),randint(20,Y-20),[1,0],speed=1,health=2,awareness=50))             #make 3
        itemgroup.add(Healing("Small Heal"+str(int(i/3)),testheart,randint(20,mapX-20),randint(20,mapY-20)))


# for list in grouplist[0:3]:     #skips grouplist[4]: effects
#     for sprite in list:
#         collidables.add(sprite)


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
