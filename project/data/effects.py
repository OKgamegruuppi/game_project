import pygame
from data.settings import fps as onesecond

player_attack = pygame.image.load("data/assets/attack.png")
blood_red = pygame.image.load("data/assets/blood_red1.png")
small_heart = pygame.image.load("data/assets/small_heart.png")

class Effect(pygame.sprite.Sprite):
    # Class containing special effects

    def __init__(self,name,image,pos_x=0,pos_y=0,timer=onesecond):
        super().__init__()
        self.name = name
        self.image = image
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.timer = timer
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))

    # Reduce timer by one, when reaches 0, kill Effect
    def update(self,*args):
        if self.timer > 0:
            self.timer -= 1 
        else: 
            self.kill()      
