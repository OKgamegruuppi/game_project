#libraries
import pygame, sys
from random import randint
from data.settings import windowsizeX, windowsizeY
from map.init_map import grouplist,enemies,player
from data.controls import game_event_observer
from data.screenrefresher import draw_on_screen

#classes (Tree, Player, CameraGroup)
class Tree(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.image.load('data/assets/edited_Willow.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)
        self.image = pygame.image.load('data/assets/slime_monster_mid.png').convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.speed = 5

    #los functiones des playerinos
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed
#####################################################################################
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
       
        # camera offset
        self.offset = pygame.math.Vector2(300,100)
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        #ground
        self.ground_surf = pygame.image.load('data/assets/ground.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0)) 

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h


    def custom_draw(self, player):
        self.center_target_camera(player)

        #ground
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.ground_surf,ground_offset)
        
        #active elements (player, etc)
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

#initializing pygame, the screen and the clock.
pygame.init()
screen = pygame.display.set_mode((800,620))
clock = pygame.time.Clock()

#camera setup
camera_group = CameraGroup()

#spawn player
player = Player((640, 360), camera_group)

#spawning trees
for i in range(20):
    random_x = randint(0,1000)
    random_y = randint(0,1000)
    Tree((random_x,random_y), camera_group)

#main loop execution
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('#71ddee')
    camera_group.update()
    camera_group.custom_draw(player)
    pygame.display.update()
    clock.tick(60)
