#kirjastot
import random
import pygame

##############################
#Olioiden luonnit
########################
#1st movable object
class Object_1:
    def __init__(self):
        self.obj_one = pygame.image.load("object_1.png")
    def spawn_obj1(self):
        return [self.obj_one, self.obj_one.get_width(), self.obj_one.get_height()]
#2nd movable object
class Object_2:
    def __init__(self):
        self.obj_two = pygame.image.load("object_2.png")
    def spawn_obj2(self):
        return [self.obj_two, self.obj_two.get_width(), self.obj_two.get_height()]
#The collectable item
class Object_3:
    def __init__(self, obj_3_x_coord, obj_3_y_coord):
        self.obj_3_img = pygame.image.load("object_3.png")
        self.x_coor = obj_3_x_coord
        self.y_coor = obj_3_y_coord
        self.obj_3_rect = (self.x_coor, self.y_coor, self.obj_3_img.get_width() / 2, self.obj_3_img.get_height() / 2)
    def mint_new_coin(self):
        return [self.obj_3_img, (self.x_coor, self.y_coor), (self.obj_3_rect)]

###############################
#Pääluuppi
########################
round_counter = 0
class Mainloop():
    def __init__(self):
        pygame.init()
        global round_counter
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((1080, 720))                                                     #pygame.display.set_mode((1000,720),pygame.FULLSCREEN) mahdollistaa kokonäytöntilan
        pygame.display.set_caption("Two objects collecting items. Rounds played: "+str(round_counter))

        self.object_hit_index = []
        self.available_object_3s = []

        for x in range(10):
            self.spawned_obj3 = Object_3(random.randint(0, 800), random.randint(40, 650))
            spawn_data = Object_3.mint_new_coin(self.spawned_obj3)
            self.available_object_3s.append(spawn_data)
            self.object_hit_index.append(spawn_data[2])

        self.silmukka()

#Pelaajan liikkeet/painallukset ja niiden laukaisemat tapahtumafunktiot
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
                if keyPress.key == pygame.K_RETURN:
                    self.on_alkanut = True
                if keyPress.key == pygame.K_p:
                    Mainloop()
            if keyPress.type == pygame.KEYUP:
                if keyPress.key == pygame.K_UP:
                    self.up = False
                if keyPress.key == pygame.K_DOWN:
                    self.down = False
                if keyPress.key == pygame.K_LEFT:
                    self.left = False
                if keyPress.key == pygame.K_RIGHT:
                    self.right = False
            if keyPress.type == pygame.KEYDOWN:
                if keyPress.key == pygame.K_w:
                    self.button_w = True
                if keyPress.key == pygame.K_s:
                    self.button_s = True
                if keyPress.key == pygame.K_a:
                    self.button_a = True
                if keyPress.key == pygame.K_d:
                    self.button_d = True
            if keyPress.type == pygame.KEYUP:
                if keyPress.key == pygame.K_w:
                    self.button_w = False
                if keyPress.key == pygame.K_s:
                    self.button_s = False
                if keyPress.key == pygame.K_a:
                    self.button_a = False
                if keyPress.key == pygame.K_d:
                    self.button_d = False

            if keyPress.type == pygame.QUIT:
                exit()

    #Updating loop
    def silmukka(self):
        self.obj2_collision_points = 0
        self.obj1_collision_points = 0

        #objekti 1:n koordinnaatit ja napit
        self.obj_2_pos_x = 30
        self.obj_2_pos_y = 30
        self.up = False
        self.down = False
        self.left = False
        self.right = False

        #objekti 2:n koordinaatit ja napit
        self.obj1_pos_x = 800
        self.obj1_pos_y = 30
        self.button_w = False
        self.button_s = False
        self.button_a = False
        self.button_d = False

        while True:
            self.event_observer()
            self.draw_screen()
            self.clock.tick(60)

#Näytön päivitys.
    def draw_screen(self):
        if len(self.available_object_3s) < 1: #peli ohi
            global round_counter
            round_counter += 1
            Mainloop()
        self.display.fill((250, 250, 250))

        self.font_setting = pygame.font.SysFont("Arial", 15)
        self.obj2_collision_counter = self.font_setting.render(f"Object_2 collisions with Object_3: {str(self.obj2_collision_points)}",True, (255, 100, 0))
        self.obj1_collision_counter = self.font_setting.render(f"Object_1 collisions with Object_3: {str(self.obj1_collision_points)}", True, (255, 100, 0))
        self.display.blit(self.obj2_collision_counter, (100, 0))
        self.display.blit(self.obj1_collision_counter, (500, 0))


        self.object_2s_information = Object_1().spawn_obj1()
        self.object_2_block = self.object_2s_information[0]
        self.display.blit(self.object_2_block, (self.obj_2_pos_x, self.obj_2_pos_y))
        self.obj_1_rect = pygame.Rect(self.obj_2_pos_x, self.obj_2_pos_y,
                                      self.object_2_block.get_width() / 2, self.object_2_block.get_height() / 2)

        self.object_1s_information = Object_2().spawn_obj2()
        self.object_1_block = self.object_1s_information[0]
        self.display.blit(self.object_1_block, (self.obj1_pos_x, self.obj1_pos_y))
        self.rect2 = pygame.Rect(self.obj1_pos_x, self.obj1_pos_y,
                                 self.object_1_block.get_width() / 2, self.object_1_block.get_height() / 2)

        self.obj3_image = pygame.image.load("object_3.png")

        #luodaan itemit näytölle
        num = 0
        for new_ones in range(len(self.available_object_3s)):
            self.display.blit(self.obj3_image, (self.available_object_3s[num][1]))
            num += 1

        if self.up and self.obj_2_pos_y > 30:
            self.obj_2_pos_y -= 5
        if self.down and self.obj_2_pos_y + self.object_2s_information[2] < 720:
            self.obj_2_pos_y += 5
        if self.left and self.obj_2_pos_x > 0:
            self.obj_2_pos_x -= 5
        if self.right and self.obj_2_pos_x + self.object_2s_information[1] < 1080 :
            self.obj_2_pos_x += 5

        if self.button_w and self.obj1_pos_y > 30:
            self.obj1_pos_y -= 5
        if self.button_s and self.obj1_pos_y + self.object_1s_information[2] < 720:
            self.obj1_pos_y += 5
        if self.button_a and self.obj1_pos_x > 0:
            self.obj1_pos_x -= 5
        if self.button_d and self.obj1_pos_x + self.object_1s_information[1] < 1080 :
            self.obj1_pos_x += 5

       # if self.rect1.colliderect(self.rect2): #If Object_1 & Object_2 collide
        #    Peli()

        lookup_obj1_index = -1
        for lookup in self.object_hit_index:
            lookup_obj1_index += 1
            if self.obj_1_rect.colliderect(lookup):
                self.object_hit_index.pop(lookup_obj1_index)
                self.available_object_3s.pop(lookup_obj1_index)
                self.obj2_collision_points += 1

        lookup_obj2_index = -1
        for lookup2 in self.object_hit_index:
            lookup_obj2_index += 1
            if self.rect2.colliderect(lookup2):
                self.object_hit_index.pop(lookup_obj2_index)
                self.available_object_3s.pop(lookup_obj2_index)
                self.obj1_collision_points += 1

        pygame.display.flip()
        self.clock.tick(60)

#Calling the main loop that creates the window and game
if __name__ == "__main__":
    Mainloop()
