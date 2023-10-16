import pygame
from data.assets.images import health_anim_icon,cat_HUD_icon
from data.init_groups import found_cats
from data.settings import quest_length

def hellobutton():
    print("Hello, I am a Button!")

class HealthBar(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,health):
    #def __init__(self,x,y,health):
        super().__init__()
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        self.health = health
        self.maxhealth = health
        self.fill_color = "#00000000"
        self.images = health_anim_icon
        if health > len(self.images)-1:
            self.health = len(self.images)
            self.maxhealth = len(self.images)-1
        self.image = self.images[self.maxhealth]
        self.bar_surface = pygame.Surface((width, height),pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(self.pos_x,self.pos_y))

    def hp_update(self,playerhealth):
        self.health = min(self.maxhealth,playerhealth)
        if self.health >= 0:
            self.image = self.images[self.health]
        else: 
            self.image = self.images[0]
            print("Invalid HP range!")

    def update(self,screen):
        # Color the box
        self.bar_surface.fill(self.fill_color)
        # Blit the surface containing the button text
        self.bar_surface.blit(self.image, [
            self.rect.width/2 - self.image.get_rect().width/2,
            self.rect.height/2 - self.image.get_rect().height/2
        ])
        # Blit everything to the screen
        screen.blit(self.bar_surface, self.rect)
        #screen.blit(self.image, self.rect)

class CatHUD(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.pos_x = x
        self.pos_y = y
        self.width = width
        self.height = height
        self.questprogress = found_cats
        self.quest_length = quest_length

        self.fill_color = "#00000000"
        self.image = cat_HUD_icon
        self.cat_bar = pygame.Surface((width, height),pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(self.pos_x,self.pos_y))

    def quest_progression(self,catname):
        self.questprogress = len(found_cats)
        

    def update(self,screen):
        # Color the box
        self.cat_bar.fill(self.fill_color)
        self.font = pygame.font.SysFont("Arial", 14)
        # Blit the surface containing the button text
        for i in range(len(self.questprogress)):
            self.cat_bar.blit(self.image,[i*28,0])

        # self.bar_surface.blit(self.image, [
        #     self.rect.width/2 - self.image.get_rect().width/2,
        #     self.rect.height/2 - self.image.get_rect().height/2
        # ])
        
        # Blit everything to the screen
        screen.blit(self.cat_bar, self.rect)
        #screen.blit(self.image, self.rect)


class TextBox():
    def __init__(self,x,y,width,height,box_text="TextBox",font_val="default",fill_colors="#ffffff",
                 transparent=False,border=False,border_thickness=0,border_color="#333333"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Is box transparent? Otherwise set fill color
        if transparent:
            self.fill_colors = "#00000000"
            self.box_surface = pygame.Surface((width, height),pygame.SRCALPHA)
        else:
            self.fill_colors = fill_colors
            self.box_surface = pygame.Surface((width, height))
        # Border?
        self.border = border
        self.border_thickness = border_thickness
        self.border_color = border_color
        self.border_width = width+2*border_thickness
        self.border_height = height+2*border_thickness
        self.border_surface = pygame.Surface((self.border_width,self.border_height))
        self.border_rect = pygame.Rect(x-border_thickness,y-border_thickness,self.border_width,self.border_height)
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
        if transparent:
            self.fill_colors = {
                "normal": "#00000000",
                "hover": "#00000000",
                "pressed": "#00000000"
            }
            self.box_surface = pygame.Surface((width, height),pygame.SRCALPHA)
        else:
            self.fill_colors = {
                "normal": fill_colors[0],
                "hover": fill_colors[1],
                "pressed": fill_colors[2]
            }
            self.box_surface = pygame.Surface((width, height))

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
        
