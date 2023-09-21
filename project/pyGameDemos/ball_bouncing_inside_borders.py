import pygame

#Mainloop
def main():
    pygame.init()   #Initialize pygame
    screen_1 = pygame.display.set_mode((1040, 480)) #Set window size
    ball = pygame.image.load("ball.png") #Load the image of the ball

    x = 0 # X & Y
    y = 0 # Coordinates

    speed = 1
    down = 0

    clock = pygame.time.Clock()
    while True:
        for event_trigger in pygame.event.get():
            if event_trigger.type == pygame.QUIT:
                exit()
        screen_1.fill((0, 0, 0))
        screen_1.blit(ball, (x, y)) #.blit() make the objects appear on screen
        pygame.display.flip()

        left_border = x+ball.get_width()
        right_border = x
        bottom_border = y + ball.get_height()
        top_border = y

        x += speed
        y += down

        if left_border >= 1040:
            speed = -1
        if right_border == 0:
            speed = 1
        if bottom_border >= 480:
            down = -1
        if top_border == 0:
            down = 1

        clock.tick(1000) #increase this to make the ball bounce faster

if __name__ == '__main__':
    main()
