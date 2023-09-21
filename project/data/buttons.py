import pygame

def hellobutton():
    print("Hello, I am a Button!")

class Button():
    def __init__(self, x, y, width, height, buttonText="Button", onclickFunction=hellobutton(), 
                 font=pygame.font.SysFont("Arial", 40), fillColors = ["#ffffff","#666666","#333333"], onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        # Set button colors for different cases
        self.fillColors = {
            "normal": fillColors[0],
            "hover": fillColors[1],
            "pressed": fillColors[2]
        }
        # Define the Surface and Rect for the button, and the surface for the button text
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = font
        self.buttonSurf = self.font.render(buttonText, True, (20, 20, 20))

    def __str__(self):
            print("Hello, I am a Button!")

    def process(self,screen):
        # Get mouse position
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors["normal"])
        # If mouse is on Button, change color of button
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors["hover"])
            # If mousebutton 1 (left-click) is pressed, change color, and run onclickfunction
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors["pressed"])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        # Blit the surface containing the button text
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        # Blit everything to the screen
        screen.blit(self.buttonSurface, self.buttonRect)

