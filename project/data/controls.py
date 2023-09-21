import pygame

# Event observer for main menu(?)
def menu_event_observer(menuloop):
    for keyPress in pygame.event.get():
        if keyPress.type == pygame.KEYDOWN:
            if keyPress.key == pygame.K_UP:
                pass
                # Move menu selection up
            if keyPress.key == pygame.K_DOWN:
                pass
                # Move menu selection down
            if keyPress.key == pygame.K_LEFT:
                pass
                # Move menu selection left
            if keyPress.key == pygame.K_RIGHT:
                pass
                # Move menu selection right
            if keyPress.key == pygame.K_RETURN:
                pass
                # Choose current selection


def game_event_observer(player):
    for keyPress in pygame.event.get():
        if keyPress.type == pygame.KEYDOWN:
            # Movement
            if keyPress.key == pygame.K_UP:
                player.movement("up",True)
            if keyPress.key == pygame.K_DOWN:
                player.movement("down",True)
            if keyPress.key == pygame.K_LEFT:
                player.movement("left",True)
            if keyPress.key == pygame.K_RIGHT:
                player.movement("right",True)
            # Interact
            if keyPress.key == pygame.K_SPACE:
                pass

            # Pause Menu
            if keyPress.key == pygame.K_ESCAPE:
                pass
            # Inventory    
            if keyPress.key == pygame.K_i:
                pass
                
            # Etc

        if keyPress.type == pygame.KEYUP:
            if keyPress.key == pygame.K_UP:
                player.movement("up",False)
            if keyPress.key == pygame.K_DOWN:
                player.movement("down",False)
            if keyPress.key == pygame.K_LEFT:
                player.movement("left",False)
            if keyPress.key == pygame.K_RIGHT:
                player.movement("right",False)


        if keyPress.type == pygame.QUIT:
            exit()