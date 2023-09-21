from os import path

import pygame

from utils.constants import (IMG_DIR, SKY, SCREEN_WIDTH, SCREEN_HEIGHT, FONT, FONT_SIZE,
                             Colors, SND_DIR, SPACE_MUSIC, BAR_HEIGHT)


class GameView:
    def __init__(self):
        pygame.init()
        self.play_music()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Shooter Game")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(path.join(IMG_DIR, SKY)).convert()

    @staticmethod
    def play_music():
        pygame.mixer.init()
        pygame.mixer.music.load(path.join(SND_DIR, SPACE_MUSIC))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1)

    def render_game(self, model):
        self.screen.fill(Colors.BLACK.value)
        self.screen.blit(self.background, self.background.get_rect())
        model.all_sprites.draw(self.screen)
        self.draw_text(self.screen, f'Score: {str(model.score)}', FONT_SIZE, SCREEN_WIDTH * 6/7, 10)
        self.draw_health_bar(self.screen, 5, 10, model.player.health)
        pygame.display.flip()

    @staticmethod
    def draw_text(screen, text, size, x, y):
        font_name = pygame.font.match_font(FONT)
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, Colors.WHITE.value)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

    @staticmethod
    def draw_health_bar(screen, x, y, pct):
        if pct < 0:
            pct = 0
        bar_length = SCREEN_WIDTH / 5
        fill = (pct / 100) * bar_length
        outline_rect = pygame.Rect(x, y, bar_length, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(screen, Colors.GREEN.value, fill_rect)
        pygame.draw.rect(screen, Colors.WHITE.value, outline_rect, 2)
