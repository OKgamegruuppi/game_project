from creature import Creature

class Player(Creature):
    def __init__(self,name,pos_x,pos_y,dir_x,dir_y,speed,health,target,dmg):
        super().__init__(self,name,pos_x,pos_y,dir_x,dir_y,speed,health,target)
        self.dmg = dmg

    def attack(target):
        pass

    def itempickup():
        pass

