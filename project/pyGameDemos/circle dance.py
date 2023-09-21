import pygame
import math

def spinning():
    pygame.init()
    screen_1 = pygame.display.set_mode((640, 480))
    ball = pygame.image.load("imgs/object_2.png")

    #the ball degrees
    degree_of_1st = 0.62727273 #Was this was an important number, for some reason??  #MATHS
    degree_of_2nd = degree_of_1st * 2
    degree_of_3rd = degree_of_1st * 3
    degree_of_4th = degree_of_1st * 4
    degree_of_5th = degree_of_1st * 5
    degree_of_6th = degree_of_1st * 6
    degree_of_7th = degree_of_1st * 7
    degree_of_8th = degree_of_1st * 8
    degree_of_9th = degree_of_1st * 9
    degree_of_10th = degree_of_1st * 10

    clock = pygame.time.Clock()

    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                exit()

        x1, y1 = 360+math.cos(degree_of_1st)*130, 240+math.sin(degree_of_1st)*130
        x2, y2 = 360+math.cos(degree_of_2nd)*130, 240+math.sin(degree_of_2nd)*130
        x3, y3 = 360+math.cos(degree_of_3rd)*130, 240+math.sin(degree_of_3rd)*130
        x4, y4 = 360+math.cos(degree_of_4th)*130, 240+math.sin(degree_of_4th)*130
        x5, y5 = 360+math.cos(degree_of_5th)*130, 240+math.sin(degree_of_5th)*130
        x6, y6 = 360+math.cos(degree_of_6th)*130, 240+math.sin(degree_of_6th)*130
        x7, y7 = 360+math.cos(degree_of_7th)*130, 240+math.sin(degree_of_7th)*130
        x8, y8 = 360+math.cos(degree_of_8th)*130, 240+math.sin(degree_of_8th)*130
        x9, y9 = 360+math.cos(degree_of_9th)*130, 240+math.sin(degree_of_9th)*130
        x10, y10 = 360 + math.cos(degree_of_10th) * 130, 240 + math.sin(degree_of_10th) * 130

        screen_1.fill((0, 0, 0))

        screen_1.blit(ball, (x1, y1))
        screen_1.blit(ball, (x2, y2))
        screen_1.blit(ball, (x3, y3))
        screen_1.blit(ball, (x4, y4))
        screen_1.blit(ball, (x5, y5))
        screen_1.blit(ball, (x6, y6))
        screen_1.blit(ball, (x7, y7))
        screen_1.blit(ball, (x8, y8))
        screen_1.blit(ball, (x9, y9))
        screen_1.blit(ball, (x10, y10))

        pygame.display.flip()
        degree_of_1st += 0.01
        degree_of_2nd += 0.01
        degree_of_3rd += 0.01
        degree_of_4th += 0.01
        degree_of_5th += 0.01
        degree_of_6th += 0.01
        degree_of_7th += 0.01
        degree_of_8th += 0.01
        degree_of_9th += 0.01
        degree_of_10th += 0.01
        clock.tick(60)

if __name__ == '__main__':
    spinning()