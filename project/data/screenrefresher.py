import pygame

def draw_screen(self):
    self.display.fill((250, 250, 250))
    #bg = pygame.image.load(main_game_loop.background_image)
    #self.display.blit()

    pygame.display.flip()
    self.clock.tick(60)