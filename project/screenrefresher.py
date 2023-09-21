

def refreshdisplay(self):
  print(".blit objects onto the screen")
  self.display.fill((250, 250, 250)) #täyttää näytön valkoisella, RBG koodit.



  
  pygame.display.flip() #näytön päivitys
  self.clock.tick(60) # näytön päivitys

