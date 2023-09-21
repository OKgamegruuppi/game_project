import pygame

def draw_screen(self):
    self.display.fill((250, 250, 250))
    #THIS UPDATES
    pygame.display.flip()
    self.clock.tick(60)