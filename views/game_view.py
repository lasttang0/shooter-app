import sys
from os import path

import pygame

from utils.constants import (IMG_DIR, SKY, SCREEN_WIDTH, SCREEN_HEIGHT, FONT, FONT_SIZE,
                             Colors, SND_DIR, SPACE_MUSIC, BAR_HEIGHT, MUSIC_VOLUME, STARSHIP, PLAYER_WIDTH,
                             PLAYER_HEIGHT, FPS)


class GameView:
    def __init__(self):
        pygame.init()
        self.play_music()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Space Shooter Game")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load(path.join(IMG_DIR, SKY)).convert()

    def open_screen(self):
        self.screen.blit(self.background, self.background.get_rect())
        self.draw_text(self.screen, "Shooter app!", 64, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text(self.screen, "Left / right to move, Space to fire", 22,
                       SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text(self.screen, "Press a key to begin", 18, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        pygame.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.KEYUP:
                    waiting = False

    @staticmethod
    def play_music():
        pygame.mixer.init()
        pygame.mixer.music.load(path.join(SND_DIR, SPACE_MUSIC))
        pygame.mixer.music.set_volume(MUSIC_VOLUME)
        pygame.mixer.music.play(loops=-1)

    def render_game(self, model):
        self.screen.fill(Colors.BLACK.value)
        self.screen.blit(self.background, self.background.get_rect())
        model.all_sprites.draw(self.screen)
        self.draw_text(self.screen, f'Score: {str(model.score)}', FONT_SIZE, SCREEN_WIDTH * 6/7, 10)
        self.draw_health_bar(self.screen, 5, 10, model.player.health)
        life_pic = pygame.transform.scale(pygame.image.load(path.join(IMG_DIR, STARSHIP)).convert(),
                                            (PLAYER_WIDTH / 3, PLAYER_HEIGHT / 3))
        self.draw_lives(self.screen, 5, 30, model.player.lives, life_pic)
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

    @staticmethod
    def draw_lives(screen, x, y, lives, image):
        for i in range(lives):
            image_rect = image.get_rect()
            image_rect.x = x + 40 * i
            image_rect.y = y
            screen.blit(image, image_rect)

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()
