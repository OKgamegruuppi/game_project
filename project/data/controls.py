import pygame
from data.settings import game_state

# Function that starts the game
def start_game():
    if game_state["MainMenu"] == True:
        game_state["MainMenu"] = False
        game_state["GamePaused"] = False
        return True
    else:
        return False

# Function that pauses game
def pause_game():
    if game_state["GamePaused"] == False:
        game_state["GamePaused"] = True
        return game_state["GamePaused"]
    else:
        game_state["GamePaused"] = False
        return game_state["GamePaused"]

# Function to exit game    
def exit_game():
    exit()

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


######NEW
game_turned_on = True
# Arguments are player Sprite, and a Group of enemies to attack
def game_event_observer(game):
    #global game_turned_on #######NEW
    for keyPress in pygame.event.get():
        if keyPress.type == pygame.KEYDOWN:
            # Movement
            if keyPress.key == pygame.K_UP or keyPress.key == pygame.K_w:
                game.player.move["up"] = True
            if keyPress.key == pygame.K_DOWN or keyPress.key == pygame.K_s:
                game.player.move["down"] = True
            if keyPress.key == pygame.K_LEFT or keyPress.key == pygame.K_a:
                game.player.move["left"] = True
            if keyPress.key == pygame.K_RIGHT or keyPress.key == pygame.K_d:
                game.player.move["right"] = True
            # Attack
            if keyPress.key == pygame.K_SPACE:
                game.player.attack()
            # Interact
            if keyPress.key == pygame.K_f:
                game.player.interact()
            # Inventory
            if keyPress.key == pygame.K_i:
                game.player.check_inventory()

            # Quit Game
            if keyPress.key == pygame.K_ESCAPE:
                exit_game()
            # Inventory    
            if keyPress.key == pygame.K_i:
                pass
            
            # Pause Game
            if keyPress.key == pygame.K_p:
                pause_game()
            # Etc

        if keyPress.type == pygame.KEYUP:
            if keyPress.key == pygame.K_UP or keyPress.key == pygame.K_w:
                game.player.move["up"] = False
            if keyPress.key == pygame.K_DOWN or keyPress.key == pygame.K_s:
                game.player.move["down"] = False
            if keyPress.key == pygame.K_LEFT or keyPress.key == pygame.K_a:
                game.player.move["left"] = False
            if keyPress.key == pygame.K_RIGHT or keyPress.key == pygame.K_d:
                game.player.move["right"] = False

        if keyPress.type == pygame.QUIT:
            exit()


