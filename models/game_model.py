import pygame

from models.player_model import PlayerModel
from models.asteroid_model import AsteroidModel
from models.rocket_model import RocketModel
from utils.constants import COUNT


class GameModel:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = PlayerModel()
        self.asteroids = pygame.sprite.Group()
        self.rockets = pygame.sprite.Group()
        self.add_player()
        self.add_asteroids()

    def add_player(self):
        self.all_sprites.add(self.player)

    def add_asteroids(self):
        for _ in range(COUNT):
            asteroid = AsteroidModel()
            self.all_sprites.add(asteroid)
            self.asteroids.add(asteroid)

    def add_rocket(self, x, y):
        rocket = RocketModel(x, y)
        self.all_sprites.add(rocket)
        self.rockets.add(rocket)

