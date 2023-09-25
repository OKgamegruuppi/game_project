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
        self.display.fill('#71ddee')
        pygame.display.set_caption("GAME WINDOW")
        
        self.enemies = enemies
        self.player = player
        self.grouplist = grouplist

        self.gameEventLoop()

#Updating loop
    def gameEventLoop(self):
        while True:
            game_event_observer(self.player,self.enemies)
            #camera_group.update()
            #camera_group.custom_draw(player)
            draw_on_screen(self)
            self.clock.tick(60)


#Calling the main loop that creates the window and game
if __name__ == "__main__":
    Mainloop()
