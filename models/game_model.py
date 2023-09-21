import pygame

from models.player_model import PlayerModel
from models.asteroid_model import AsteroidModel
from utils.constants import COUNT


class GameModel:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = PlayerModel()
        self.asteroids = pygame.sprite.Group()
        for _ in range(COUNT):
            asteroid = AsteroidModel()
            self.all_sprites.add(asteroid)
            self.asteroids.add(asteroid)
        self.all_sprites.add(self.player)

