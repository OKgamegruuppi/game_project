#libraries
import pygame
import data.controls
from data.settings import windowsizeX, windowsizeY,fps
from data.game_update import game_update
from map.camera import CameraGroup
from data.init_groups import *
from map.init_map import *
from data.controls import game_event_observer


class Mainloop():
    def __init__(self):
        pygame.init()

        #initializing pygame, the screen and the clock.
        self.screen = pygame.display.set_mode((windowsizeX,windowsizeY))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("GAME WINDOW")

        ##initing the variables brought from init_map
        self.player = player

        #camera setup
        camera_group.append(CameraGroup())
        add_to_camera()
        self.gameEventLoop()


    #main loop execution
    def gameEventLoop(self):

        while True:
            game_event_observer(self)
            is_game_paused = data.controls.game_turned_on
            if is_game_paused == True:
                #print(f'GAME IS PAUSED? {self.game_pause_check}')
                self.screen.fill('#71ddee')
                #self.camera_group.update(self.grouplist)
                game_update(self)
                ##custom draw keeps player in the middle of the screen and draw all elements in camera group
                camera_group[0].custom_draw(self.player)
                pygame.display.update()
                self.clock.tick(fps)

            #IF game_pause_check == True ==> PAUSE THE GAME
            else:
                style_of_font = pygame.font.SysFont("Arial", 24)
                displayed_text = style_of_font.render("PAUSED ||", True, (255, 250, 0))
                self.screen.blit(displayed_text, (10, 5))
                pygame.display.update()


#Calling the main loop that creates the window and game
if __name__ == "__main__":
    Mainloop()
