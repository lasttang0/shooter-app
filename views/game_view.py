import pygame

from utils.constants import WIDTH, HEIGHT


class GameView:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Shooter Game")
        self.clock = pygame.time.Clock()
