import pygame
from data.creature import Creature

class Player(Creature):
    def __init__(self,name,image,pos_x,pos_y,dir,speed=5,health=10,target=None,status={},awareness=0,dmg=1):
        super().__init__(name,image,pos_x,pos_y,dir,speed,health,target,status,awareness)     
        self.dmg = dmg

        # Determine if player is moving in any direction
        self.move = {
            "up" : False,
            "down": False,
            "left": False,
            "right": False
        }

    def __str__(self):
        print(self.name)
    
    # Move player character if self.move == True
    # Check if moving causes a collision, if so, don't move!
    def movement(self,group):
        if self.move["right"] == True:
            self.pos_x += self.speed
            self.rect = self.rect.move(self.speed,0)
            if pygame.sprite.spritecollideany(self,group):
                self.pos_x -= self.speed
                self.rect = self.rect.move(-self.speed,0)
            else:
                self.dir = (1,0)
        if self.move["left"] == True:
            self.pos_x -= self.speed
            self.rect = self.rect.move(-self.speed,0)
            if pygame.sprite.spritecollideany(self,group):
                self.pos_x += self.speed
                self.rect = self.rect.move(self.speed,0)
            else:
                self.dir = (-1,0)
        if self.move["up"] == True:
            self.pos_y -= self.speed
            self.rect = self.rect.move(0,-self.speed)
            if pygame.sprite.spritecollideany(self,group):
                self.pos_y += self.speed
                self.rect = self.rect.move(0,self.speed)
            else:
                self.dir = (0,-1)
        if self.move["down"] == True:
            self.pos_y += self.speed
            self.rect = self.rect.move(0,self.speed)
            if pygame.sprite.spritecollideany(self,group):
                self.pos_y -= self.speed
                self.rect = self.rect.move(0,-self.speed)
            else:
                self.dir = (0,1)

    def attack(self,target):
        pass

    def itempickup(self,target):
        pass

    def interact(self,target=None):
        print("Nothing to interact with!")
    
    # group = Group of sprites that the player might collide with
    def update(self,group):
        self.movement(group)        
        #pygame.draw.rect(screen,"#333333",self.hitbox)
        #screen.blit(self.image,(self.pos_x,self.pos_y))