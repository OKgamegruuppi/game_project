#libraries
import pygame
from data.settings import windowsizeX, windowsizeY,fps,game_state, progression
from data.ui_elements import *
from data.game_update import game_update, ui_update
from map.camera import CameraGroup
 
from map.init_map import *
from map.clear_map import clear_map
from data.controls import game_event_observer
from data.menus import pause_menu_update, game_over_screen, WIN_screen,start_screen

class Mainloop():
    def __init__(self):
        pygame.init()

        #initializing pygame, the screen and the clock.
        self.screen = pygame.display.set_mode((windowsizeX,windowsizeY))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("GAME WINDOW")

        ##initing the variables brought from init_map
        initialize_game()
        self.player = player

        #camera setup
        if camera_group.__len__() == 0:
            camera_group.append(CameraGroup())
        add_to_camera()
        print(camera_group)
        self.gameEventLoop()

    #main loop execution
    def gameEventLoop(self):

        while True:
            if game_state["Restarting"]:
                game_state["Restarting"] = False
                print("RESTARTING")
                clear_map()
                Mainloop()
            game_event_observer(self)
            # If player dead, print game over screen
            if game_state["MainMenu"]:
                start_screen(self.screen)
                pygame.display.flip()
                pygame.display.update()

            elif not game_state["PlayerAlive"]:
                game_over_screen(self.screen)

                pygame.display.flip()
                pygame.display.update()

            elif progression["Quest"] == quest_length:
                WIN_screen(self.screen)
                pygame.display.flip()
                pygame.display.update()

            elif not game_state["GamePaused"]:
                #print(f'GAME IS PAUSED? {self.game_pause_check}')
                self.screen.fill('#71ddee')
                #self.camera_group.update(self.grouplist)
                game_update(self)
                ##custom draw keeps player in the middle of the screen and draw all elements in camera group
                camera_group[0].custom_draw(self.player)
                ui_update(self)
                pygame.display.update()
                self.clock.tick(fps)

            #IF is_game_paused == True ==> PAUSE THE GAME
            #Draw the pause menu stuff inside the else
            elif game_state["GamePaused"]:
                pause_menu_update(self.screen)
                
                pygame.display.flip()
                pygame.display.update()
            else:
                continue

#Calling the main loop that creates the window and game
if __name__ == "__main__":
    Mainloop()
