#Necessary libraries
from data.player import Player
from data.creature import Creature, Enemy
from data.controls import game_event_observer
import pygame

background_image = "alpha_stage.png"
windowsizeX = 1080
windowsizeY = 700

class Mainloop():
    def __init__(self):
        pygame.init()
        self.background = pygame.image.load(background_image)
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((windowsizeX, windowsizeY))
        pygame.display.set_caption("GAME WINDOW")

        # Load test images
        marcos = pygame.image.load("data/assets/slime_monster.png")
        cat1_ico = pygame.image.load("data/assets/Cat-sprite-stand.png")
        defaultEnemy_icon2 = pygame.image.load("data/assets/TEST_Light_balls_tree1.png")
        # Make objects, and add them to the Group    
        self.player = Player("Marcos Petriades",marcos,0,0,(0,0))
        cat1 = Creature("Cat",cat1_ico,400,300,(1,0),1,1,None,{"walking":40,"standing":0})
        defaultEnemy2 = Enemy("Green",defaultEnemy_icon2,800,600,(1,0),0,1)
        self.objects = pygame.sprite.GroupSingle(self.player)
        self.objects2 = pygame.sprite.Group(cat1,defaultEnemy2)

        self.gameEventLoop()

#Updating loop
    def gameEventLoop(self):
        while True:
            game_event_observer(self.player)
            self.draw_screen()
            self.clock.tick(60)

#Refreshing the screen.
    def draw_screen(self):
        self.display.fill((250, 250, 250))
        self.display.blit(self.background, (300, 300))
        self.objects.update(self.objects2)
        self.objects.draw(self.display)
        self.objects2.update()
        self.objects2.draw(self.display)
        pygame.display.flip()

#Calling the main loop that creates the window and game
if __name__ == "__main__":
    Mainloop()
