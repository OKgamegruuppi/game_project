from random import randint
from data.settings import windowsizeX as X
from data.settings import windowsizeY as Y
from data.settings import mapsizeX as mapX
from data.settings import mapsizeY as mapY
from data.settings import show_hitboxes
from data.location import Map_object,Decor
from data.creature import Creature
from data.enemies import Enemy
from data.player import Player
from data.items import Currency, Healing
from data.init_groups import *


import pygame


# Load test images
'CREATURES'
marcos = pygame.image.load("data/assets/slime_monster_spritesheet.png")
cat1_ico = pygame.image.load("data/assets/Cat-sprite-stand.png")
defaultEnemy_icon2 = pygame.image.load("data/assets/TEST_Light_balls_tree1.png")


player = Player("Marcos Petriades",marcos,int(X/2),int(Y/2),(0,0))
playergroup.add(player)

'ITEMS'
testitem = pygame.image.load("data/assets/gold_pile.png")
testheart = pygame.image.load("data/assets/heart.png")


'DECOR/ MAP TILES'
willow = pygame.image.load('data/assets/edited_Willow.png')



# Make objects, and add them to the Group    
                        ##(name,image,pos_x,pos_y,dir,speed,health=0,target=None,awareness=0)
for i in range(1,10):
    ########################    name,      image    pos_x           pos_y           dir     speed   health
    friendlies.add(Creature("Cat"+str(i),cat1_ico,randint(20,X-20),randint(20,Y-20),[1,0],randint(2,4),2))           #make 9
    itemgroup.add(Currency("Pile-o-Gold"+str(i),testitem,randint(20,mapX-20),randint(20,mapY-20)))
    ####################    name,          image           pos_x           pos_y    dir,speed,health
    enemies.add(Enemy("Spy"+str(int(i/2)),willow,randint(20,X-20),randint(20,Y-20),[1,0],speed=1,health=1,awareness=10,dmg=5,wander_dur =10,wait_dur=3*fps))   ##SPY TREE

    if i % 2 == 0 : 
        ######                       name,                  image,      pos_x,              pos_y,  (healing)value=1,    timer=None,tangible=None
        itemgroup.add(Healing("Small Heal"+str(int(i/3)),testheart,randint(20,mapX-20),randint(20,mapY-20),5))        #make 5

    if i % 3 == 0 : 
        ####################    name,                   image           pos_x           pos_y       dir,speed,health
        enemies.add(Enemy("Green"+str(int(i/3)),defaultEnemy_icon2,randint(20,X-20),randint(20,Y-20),[1,0],speed=1,health=3,awareness=50,dmg=1))             #make 3


# for list in grouplist[0:3]:     #skips grouplist[4]: effects
#     for sprite in list:
#         collidables.add(sprite)




# (startX,startY,sizeX,sizeY, starts from top left corner)

bord_x0 = Map_object(-150,-150,pygame.image.load("data/assets/x-border-width.jpg"))
bord_x100 = Map_object(-150,mapY+150,pygame.image.load("data/assets/x-border-width.jpg"))

bord_y0 = Map_object(-150,-120,pygame.image.load("data/assets/y-border-height.jpg"))
bord_y100 = Map_object(mapX+150,-120,pygame.image.load("data/assets/y-border-height.jpg"))


borders.add(bord_x0,bord_x100,bord_y0,bord_y100)

for i in range(200):
    
    random_x = randint(50,mapX-50)
    random_y = randint(50,mapY-50)
    decor.add(Decor(random_x,random_y,willow))













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
