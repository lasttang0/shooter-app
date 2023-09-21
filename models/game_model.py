from os import path

import pygame

from models.player_model import PlayerModel
from models.asteroid_model import AsteroidModel
from models.rocket_model import RocketModel
from utils.constants import COUNT, SND_DIR, PEW


class GameModel:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = None
        self.asteroids = pygame.sprite.Group()
        self.rockets = pygame.sprite.Group()
        self.add_player()
        self.add_asteroids(COUNT)
        self.score = 0

    def add_player(self):
        self.player = PlayerModel()
        self.all_sprites.add(self.player)

    def add_asteroids(self, count):
        for _ in range(count):
            asteroid = AsteroidModel()
            self.all_sprites.add(asteroid)
            self.asteroids.add(asteroid)

    def add_rocket(self, x, y):
        rocket = RocketModel(x, y)
        self.all_sprites.add(rocket)
        self.rockets.add(rocket)
        pygame.mixer.Sound(path.join(SND_DIR, PEW)).play()

