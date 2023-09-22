#Necessary libraries
import pygame
#import data.player
#import data.controls

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
        self.gameEventLoop()

#Pelaajan liikkeet/painallukset ja niiden laukaisemat tapahtumafunktiot.
    def event_observer(self):
        for keyPress in pygame.event.get():
            if keyPress.type == pygame.QUIT:
                exit()

#Updating loop
    def gameEventLoop(self):
        while True:
            self.event_observer()
            self.draw_screen()
            self.clock.tick(60)

#Refreshing the screen.
    def draw_screen(self):
        self.display.fill((250, 250, 250))
        self.display.blit(self.background, (300, 300))
        pygame.display.flip()
        self.clock.tick(60)

#Calling the main loop that creates the window and game
if __name__ == "__main__":
    Mainloop()
