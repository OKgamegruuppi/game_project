import random
import pygame

import eventObserver
import screenDrawer #draws the screen

#important changing variables
screen_wid = int(1000)
screen_hei = int(960)
round_counter = 0
player_speed = 5
player_image = "assets/player_character.png"
item1_image = "assets/item1.png"
item1_spawn_amount = 30
quest_status = "Pick berries, lol" #load more of these from a file
background_image = "assets/bg.png"

class PlayerCharacter:
    def __init__(self):
        self.player_char = pygame.image.load(player_image)
    def spawn_player_char(self):
        return [self.player_char, self.player_char.get_width(), self.player_char.get_height()]
class Item1:
    def __init__(self, item1_x_coord, item1_y_coord):
        self.item1_img = pygame.image.load(item1_image)
        self.x_coor = item1_x_coord
        self.y_coor = item1_y_coord
        self.item1_rect = (self.x_coor, self.y_coor, self.item1_img.get_width() / 2, self.item1_img.get_height() / 2)
    def mint_new_item1(self):
        return [self.item1_img, (self.x_coor, self.y_coor), (self.item1_rect)]

class Mainloop():
    def __init__(self):
        pygame.init()
        global round_counter
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((screen_wid, screen_hei), pygame.FULLSCREEN)
        pygame.display.set_caption("Stickman quest")

        self.item1_hit_index = []
        self.available_item1s = []

        #luodaan pelille kerättävät esineet
        for x in range(item1_spawn_amount):
            self.spawned_obj3 = Item1(random.randint(0, screen_wid - 50), random.randint(40, screen_hei - 50))
            spawn_data = Item1.mint_new_item1(self.spawned_obj3)
            self.available_item1s.append(spawn_data)
            self.item1_hit_index.append(spawn_data[2])

        self.silmukka()
    #Updating loop
    def silmukka(self):
        self.player_char_collision_points = 0

        #eventObserver tarkistaa
        self.player_char_pos_x = 30
        self.player_char_pos_y = 30
        self.up = False
        self.down = False
        self.left = False
        self.right = False

        while True:
            eventObserver.event_observer(self) #kutsutaan eventObserver.py
            screenDrawer.draw_screen(self) #kutsutaan screenDrawer.py
            self.clock.tick(60)

if __name__ == "__main__":
    Mainloop()
