

def refreshdisplay(self):
  print(".blit objects onto the screen")
  self.display.fill((250, 250, 250)) #fills the screen with white, RBG


  
  pygame.display.flip() # refreshing the display
  self.clock.tick(60) # refreshing the display

