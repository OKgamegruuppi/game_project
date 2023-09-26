import pygame

grouplist = []

playergroup = pygame.sprite.GroupSingle()
playergroup.name = "Playergroup"
friendlies = pygame.sprite.Group()
friendlies.name = "Friendlies"
enemies = pygame.sprite.Group()
enemies.name = "Enemies"

borders = pygame.sprite.Group()

collidables =pygame.sprite.Group()
collidables.name = "Collidables"



decor = pygame.sprite.Group()

effects = pygame.sprite.Group()
effects.name = "Effects"



grouplist.append(borders)
grouplist.append(friendlies)
grouplist.append(enemies)
grouplist.append(playergroup)
grouplist.append(effects)
