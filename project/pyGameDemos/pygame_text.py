import pygame

def main():
    pygame.init()
    screen_1 = pygame.display.set_mode((640, 480))
    screen_1.fill((0, 0, 0))

    style_of_font = pygame.font.SysFont("Arial", 24)
    displayed_text = style_of_font.render("HELLO WORLD!", True, (255, 0, 0))
    screen_1.blit(displayed_text, (100, 50))
    pygame.display.flip()

    while True:
        for event_trigger in pygame.event.get():
            if event_trigger.type == pygame.QUIT:
                exit()

if __name__ == '__main__':
    main()