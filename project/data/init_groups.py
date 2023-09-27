import pygame

'''
DO NOT IMPORT ANY OTHER MODULES HERE
spritegroup initialisation for easy access
'''

#grouplist = []
collidables = []

playergroup = pygame.sprite.GroupSingle()
playergroup.name = "Playergroup"
friendlies = pygame.sprite.Group()
friendlies.name = "Friendlies"
enemies = pygame.sprite.Group()
enemies.name = "Enemies"
itemgroup = pygame.sprite.Group()
itemgroup.name = "Items"
borders = pygame.sprite.Group()

# collidables.name = "Collidables"



decor = pygame.sprite.Group()

effectsgroup = pygame.sprite.Group()
effectsgroup.name = "Effects"

# Create camera_group list
# IMPORTANT! When using camera_group, in other 
# modules add stuff to camera_group[0]
camera_group = []


'''collidables= a list of all collidable groups'''

collidables.append(borders)
collidables.append(friendlies)
collidables.append(enemies)
collidables.append(playergroup)
#collidables.append(effectsgroup)
