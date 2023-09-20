import pygame

class GameLoop:
    def __init__(self):
        pygame.init() #2. pygame moduulin startti

        self.load_images() #3. lataa kuvat self.kuvat listaan
        self.new_games() #4. luo pelikartan self.kartta matrixiin

        #5. kartan korkeus asetetaan
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[0].get_width()
        screen_height = self.scale * self.height
        screen_width = self.scale * self.width
        self.screen_1 = pygame.display.set_mode((screen_width, screen_height))

        #6. peli-ikkunan otsikko: Pyypeli
        pygame.display.set_caption("Box pushing thing")

        #7. silmukka alkaa
        self.looping()

    def load_images(self):
        self.images = []
        for name in ["floor", "wall", "target", "box", "object", "done", "targetobject"]:
            self.images.append(pygame.image.load("box_pushing_imgs/" + name + ".png"))

    def new_games(self): #KARTAN OBJEKTIEN LUONTI
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                    [1, 2, 3, 0, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1],
                    [1, 0, 0, 1, 2, 3, 0, 2, 3, 0, 0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 4, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def looping(self):
        while True:
            #os.system('clear')
            self.check_events() #8. ottaa vastaan pelaajan napin painallukset SIIRTYY FUNKTIOON self.liiku()
            self.find_object()
            self.draw_the_screen()

    def check_events(self):
        for event_trigger in pygame.event.get():
            if event_trigger.type == pygame.KEYDOWN:
                if event_trigger.key == pygame.K_LEFT:
                    self.move(0, -1)
                if event_trigger.key == pygame.K_RIGHT:
                    self.move(0, 1)
                if event_trigger.key == pygame.K_UP:
                    self.move(-1, 0)
                if event_trigger.key == pygame.K_DOWN:
                    self.move(1, 0)
            if event_trigger.type == pygame.QUIT:
                exit()

    def find_object(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [4, 6]:
                    return (y, x)

    def move(self, move_y, move_x):
        objects_old_y, objects_old_x = self.find_object()     #9. HAKEE ROBON SIJAINNIN FUNKTIOLLA etsi_robo()
        objects_new_y = objects_old_y + move_y      #LISÄÄ SIIHEN PELAAJAN PAINALLUKSEN
        objects_new_x = objects_old_x + move_x
        #10. TUTKII ONKO ROBOTIN UUSI LIIKE MAHDOLLINEN
        if self.map[objects_new_y][objects_new_x] == 1:    #SEINÄ = EI MAHDOLLINEN
            return
        if self.map[objects_new_y][objects_new_x] in [3, 5]:   #LAATIKKO TAI VALMIS LAATIKKO SEURAAVASSA RUUDUSSA
            boxs_new_y = objects_new_y + move_y
            boxs_new_x = objects_new_x + move_x
            if self.map[boxs_new_y][boxs_new_x] in [1, 3, 5]: #JOS LAATIKON SEURAAVASSA RUUDUSSA ON SEINÄ TAI LAATIKKO TAI VALMIS LAATIKKO = EI MAHDOLLINEN
                return
            self.map[objects_new_y][objects_new_x] -= 3
            self.map[boxs_new_y][boxs_new_x] += 3
        self.map[objects_old_y][objects_old_x] -= 4
        self.map[objects_new_y][objects_new_x] += 4
        for x in self.map:
            print(x)
        print("\n")

    def games_text(self):
        self.completed_boxes = 0
        self.total_amount = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [5]:
                    self.completed_boxes += 1
                if self.map[y][x] in [3, 5]:
                    self.total_amount += 1
        self.font_style = pygame.font.SysFont("Arial", 30)
        self.games_status_text = self.font_style.render(f"Laatikkoja paikallaan:[{self.completed_boxes}]", True, (255, 100, 0))
        return self.games_status_text

    def draw_the_screen(self):
        self.screen_1.fill((0, 0, 0))
        self.games_text()
        for y in range(self.height):
            for x in range(self.width):
                ruutu = self.map[y][x]
                self.screen_1.blit(self.images[ruutu], (x * self.scale, y * self.scale))
                self.screen_1.blit(self.games_status_text, (0, 10))
                if self.completed_boxes == self.total_amount:
                    print("YOU WIN")
                    GameLoop()
        pygame.display.flip()

if __name__ == "__main__":
    GameLoop() #1. aloittaa pelin