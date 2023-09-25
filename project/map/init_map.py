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


cat1 = Creature("Cat",cat1_ico,400,300,[1,0],1,1,None,{"walking":40,"standing":0})
cat2 = Creature("Cat",cat1_ico,500,300,[1,0],2,1,None,{"walking":60,"standing":0})
cat3 = Creature("Cat",cat1_ico,500,300,[1,0],3,1,None,{"walking":60,"standing":0})

defaultEnemy2 = Enemy("Green",defaultEnemy_icon2,280,260,[1,0],2,1)
cat1.target = defaultEnemy2

playergroup = pygame.sprite.GroupSingle(player)
friendlies = pygame.sprite.Group(cat1,cat2,cat3)
enemies = pygame.sprite.Group(defaultEnemy2)

grouplist = [borders,friendlies,enemies,playergroup]