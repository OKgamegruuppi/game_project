

def refreshdisplay(self):
  print(".blit objects onto the screen")
  self.display.fill((250, 250, 250))



  
  pygame.display.flip()
  self.clock.tick(60)



if __name__ == "__main__":
  refreshdisplay()
  
