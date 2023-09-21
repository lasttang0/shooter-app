from os import path

import pygame

from utils.constants import IMG_DIR, SCREEN_WIDTH, SCREEN_HEIGHT, Colors


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
        pygame.display.flip()
