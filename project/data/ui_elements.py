import pygame

def hellobutton():
    print("Hello, I am a Button!")

class TextBox():
    def __init__(self,x,y,width,height,box_text="TextBox",font_val="default",fill_colors="#ffffff",
                 transparent=False,border=False,border_thickness=0,border_color="#333333"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Is box transparent?
        self.transparent = transparent
        # Border?
        self.border = border
        self.border_thickness = border_thickness
        self.border_color = border_color
        self.border_width = width+2*border_thickness
        self.border_height = height+2*border_thickness
        self.border_surface = pygame.Surface((self.border_width,self.border_height))
        self.border_rect = pygame.Rect(x-border_thickness,y-border_thickness,self.border_width,self.border_height)
        # Set button colors for different cases
        self.fill_colors = fill_colors
        # Define the Surface and Rect for the button, and the surface for the button text
        self.box_surface = pygame.Surface((width, height))
        self.box_rect = pygame.Rect(x, y, width, height)
        if font_val == "default":
            self.font = pygame.font.SysFont("Arial", 24)
        else:
            self.font = font_val
        self.box_text_surf = self.font.render(box_text, True, (20, 20, 20))

    def __str__(self):
        print("Hello, I am a TextBox!")

    def update(self,screen):
        # Color the box
        if not self.transparent:
            self.box_surface.fill(self.fill_colors)
            
        # Blit the surface containing the button text
        self.box_surface.blit(self.box_text_surf, [
            self.box_rect.width/2 - self.box_text_surf.get_rect().width/2,
            self.box_rect.height/2 - self.box_text_surf.get_rect().height/2
        ])
        # Blit everything to the screen
        if self.border:
            self.border_surface.fill(self.border_color)
            screen.blit(self.border_surface,self.border_rect)
        screen.blit(self.box_surface, self.box_rect)

class Button(TextBox):
    def __init__(self,x,y,width,height,box_text="Button",onclick_function=hellobutton,onePress=False,font_val="default",
                 fill_colors=["#ffffff","#666666","#333333"],transparent=False,border=False,border_thickness=0,border_color="#333333"):
        super().__init__(x,y,width,height,box_text,font_val,fill_colors,transparent,border,border_thickness,border_color)    
        self.onclick_function = onclick_function
        # if onePress == True -> If button pressed down, keep executing function
        self.onePress = onePress
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
        if not self.transparent:
            self.box_surface.fill(self.fill_colors["normal"])
        # If mouse is on Button, change color of button
        if self.box_rect.collidepoint(mouse_pos):
            if not self.transparent:
                self.box_surface.fill(self.fill_colors["hover"])
            # If mousebutton 1 (left-click) is pressed, change color, and run onclickfunction
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                if not self.transparent:
                    self.box_surface.fill(self.fill_colors["pressed"])
                # If onePress True, keeping button held keeps executing the function over and over
                if self.onePress:
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
        if self.border:
            self.border_surface.fill(self.border_color)
            screen.blit(self.border_surface,self.border_rect)
        screen.blit(self.box_surface, self.box_rect)
        
