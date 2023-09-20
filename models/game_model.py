import pygame

from models.player_model import PlayerModel


class GameModel:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.player = PlayerModel()
        self.all_sprites.add(self.player)

