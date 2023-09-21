import pygame
import math

def main():
    pygame.init()
    screen_1 = pygame.display.set_mode((640, 480))

    object = pygame.image.load("object_1.png")

    degree = 0
    clock = pygame.time.Clock()

    while True:
        for event_trigger in pygame.event.get():
            if event_trigger.type == pygame.QUIT:
                exit()

        x = 320+math.cos(degree)*100-object.get_width()/2
        y = 240+math.sin(degree)*100-object.get_height()/2

        screen_1.fill((0, 0, 0))
        screen_1.blit(object, (x, y))
        pygame.display.flip()

        degree += 0.01
        clock.tick(60)

if __name__ == '__main__':
    main()
