import pygame
import data.controls
from data.settings import windowsizeX, windowsizeY,fps,progression
from data.game_update import game_update, ui_update
from map.camera import CameraGroup
from data.init_groups import *
from map.init_map import *
from data.controls import game_event_observer
from data.ui_elements import *

def start_screen(screen):
    cats = progression["Quest"]
    gamestart_window = TextBox(windowsizeX/4,windowsizeY/4,windowsizeX/2,windowsizeY/2,f"Your quest is to find all cats! Cats:{cats}/{quest_length}")
    gamestart_button_1 = Button(windowsizeX/2-50,windowsizeY*3/4-50,100,50,"START",data.controls.start_game)
                
    gamestart_window.update(screen)
    gamestart_button_1.update(screen)

def pause_menu_update(screen):
    cats = progression["Quest"]
    pausemenu_window = TextBox(windowsizeX/3,windowsizeY/4,windowsizeX/3,windowsizeY/2,f"Game Paused. Quest: find all {quest_length} cats. {cats}/{quest_length}")
    pause_menu_button_1 = Button(windowsizeX/2-50,windowsizeY*3/4-50,100,50,"CONTINUE",data.controls.pause_game)
                
    pausemenu_window.update(screen)
    pause_menu_button_1.update(screen)

def game_over_screen(screen):
    moneys = progression["Currency"]
    gameover_window = TextBox(windowsizeX/4,windowsizeY/4,windowsizeX/2,windowsizeY/2,f"YOU DIED! GAME OVER! Money: {moneys}")
    gameover_button_1 = Button(windowsizeX/2-50,windowsizeY*3/4-50,100,50,"Exit",data.controls.exit_game)
                
    gameover_window.update(screen)
    gameover_button_1.update(screen)

def WIN_screen(screen):
    moneys = progression["Currency"]
    cats = progression["Quest"]
    gameWIN_window = TextBox(windowsizeX/4,windowsizeY/4,windowsizeX/2,windowsizeY/2,f"Quest COMPLETE! YOU WIN! Money: {moneys}, Cats:{cats}/{quest_length}")
    gameWIN_button_1 = Button(windowsizeX/2-50,windowsizeY*3/4-50,100,50,"Exit",data.controls.exit_game)
                
    gameWIN_window.update(screen)
    gameWIN_button_1.update(screen)