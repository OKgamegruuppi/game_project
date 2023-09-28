#libraries
import pygame
import data.controls
from data.settings import windowsizeX, windowsizeY,fps
from data.game_update import game_update, ui_update
from map.camera import CameraGroup
from data.init_groups import *
from map.init_map import *
from data.controls import game_event_observer
from data.ui_elements import *

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
                ui_update(self)
                pygame.display.update()
                self.clock.tick(fps)

            #IF is_game_paused == False ==> PAUSE THE GAME
            #Draw the pause menu stuff inside the else
            else:
                pausemenu_window = TextBox(windowsizeX/4,windowsizeY/4,windowsizeX/2,windowsizeY/2)
                pause_menu_button_1 = Button(windowsizeX/3,windowsizeY/3,windowsizeX/3,windowsizeY/3,"CONTINUE",data.controls.pause_game)
                
                pausemenu_window.update(screen=self.screen)
                pause_menu_button_1.update(screen=self.screen)
                
                pygame.display.flip()
                pygame.display.update()

#Calling the main loop that creates the window and game
if __name__ == "__main__":
    Mainloop()
