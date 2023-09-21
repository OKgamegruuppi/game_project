#Necessary libraries
import pygame

class Mainloop():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("GAME WINDOW")

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

        #screenfresh.py creates/fetches objects
        #self.mustaneliö = pygame.draw.rect(self.display, (0,0,0), pygame.Rect(30, 30, 700, 700))


        #THIS UPDATES
        pygame.display.flip()
        self.clock.tick(60)

#Calling the main loop that creates the window and game
if __name__ == "__main__":
    Mainloop()
