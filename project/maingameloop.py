#cycle through all the main .py components of the game
#import creature.py, player.py etc. here
import data.screenrefresher
import pygame

class Mainloop():
    def __init__(self):
        pygame.init()
        global round_counter
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Stickman quest")
        self.silmukka()
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
            data.screenrefresher.draw_screen(self)
            self.clock.tick(60)

if __name__ == "__main__":
    Mainloop()