import pygame
from random import randint
from data.settings import fps as onesecond

class Effect(pygame.sprite.Sprite):
    # Class containing special effects

    def __init__(self,name,image,pos_x=0,pos_y=0,timer=onesecond,jitter=0):
        super().__init__()
        self.jitter = randint(-jitter,jitter)
        self.name = name
        self.image = image
        self.pos_x = pos_x + self.jitter
        self.pos_y = pos_y + self.jitter
        self.timer = timer
        self.rect = self.image.get_rect(center=(self.pos_x,self.pos_y))

    # Reduce timer by one, when reaches 0, kill Effect
    def update(self,*args):
        if self.timer > 0:
            self.timer -= 1 
        else: 
            self.kill()      
