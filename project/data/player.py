from creature import Creature

class Player(Creature):
    def __init__(self,name,pos_x,pos_y,speed,health,target,dmg):
        super().__init__(self,name,pos_x,pos_y,dir_x,dir_y,speed,health,target)
        self.dmg = dmg

    def movement(self,up,down,left,right):
        self.pos_x += dir * speed
        self.pos_y += dir * speed
    def attack(target):
        pass

    def itempickup():
        pass

