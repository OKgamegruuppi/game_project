import pygame

def main():
    pygame.init()
    screen_1 = pygame.display.set_mode((640, 480))
    robo = pygame.image.load("robo.png")

    x = 0
    y = 0
    speed = 1
    down = 0
    clock = pygame.time.Clock()

    while True:
        for event_trigger in pygame.event.get():
            if event_trigger.type == pygame.QUIT:
                exit()
        screen_1.fill((0, 0, 0))
        screen_1.blit(robo, (x, y))
        pygame.display.flip()
        x += speed
        y += down

        if y + robo.get_height() == 86 and x + robo.get_width() >= 640:
            speed = 0
            down = 1
        if y + robo.get_height() >= 480 and x + robo.get_width() > 640:
            speed = -1
            down = 0
        if x + robo.get_width() == 50 and y + robo.get_height() >= 480:
            speed = 0
            down = -1
        if y + robo.get_height() == 86 and x + robo.get_width() <= 640:
            speed = 1
            down = 0
        clock.tick(120)

if __name__ == '__main__':
    main()
