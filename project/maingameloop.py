#Necessary libraries
import random
import pygame
#import data.screenrefresher

class Mainloop():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Two objects collecting items. Rounds played:")

        self.silmukka()

#Pelaajan liikkeet/painallukset ja niiden laukaisemat tapahtumafunktiot
    def event_observer(self):
        for keyPress in pygame.event.get():
            if keyPress.type == pygame.QUIT:
                exit()

    #Updating loop
    def silmukka(self):
        while True:
            self.event_observer()
            self.draw_screen()
            self.clock.tick(60)


#Näytön päivitys.

    def draw_screen(self):
        self.display.fill((250, 250, 250))

        #THIS UPDATES
        pygame.display.flip()
        self.clock.tick(60)

#Calling the main loop that creates the window and game
if __name__ == "__main__":
    Mainloop()
