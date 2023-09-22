from data.creature import Creature

class Player(Creature):
    def __init__(self,name,icon,hitbox,pos_x,pos_y,dir,speed=5,health=10,target=None,status={},awareness=0,dmg=1):
        super().__init__(name,icon,hitbox,pos_x,pos_y,dir,speed,health,target,status,awareness)     
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
        
    def movement(self):
        if self.move["right"] == True:
            self.pos_x += self.speed
        if self.move["left"] == True:
            self.pos_x -= self.speed
        if self.move["up"] == True:
            self.pos_y += self.speed
        if self.move["down"] == True:
            self.pos_y -= self.speed

    def attack(self,target):
        pass

    def itempickup(self,target):
        pass

    def interact(self,target=None):
        print("Nothing to interact with!")
    
    def process(self,screen):
        self.movement()
        screen.blit(self.icon,(self.pos_x,self.pos_y))