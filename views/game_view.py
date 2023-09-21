from os import path

import pygame

from utils.constants import IMG_DIR, SCREEN_WIDTH, SCREEN_HEIGHT, FONT, FONT_SIZE, Colors


class GameView:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Shooter Game")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(path.join(IMG_DIR, "sky.png")).convert()

    def render_game(self, model):
        self.screen.fill(Colors.BLACK.value)
        self.screen.blit(self.background, self.background.get_rect())
        model.all_sprites.draw(self.screen)
        self.draw_text(self.screen, f'Score: {str(model.score)}', FONT_SIZE, SCREEN_WIDTH * 6/7, 10)
        pygame.display.flip()

    @staticmethod
    def draw_text(screen, text, size, x, y):
        font_name = pygame.font.match_font(FONT)
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, Colors.WHITE.value)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)
