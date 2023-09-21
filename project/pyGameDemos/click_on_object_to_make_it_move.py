import random
import pygame

def main():
    pygame.init()
    screen_1 = pygame.display.set_mode((640, 480))
    moving_object = pygame.image.load("imgs/object_1.png")
    x = 100
    y = 100

    while True:
        rect1 = pygame.Rect(x, y, moving_object.get_width(), moving_object.get_height())
        clock = pygame.time.Clock()

        for event_trigger in pygame.event.get():
            if event_trigger.type == pygame.MOUSEBUTTONDOWN:
                rect_click = pygame.Rect(event_trigger.pos[0],event_trigger.pos[1],1,1)
                if rect_click.colliderect(rect1):
                    x = random.randint(0,600)
                    y = random.randint(0,400)
            if event_trigger.type == pygame.QUIT:
                exit()

        screen_1.fill((0, 0, 0))
        screen_1.blit(moving_object, (x, y))
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()

