import pygame

from models.rocket_model import RocketModel
from utils.constants import (Colors,
                             SCREEN_WIDTH, SCREEN_HEIGHT,
                             PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, SPEED_CHANGE)


class PlayerModel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10)
        self.speed_x = PLAYER_SPEED
        self.image.fill(Colors.GREEN.value)

    def update(self):
        self.speed_x = PLAYER_SPEED
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.speed_x = -SPEED_CHANGE
        if key_pressed[pygame.K_RIGHT]:
            self.speed_x = SPEED_CHANGE
        self.rect.x += self.speed_x
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

