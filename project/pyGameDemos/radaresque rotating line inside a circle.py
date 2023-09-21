import pygame
import math

def main():
    pygame.init()
    screen_1 = pygame.display.set_mode((640, 480))
    screen_1.fill((0, 0, 0))

    x_coordinate = 320
    y_coordinate = 240

    length_of_line = 155
    the_radius_of_the_circle = (2 * math.pi) * length_of_line
    the_angle = the_radius_of_the_circle - the_radius_of_the_circle

    while True:
        the_angle += 0.001
        for event_trigger in pygame.event.get():
            if event_trigger.type == pygame.QUIT:
                exit()
        x = x_coordinate + math.cos(the_angle) * length_of_line
        y = y_coordinate + math.sin(the_angle) * length_of_line

        pygame.draw.circle(screen_1, (255, 0, 0), (x_coordinate, y_coordinate), 160)
        pygame.draw.circle(screen_1, (0, 0, 0), (x_coordinate, y_coordinate), 155)
        pygame.draw.circle(screen_1, (255, 0, 0), (x_coordinate, y_coordinate), 5)
        pygame.draw.line(screen_1, (0, 0, 255), (x, y), (x_coordinate, 240), 1)

        print(the_angle)

        pygame.display.flip()

if __name__ == '__main__':
    main()