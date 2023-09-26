from random import randint
from data.settings import windowsizeX as X
from data.settings import windowsizeY as Y
from data.settings import show_hitboxes
from data.location import borders,decor
from data.creature import Creature,Pickup
from data.enemies import Enemy
from data.player import Player
from data.init_groups import *


import pygame


# Load test images
marcos = pygame.image.load("data/assets/slime_monster_spritesheet.png")
cat1_ico = pygame.image.load("data/assets/Cat-sprite-stand.png")
defaultEnemy_icon2 = pygame.image.load("data/assets/TEST_Light_balls_tree1.png")

player = Player("Marcos Petriades",marcos,int(X/2),int(Y/2),(0,0))
playergroup.add(player)


# Make objects, and add them to the Group    
                        ##(name,image,pos_x,pos_y,dir,speed,health=0,target=None,status={},awareness=0)
for i in range(1,10):
    friendlies.add(Creature("Cat"+str(i),cat1_ico,randint(20,X-20),randint(20,Y-20),[1,0],randint(1,4),1,None,{"walking":40,"standing":0}))           #make 9
    if i % 3 == 0 : enemies.add(Enemy("Green"+str(int(i/3)),defaultEnemy_icon2,randint(20,X-20),randint(20,Y-20),[1,0],2,1,awareness=50))             #make 3


for list in grouplist[0:3]:     #skips grouplist[4]: effects
    for sprite in list:
        collidables.add(sprite)


def add_to_camera(camera_group):
#####add all creatures to camera_group
    for i in borders:
        camera_group.add(i)
    for i in decor:
        camera_group.add(i)
    for i in enemies:
        camera_group.add(i)
    for i in friendlies:
        camera_group.add(i)
    camera_group.add(player)


######TBD
    # if show_hitboxes:
    #     for list in grouplist:
    #         for sprite in list:
    #             camera_group.add(sprite.rect)
