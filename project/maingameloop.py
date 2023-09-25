#Necessary libraries
from data.settings import windowsizeX, windowsizeY
from map.init_map import grouplist,enemies,player
from data.controls import game_event_observer
from data.screenrefresher import draw_on_screen
import pygame

background_image = "data/assets/ground.png"


class Mainloop():
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load(background_image)
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((windowsizeX, windowsizeY))
        pygame.display.set_caption("GAME WINDOW")
        
        self.enemies = enemies
        self.player = player
        self.grouplist = grouplist

        self.gameEventLoop()

#Updating loop
    def gameEventLoop(self):
        while True:
            game_event_observer(self.player,self.enemies)
            #self.draw_screen()
            draw_on_screen(self)
            self.clock.tick(60)
'''
#Refreshing the screen.
    def draw_screen(self):
        self.display.fill((250, 250, 250))
        self.display.blit(self.background, (300, 300))
        self.objects.update(self.objects2)
        self.objects.draw(self.display)
        self.objects2.update()
        self.objects2.draw(self.display)
        pygame.display.flip()
'''

#Calling the main loop that creates the window and game
if __name__ == "__main__":
    Mainloop()
