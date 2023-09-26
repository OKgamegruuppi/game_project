import pygame
info_freq = 0

def game_update(game):
    #game.camera_group.update(game.grouplist)
    game.enemies.update(game.player,game.grouplist)
    # game.enemies.update(game.player,game.friendlies,game.grouplist,game.camera_group)
    game.friendlies.update(game.grouplist)
    game.playergroup.update(game.grouplist)
    game.effects.update()

    global info_freq
    info_freq += 1

    if info_freq > 60:
        for enemy in game.enemies:
            enemy.info()
        info_freq = 0
