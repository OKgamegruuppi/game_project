import pygame

def main():
    pygame.init()
    screen_1 = pygame.display.set_mode((640, 480))
    object_1 = pygame.image.load("imgs/object_1.png")

    object_1_x = 0
    object_1_y = 30
    object_1_speed = 1

    object_2_x = 0
    object_2_y = 130
    object_2_speed = 1
    clock = pygame.time.Clock()

    while True:
        for event_trigger in pygame.event.get():
            if event_trigger.type == pygame.QUIT:
                exit()

        screen_1.fill((0, 0, 0))
        screen_1.blit(object_1, (object_1_x, object_1_y))
        screen_1.blit(object_1, (object_2_x, object_2_y))
        pygame.display.flip()

        object_1_x += object_1_speed
        if object_1_speed > 0 and object_1_x + object_1.get_width() >= 640:
            object_1_speed = -object_1_speed
        if object_1_speed < 0 and object_1_x <= 0:
            object_1_speed = -object_1_speed

        object_2_x += (object_2_speed*2)
        if object_2_speed > 0 and object_2_x + object_1.get_width() >= 640:
            object_2_speed = -object_2_speed
        if object_2_speed < 0 and object_2_x <= 0:
            object_2_speed = -object_2_speed

        clock.tick(60)

if __name__ == '__main__':
    main()