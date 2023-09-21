import pygame

def event_observer(self):
    for keyPress in pygame.event.get():
        if keyPress.type == pygame.KEYDOWN:
            if keyPress.key == pygame.K_UP:
                self.up = True
            if keyPress.key == pygame.K_DOWN:
                self.down = True
            if keyPress.key == pygame.K_LEFT:
                self.left = True
            if keyPress.key == pygame.K_RIGHT:
                self.right = True

        if keyPress.type == pygame.KEYUP:
            if keyPress.key == pygame.K_UP:
                self.up = False
            if keyPress.key == pygame.K_DOWN:
                self.down = False
            if keyPress.key == pygame.K_LEFT:
                self.left = False
            if keyPress.key == pygame.K_RIGHT:
                self.right = False

        if keyPress.type == pygame.QUIT:
            exit()

