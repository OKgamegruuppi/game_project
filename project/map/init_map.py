from random import randint
from data.settings import windowsizeX as X
from data.settings import windowsizeY as Y
from data.creature import Creature,Enemy, Pickup
from data.player import Player
from data.location import Location
from data.location import Map_object,borders

import pygame


# Load test images
marcos = pygame.image.load("data/assets/slime_monster_mid.png")
cat1_ico = pygame.image.load("data/assets/Cat-sprite-stand.png")
defaultEnemy_icon2 = pygame.image.load("data/assets/TEST_Light_balls_tree1.png")

# Make objects, and add them to the Group    
##(name,image,pos_x,pos_y,dir,speed,health=0,target=None,status={},awareness=0)

player = Player("Marcos Petriades",marcos,50,50,(0,0))


playergroup = pygame.sprite.GroupSingle(player)
collidables =pygame.sprite.Group()
friendlies = pygame.sprite.Group()
enemies = pygame.sprite.Group()

cats = []
trees = []
for i in range(1,10):
    friendlies.add(Creature("Cat",cat1_ico,randint(20,X-20),randint(20,Y-20),[1,0],randint(1,4),1,None,{"walking":40,"standing":0}))    #make 9
    if i % 3 == 0 : enemies.add(Enemy("Green",defaultEnemy_icon2,randint(20,X-20),randint(20,Y-20),[1,0],2,1,awareness=50))             #make 3


grouplist = [borders,friendlies,enemies,playergroup]
for list in grouplist:
    for sprite in list:
        collidables.add(sprite)