import pygame

def main():
    pygame.init()
    screen_1 = pygame.display.set_mode((640, 480))

    moving_object = pygame.image.load("object_2.png")
    x = 0
    y = 0

    speed = 1
    clock = pygame.time.Clock()

    while True:
        for event_trigger in pygame.event.get():
            if event_trigger.type == pygame.QUIT:
                exit()

        screen_1.fill((0, 0, 0))
        screen_1.blit(moving_object, (x, y))
        pygame.display.flip()

        y += speed
        if speed > 0 and y + moving_object.get_height() >= 480:
            speed = -speed
        if speed < 0 and y <= 0:
            speed = -speed

        clock.tick(60)

if __name__ == '__main__':
    main()
