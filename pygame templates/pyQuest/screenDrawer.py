import pygame
import main_game_loop

# screenDrawer.py:n funktio draw_screen
# päivittää main_game_loopin näytön

def draw_screen(self):
    self.display.fill((250, 250, 250))

    bg = pygame.image.load("bg.png")
    self.display.blit(bg, (0, 0))

    self.font_setting = pygame.font.SysFont("Arial", 15)
    self.player_inventory = self.font_setting.render(f"INVENTORY:", True, (255, 100, 0))
    self.player_char_berry_counter = self.font_setting.render(f"Berries: {str(self.player_char_collision_points)}", True, (255, 100, 0))

    self.player_qb = self.font_setting.render(f"CURRENT QUEST:", True, (255, 100, 0))

    if self.player_char_collision_points > 9:
        self.player_current_quest = self.font_setting.render("QUEST COMPLETED", True, (255, 100, 0))
    else:
        self.player_current_quest = self.font_setting.render(main_game_loop.quest_status, True, (255, 100, 0))

    self.display.blit(self.player_char_berry_counter, (1000, 30))
    self.display.blit(self.player_inventory, (1000, 0))
    self.display.blit(self.player_qb, (1000, 100))
    self.display.blit(self.player_current_quest, (1000, 120))


    self.player_chars_information = main_game_loop.PlayerCharacter().spawn_player_char()
    self.player_char_block = self.player_chars_information[0]
    self.display.blit(self.player_char_block, (self.player_char_pos_x, self.player_char_pos_y))
    self.player_char_rect = pygame.Rect(self.player_char_pos_x, self.player_char_pos_y,
                                        self.player_char_block.get_width() / 2, self.player_char_block.get_height() / 2)
    self.obj3_image = pygame.image.load("item1.png")

    num = 0
    for new_ones in range(len(self.available_item1s)):
        self.display.blit(self.obj3_image, (self.available_item1s[num][1]))
        num += 1

    if self.up and self.player_char_pos_y > 0:
        self.player_char_pos_y -= 1
    if self.down and self.player_char_pos_y + self.player_chars_information[2] < main_game_loop.screen_hei:
        self.player_char_pos_y += 1
    if self.left and self.player_char_pos_x > 0:
        self.player_char_pos_x -= 1
    if self.right and self.player_char_pos_x + self.player_chars_information[1] < main_game_loop.screen_wid:
        self.player_char_pos_x += 1

    lookup_player_char_hits = -1
    for lookup in self.item1_hit_index:
        lookup_player_char_hits += 1

        if self.player_char_rect.colliderect(lookup):
            self.item1_hit_index.pop(lookup_player_char_hits)
            self.available_item1s.pop(lookup_player_char_hits)
            self.player_char_collision_points += 1
    pygame.display.flip()
    self.clock.tick(60)
