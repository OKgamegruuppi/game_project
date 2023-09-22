from data.creature import Enemy
import pygame

defaultEnemy_icon = pygame.image.load("data\\assets\\slime_monster.png")   #Load the image 
defaultEnemy_icon2 = pygame.image.load("data\\assets\\TEST_Light_balls_tree1.png")   #Load the image 
defaultEnemy_hitbox = True

##enemy(name,icon,hitbox,pos_x,pos_y,dir(tuple),speed=1,health=0,target=None,status={"walking":20,"standing":0},awareness=1,dmg=1)

defaultEnemy = Enemy("Red",defaultEnemy_icon,defaultEnemy_hitbox,500,56,(-1,0),5,1)
defaultEnemy2 = Enemy("Green",defaultEnemy_icon2,defaultEnemy_hitbox,300,156,(1,0),5,1,defaultEnemy)
defaultEnemy.target = defaultEnemy2
print(defaultEnemy2.target)



