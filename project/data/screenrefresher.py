import pygame

def draw_on_screen(self):
    self.display.fill((250, 250, 250))
    self.display.blit(self.background, (300, 300))
    self.playergroup.update(self.enemies)
    self.playergroup.draw(self.display)
    self.enemies.update()
    self.enemies.draw(self.display)
    pygame.display.flip()
