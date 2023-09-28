import pygame
import data.controls
from data.settings import windowsizeX, windowsizeY,fps
from data.game_update import game_update, ui_update
from map.camera import CameraGroup
from data.init_groups import *
from map.init_map import *
from data.controls import game_event_observer
from data.ui_elements import *

def pause_menu_update(screen):
    pausemenu_window = TextBox(windowsizeX/4,windowsizeY/4,windowsizeX/2,windowsizeY/2,"Game Paused")
    pause_menu_button_1 = Button(windowsizeX/3,windowsizeY/3,windowsizeX/3,windowsizeY/3,"CONTINUE",data.controls.pause_game)
                
    pausemenu_window.update(screen)
    pause_menu_button_1.update(screen)

def game_over_screen(screen):
    gameover_window = TextBox(windowsizeX/4,windowsizeY/4,windowsizeX/2,windowsizeY/2,"YOU DIED!\nGAME OVER!")
    gameover_button_1 = Button(windowsizeX/3,windowsizeY/3,windowsizeX/3,windowsizeY/3,"Exit",data.controls.exit_game)
                
    gameover_window.update(screen)
    gameover_button_1.update(screen)