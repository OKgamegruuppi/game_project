from data.creature import Creature,Enemy, Pickup
from data.location import Location
import pygame

defaultEnemy_icon = pygame.image.load("data\\assets\\slime_monster_ico.png")   #Load the image 
defaultEnemy_icon2 = pygame.image.load("data\\assets\\TEST_Light_balls_tree1.png")   #Load the image 
cat1_ico = pygame.image.load("data\\assets\\Cat-sprite-stand.png")   #Load the image 
#tree1_icon = pygame.image.load("data\\assets\\TEST_Light_balls_tree1.png")   #Load the image 
defaultEnemy_hitbox = True

##enemy(name,icon,hitbox,pos_x,pos_y,dir(tuple),speed=1,health=0,target=None,status={"walking":20,"standing":0},awareness=1,dmg=1)

defaultEnemy = Enemy("Red",defaultEnemy_icon,defaultEnemy_hitbox,1000,56,(-1,0),5,1)
defaultEnemy2 = Enemy("Green",defaultEnemy_icon2,defaultEnemy_hitbox,300,156,(1,0),5,1)
cat1 = Creature("Cat",cat1_ico,defaultEnemy_hitbox,300,156,(1,0),5,1)
# tree1 = Location("tree",1000,600,tree1_icon)
#tree2 = Pickup("tree",defaultEnemy_hitbox,tree1_icon,1000,600,60)

defaultEnemy.target = cat1
#cat1.target = tree2
# defaultEnemy2.target = defaultEnemy
alive1 = pygame.sprite.Group()

defaultEnemy.add(alive1)
cat1.add(alive1)

print("alive contains",alive1.sprites())

