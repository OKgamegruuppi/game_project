from data.creature import Creature,Enemy, Pickup
from data.location import Location
import pygame

defaultEnemy_icon = pygame.image.load("data\\assets\\slime_monster_ico.png")   #Load the image 
defaultEnemy_icon2 = pygame.image.load("data\\assets\\TEST_Light_balls_tree1.png")   #Load the image 
cat1_ico = pygame.image.load("data\\assets\\Cat-sprite-stand.png")   #Load the image 
#tree1_icon = pygame.image.load("data\\assets\\TEST_Light_balls_tree1.png")   #Load the image 

##enemy(name,image,pos_x,pos_y,dir[list],speed=1,health=0,target=None,status={"walking":20,"standing":0},awareness=1,dmg=1)

defaultEnemy = Enemy("Red",defaultEnemy_icon,1000,56,[-1,0],3,1)
defaultEnemy2 = Enemy("Green",defaultEnemy_icon2,300,156,[1,0],5,1)
cat1 = Creature("Cat",cat1_ico,300,156,[1,0],5,1,None,{"walking":40,"standing":0})
# tree1 = Location("tree",1000,600,tree1_icon)
#tree2 = Pickup("tree",tree1_icon,1000,600,60)

defaultEnemy.target = cat1
#cat1.target = tree2
# defaultEnemy2.target = defaultEnemy
alive1 = pygame.sprite.Group()

defaultEnemy.add(alive1)
cat1.add(alive1)

print("alive contains",alive1.sprites())

