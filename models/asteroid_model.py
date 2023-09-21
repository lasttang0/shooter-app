import random

import pygame

from utils.constants import (Colors,
                             SCREEN_WIDTH, SCREEN_HEIGHT,
                             ASTEROID_WIDTH, ASTEROID_HEIGHT, SPAWN_Y_MIN, SPAWN_Y_MAX,
                             ASTEROID_SPEED_X_MIN, ASTEROID_SPEED_X_MAX, ASTEROID_SPEED_Y_MIN, ASTEROID_SPEED_Y_MAX,
                             )


class AsteroidModel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((ASTEROID_WIDTH, ASTEROID_HEIGHT))
        self.image.fill(Colors.RED.value)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SPAWN_Y_MIN, SPAWN_Y_MAX)
        self.speed_x = random.randrange(ASTEROID_SPEED_X_MIN, ASTEROID_SPEED_X_MAX)
        self.speed_y = random.randrange(ASTEROID_SPEED_Y_MIN, ASTEROID_SPEED_Y_MAX)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(SPAWN_Y_MIN, SPAWN_Y_MAX)
            self.speed_y = random.randrange(ASTEROID_SPEED_Y_MIN, ASTEROID_SPEED_Y_MAX)
