import pygame

def hellobutton():
    print("Hello, I am a Button!")

class TextBox():
    def __init__(self, x, y, width, height, box_text="TextBox", font_val="default", fill_colors = "#ffffff"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Set button colors for different cases
        self.fill_colors = fill_colors
        # Define the Surface and Rect for the button, and the surface for the button text
        self.box_surface = pygame.Surface((self.width, self.height))
        self.box_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if font_val == "default":
            self.font = pygame.font.SysFont("Arial", 24)
        else:
            self.font = font_val
        self.box_text_surf = self.font.render(box_text, True, (20, 20, 20))

    def __str__(self):
        print("Hello, I am a TextBox!")

    def update(self,screen):
        # Color the box
        self.box_surface.fill(self.fill_colors)
            
        # Blit the surface containing the button text
        self.box_surface.blit(self.box_text_surf, [
            self.box_rect.width/2 - self.box_text_surf.get_rect().width/2,
            self.box_rect.height/2 - self.box_text_surf.get_rect().height/2
        ])
        # Blit everything to the screen
        screen.blit(self.box_surface, self.box_rect)

class Button(TextBox):
    def __init__(self, x, y, width, height, box_text="Button", onclick_function=hellobutton, one_press=False, font_val="default",
                 fill_colors = ["#ffffff","#666666","#333333"]):
        super().__init__(x, y, width, height, box_text, font_val, fill_colors)    
        self.onclick_function = onclick_function
        # if onePress == True -> If button pressed down, keep executing function
        self.onePress = one_press
        # Stop function from executing if alreadyPressed == True
        self.already_pressed = False
        # Set button colors for different cases
        self.fill_colors = {
            "normal": fill_colors[0],
            "hover": fill_colors[1],
            "pressed": fill_colors[2]
        }

    def __str__(self):
            print("Hello, I am a Button!")

    def update(self,screen):
        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()
        self.box_surface.fill(self.fill_colors["normal"])
        # If mouse is on Button, change color of button
        if self.box_rect.collidepoint(mouse_pos):
            self.box_surface.fill(self.fill_colors["hover"])
            # If mousebutton 1 (left-click) is pressed, change color, and run onclickfunction
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.box_surface.fill(self.fill_colors["pressed"])
                # If onePress True, keeping button held keeps executing the function over and over
                if self.one_press:
                    self.onclick_function()
                elif not self.already_pressed:
                    self.onclick_function()
                    self.already_pressed = True
            else:
                self.already_pressed = False
        # Blit the surface containing the button text
        self.box_surface.blit(self.box_text_surf, [
            self.box_rect.width/2 - self.box_text_surf.get_rect().width/2,
            self.box_rect.height/2 - self.box_text_surf.get_rect().height/2
        ])
        # Blit everything to the screen
        screen.blit(self.box_surface, self.box_rect)
        