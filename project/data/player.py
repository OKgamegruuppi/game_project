from creature import Creature

class Player(Creature):
    def __init__(self,name,pos_x,pos_y,speed,health=0,target=None,status={},dmg=1):
        super().__init__(self,name,pos_x,pos_y,speed,health,target,status={})
        self.dmg = dmg

    def movement(self,up,down,left,right):
        
        if right:
            self.pos_x += self.speed
        if left:
            self.pos_x -= self.speed
        if up:
            self.pos_y += self.speed
        if down:
            self.pos_y -= self.speed

    def attack(self,target):
        pass

    def itempickup(self,target):
        pass

    def interact(self,target):
        pass
