import pygame
from data.init_groups import *

info_freq = 0

def game_update(game):
    #game.camera_group.update(game.grouplist)
    enemies.update(game.player)
    # game.enemies.update(game.player,game.friendlies,game.grouplist,game.camera_group)
    friendlies.update()
    playergroup.update()
    effectsgroup.update()

    global info_freq
    info_freq += 1

    if info_freq > 60:
        for enemy in enemies:
            enemy.info()
        info_freq = 0
