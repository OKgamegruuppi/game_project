import math
from random import randint
from data.settings import mapsizeX as X
from data.settings import mapsizeY as Y
from data.settings import show_hitboxes,quest_length
from data.location import Map_object,Decor
from data.creature import Creature
from data.enemies import Enemy, Spy
from data.player import Player
from data.items import Currency, Healing,QuestItem
from data.init_groups import *
from data.assets.images import *


import pygame
playerX,playerY = 930,450

player = Player("Marcos Goopyades",marcos_icon,playerX,playerY,(0,0),5,20,None,0,1)

def initialize_game():
    player.__init__("Marcos Goopyades",marcos_icon,playerX,playerY,(0,0),5,20,None,0,1)
    playergroup.add(player)
    #friendlies.add(player)


    print("INITIALIZING")

    'Get random coordinates for spawning each entry, first parameter is DISTANCE from player'
    def rand_coords(avoidplayer_dist=False,minX= 20, maxX= X-20 ,minY= 20 ,maxY= Y-20 ,):
        newX = randint(minX,maxX)
        newY = randint(minY,maxY)

        if avoidplayer_dist:
            dist= math.dist((newX,newY),(playerX,playerY))
            looplen = 0
            while dist < avoidplayer_dist and looplen < 5:
                newX = randint(minX,maxX)
                newY = randint(minY,maxY)
                dist= math.dist((newX,newY),(playerX,playerY))
                looplen +=1
        return newX,newY

    ### Good kitties need names
    quest_names=[
                "Tilly",
                "Molly",
                "Mr. Jenkins",
                "Garfield",
                "Oh Lawd",
                "Mittens",
                "Snickers",
                "El Gato",
                "Puss",
                "Whiskers",
                "Wednesday",
                "Kitty Softpaws",
                "Toast"
                ]

    ###### make the collectibles necessary to win #####
    for i in range(0,min(quest_length,13)):
        xx,yy = rand_coords(40)
        quest_items.append(QuestItem(quest_names[i],quest_icon,xx,yy))
        itemgroup.add(quest_items[i])
        


    for i in range(3):
        ####################    name,                   image           pos_x           pos_y       dir,speed,health
        xx,yy = rand_coords(40)
        itemgroup.add(Healing("Small Heal"+str(int(i/3)),testheart_icon,xx,yy))
        

        
    for i in range(0,10):
        ###########                   name,      image pos_x,pos_y           dir     speed   health awareness
        # xx,yy = rand_coords(40)
        # friendlies.add(Creature("Cat"+str(i),cat_icon,xx,yy,[1,0],randint(2,4),2))           
        
        xx,yy = rand_coords(40)
        itemgroup.add(Currency("Pile-o-Gold"+str(i),testitem_icon,xx,yy))
        
        xx,yy = rand_coords(700)
        enemies.add(Enemy("Green menace"+str(i),defaultEnemy_icon2,xx,yy,[1,0],2,3,800))             

    
    for i in range(0,30):
        ########################    name,  image pos_x,pos_y, dir     speed   health,awareness
        xx,yy = rand_coords(100)
        enemies.add(Spy("Spy"+str(i),spywillow_icon,xx,yy,[1,0],1,2,300))             

    # def spawn(number,function):
    #     for i in range(number):
    #         function()


    # (startX,startY,sizeX,sizeY, starts from top left corner)

    bord_x0 = Map_object(-150,-150,pygame.image.load("data/assets/x-border-width.jpg"))
    bord_x100 = Map_object(-150,Y+150,pygame.image.load("data/assets/x-border-width.jpg"))

    bord_y0 = Map_object(-150,-120,pygame.image.load("data/assets/y-border-height.jpg"))
    bord_y100 = Map_object(X+150,-120,pygame.image.load("data/assets/y-border-height.jpg"))


    borders.add(bord_x0,bord_x100,bord_y0,bord_y100)

    for i in range(100):
        xx,yy = rand_coords(30)
        decor.add(Decor(xx,yy,willow_icon))


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
