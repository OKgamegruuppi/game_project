import pygame

def draw_on_screen(self):
    self.display.fill((250, 250, 250))
    self.display.blit(self.background, (300, 300))
    self.objects.update(self.objects2)
    self.objects.draw(self.display)
    self.objects2.update()
    self.objects2.draw(self.display)
    pygame.display.flip()
