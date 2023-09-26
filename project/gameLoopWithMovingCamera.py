#libraries
import pygame
from random import randint
from data.settings import windowsizeX, windowsizeY,fps
from map.camera import CameraGroup
from map.init_map import grouplist,enemies,player,effects,add_to_camera
from data.controls import game_event_observer


class Mainloop():
    def __init__(self):
        pygame.init()

        #initializing pygame, the screen and the clock.
        self.screen = pygame.display.set_mode((windowsizeX,windowsizeY))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("GAME WINDOW")

        self.enemies = enemies
        self.player = player
        self.grouplist = grouplist
        self.effects = effects

            #camera setup
        self.camera_group = CameraGroup()
        add_to_camera(self.camera_group)
        self.gameEventLoop()
    
    #main loop execution
    def gameEventLoop(self):
        while True:
            game_event_observer(self.player,self.enemies,self.effects)
            
            self.screen.fill('#71ddee')
            
            self.camera_group.update(self.grouplist)
            self.camera_group.custom_draw(player)
            pygame.display.update()
            self.clock.tick(fps)

#Calling the main loop that creates the window and game
if __name__ == "__main__":
    Mainloop()
