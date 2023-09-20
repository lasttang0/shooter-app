import pygame

from utils import constants


class GameView:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
        pygame.display.set_caption("Shooter Game")
        self.clock = pygame.time.Clock()

