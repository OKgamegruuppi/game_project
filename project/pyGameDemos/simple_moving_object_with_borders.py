import pygame

class ObjectToMove:
    def __init__(self):
        self.movable_object = pygame.image.load("object_1.png")
    def spawn_object(self):
        return [self.movable_object, self.movable_object.get_width(), self.movable_object.get_height()]

class GameLoop():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_1 = pygame.display.set_mode((640, 480))

        self.looping()

    def check_events(self):
        for event_trigger in pygame.event.get():
            if event_trigger.type == pygame.KEYDOWN:
                if event_trigger.key == pygame.K_UP:
                    self.up = True
                if event_trigger.key == pygame.K_DOWN:
                    self.down = True
                if event_trigger.key == pygame.K_LEFT:
                    self.left = True
                if event_trigger.key == pygame.K_RIGHT:
                    self.right = True
                if event_trigger.key == pygame.K_RETURN:
                    self.has_begun = True

            if event_trigger.type == pygame.KEYUP:
                if event_trigger.key == pygame.K_UP:
                    self.up = False
                if event_trigger.key == pygame.K_DOWN:
                    self.down = False
                if event_trigger.key == pygame.K_LEFT:
                    self.left = False
                if event_trigger.key == pygame.K_RIGHT:
                    self.right = False
            if event_trigger.type == pygame.QUIT:
                exit()
    def looping(self):
        self.pos_x = 30
        self.pos_y = 30
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        while True:
            self.check_events()
            self.draw_the_screen()
            self.clock.tick(60)

    def draw_the_screen(self):
        self.screen_1.fill((0, 0, 0))
        self.movable_object_information = ObjectToMove().spawn_object()
        self.the_object_moved = self.movable_object_information[0]
        self.screen_1.blit(self.the_object_moved, (self.pos_x, self.pos_y))
        if self.up and self.pos_y > 0:
            self.pos_y -= 5
        if self.down and self.pos_y + self.movable_object_information[2] < 480:
            self.pos_y += 5
        if self.left and self.pos_x > 0:
            self.pos_x -= 5
        if self.right and self.pos_x + self.movable_object_information[1] < 640 :
            self.pos_x += 5

        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    GameLoop()
