import pygame

# Event observer for main menu(?)
def menu_event_observer():
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

# Arguments are player Sprite, and a Group of enemies to attack
def game_event_observer(player,enemies):
    for keyPress in pygame.event.get():
        if keyPress.type == pygame.KEYDOWN:
            # Movement
            if keyPress.key == pygame.K_UP or keyPress.key == pygame.K_w:
                player.move["up"] = True
            if keyPress.key == pygame.K_DOWN or keyPress.key == pygame.K_s:
                player.move["down"] = True
            if keyPress.key == pygame.K_LEFT or keyPress.key == pygame.K_a:
                player.move["left"] = True
            if keyPress.key == pygame.K_RIGHT or keyPress.key == pygame.K_d:
                player.move["right"] = True
            # Attack
            if keyPress.key == pygame.K_SPACE:
                player.attack(enemies)
            # Interact
            if keyPress.key == pygame.K_f:
                player.interact()

            # Pause Menu
            if keyPress.key == pygame.K_ESCAPE:
                pass
            # Inventory    
            if keyPress.key == pygame.K_i:
                pass
                
            # Etc

        if keyPress.type == pygame.KEYUP:
            if keyPress.key == pygame.K_UP or keyPress.key == pygame.K_w:
                player.move["up"] = False
            if keyPress.key == pygame.K_DOWN or keyPress.key == pygame.K_s:
                player.move["down"] = False
            if keyPress.key == pygame.K_LEFT or keyPress.key == pygame.K_a:
                player.move["left"] = False
            if keyPress.key == pygame.K_RIGHT or keyPress.key == pygame.K_d:
                player.move["right"] = False

        if keyPress.type == pygame.QUIT:
            exit()


