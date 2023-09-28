import pygame
from data.init_groups import *

info_freq = 0

def game_update(game):
    #game.camera_group.update(game.grouplist)
    enemies.update(game.player)
    # game.enemies.update(game.player,game.friendlies,game.grouplist,game.camera_group)
    friendlies.update()
    itemgroup.update()
    questgroup.update()
    playergroup.update()
    effectsgroup.update()

    global info_freq
    info_freq += 1

    if info_freq > 60:
        for enemy in enemies:
            enemy.info()
        for item in itemgroup:
            item.info()
        info_freq = 0

def ui_update(game):
    # Update all UI elements that are visible:
    for element in uigroup:
        element.update(game.screen)
