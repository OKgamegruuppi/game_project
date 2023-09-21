import pygame

class Object_1:
    def __init__(self):
        self.moving_object_1 = pygame.image.load("imgs/object_1.png")
    def spawn_object_1(self):
        return [self.moving_object_1, self.moving_object_1.get_width(), self.moving_object_1.get_height()]
class Object_2:
    def __init__(self):
        self.moving_object_2 = pygame.image.load("imgs/object_2.png")
    def spawn_object_2(self):
        return [self.moving_object_2, self.moving_object_2.get_width(), self.moving_object_2.get_height()]

class GameLoop():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_1 = pygame.display.set_mode((640, 480))

        self.looping()

    def check_events(self):
        for event_triggers in pygame.event.get():
            if event_triggers.type == pygame.KEYDOWN:
                if event_triggers.key == pygame.K_UP:
                    self.up = True
                if event_triggers.key == pygame.K_DOWN:
                    self.down = True
                if event_triggers.key == pygame.K_LEFT:
                    self.left = True
                if event_triggers.key == pygame.K_RIGHT:
                    self.right = True

            if event_triggers.type == pygame.KEYUP:
                if event_triggers.key == pygame.K_UP:
                    self.up = False
                if event_triggers.key == pygame.K_DOWN:
                    self.down = False
                if event_triggers.key == pygame.K_LEFT:
                    self.left = False
                if event_triggers.key == pygame.K_RIGHT:
                    self.right = False

            if event_triggers.type == pygame.KEYDOWN:
                if event_triggers.key == pygame.K_w:
                    self.button_w = True
                if event_triggers.key == pygame.K_s:
                    self.button_s = True
                if event_triggers.key == pygame.K_a:
                    self.button_a = True
                if event_triggers.key == pygame.K_d:
                    self.button_d = True
            if event_triggers.type == pygame.KEYUP:
                if event_triggers.key == pygame.K_w:
                    self.button_w = False
                if event_triggers.key == pygame.K_s:
                    self.button_s = False
                if event_triggers.key == pygame.K_a:
                    self.button_a = False
                if event_triggers.key == pygame.K_d:
                    self.button_d = False

            if event_triggers.type == pygame.QUIT:
                exit()

    def looping(self):
        self.pos_x = 400
        self.pos_y = 30
        self.up = False
        self.down = False
        self.left = False
        self.right = False

        self.pos_x2 = 40
        self.pos_y2 = 30
        self.button_w = False
        self.button_s = False
        self.button_a = False
        self.button_d = False

        while True:
            self.check_events()
            self.draw_the_screen()
            self.clock.tick(60)

    def draw_the_screen(self):
        self.screen_1.fill((0, 0, 0))

        self.object_1_information = Object_1().spawn_object_1()
        self.movable_object_1 = self.object_1_information[0]
        self.screen_1.blit(self.movable_object_1, (self.pos_x, self.pos_y))

        self.object_2_information = Object_2().spawn_object_2()
        self.movable_object_2 = self.object_2_information[0]
        self.screen_1.blit(self.movable_object_2, (self.pos_x2, self.pos_y2))

        if self.up and self.pos_y > 0:
            self.pos_y -= 5
        if self.down and self.pos_y + self.object_1_information[2] < 480:
            self.pos_y += 5
        if self.left and self.pos_x > 0:
            self.pos_x -= 5
        if self.right and self.pos_x + self.object_1_information[1] < 640 :
            self.pos_x += 5

        if self.button_w and self.pos_y2 > 0:
            self.pos_y2 -= 5
        if self.button_s and self.pos_y2 + self.object_2_information[2] < 480:
            self.pos_y2 += 5
        if self.button_a and self.pos_x2 > 0:
            self.pos_x2 -= 5
        if self.button_d and self.pos_x2 + self.object_2_information[1] < 640 :
            self.pos_x2 += 5

        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    GameLoop()