import pygame

#screenrefresher.py blitzes, fills, draws, updates etc. the display.

def draw_on_screen(self):
    self.display.fill((250, 250, 250))
    self.display.blit(self.background, (300, 300))
    self.borders.draw(self.display)
    # playergroup.update argument: Group of things player can collide with
    self.playergroup.update(self.enemies)
    self.playergroup.draw(self.display)
    # enemies.update argument: List of groups enemies can collide with
    self.enemies.update([self.borders,self.playergroup])
    self.enemies.draw(self.display)

    pygame.display.flip()
