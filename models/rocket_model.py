import random

import pygame

from utils.constants import (Colors,
                             ROCKET_WIDTH, ROCKET_HEIGHT, ROCKET_SPEED, HIT_RADIUS)


class RocketModel(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((ROCKET_WIDTH, ROCKET_HEIGHT))
        # self.image.fill(Colors.YELLOW.value)
        self.image.fill(random.choice([Colors.RED.value, Colors.ORANGE.value, Colors.YELLOW.value]))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_y = ROCKET_SPEED
        self.radius = HIT_RADIUS

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()
