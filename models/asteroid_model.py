import random
from os import path

import pygame

from utils.constants import (Colors, IMG_DIR,
                             SCREEN_WIDTH, SCREEN_HEIGHT,
                             ASTEROID_WIDTH, ASTEROID_HEIGHT, SPAWN_Y_MIN, SPAWN_Y_MAX,
                             ASTEROID_SPEED_X_MIN, ASTEROID_SPEED_X_MAX, ASTEROID_SPEED_Y_MIN, ASTEROID_SPEED_Y_MAX,
                             ROTATION_SPEED_MIN, ROTATION_SPEED_MAX)


class AsteroidModel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        some_asteroid = random.choice(["asteroid1.png", "asteroid2.png", "asteroid3.png", "asteroid4.png", ])
        scale = random.choice([0.75, 1, 1.1, 1.2, 1.75])
        self.image_orig = pygame.transform.scale(pygame.image.load(path.join(IMG_DIR, some_asteroid)).convert(),
                                                 (ASTEROID_WIDTH * scale, ASTEROID_HEIGHT * scale))
        self.image_orig.set_colorkey(Colors.BLACK.value)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(SPAWN_Y_MIN, SPAWN_Y_MAX)
        self.speed_x = random.randrange(ASTEROID_SPEED_X_MIN, ASTEROID_SPEED_X_MAX)
        self.speed_y = random.randrange(ASTEROID_SPEED_Y_MIN, ASTEROID_SPEED_Y_MAX)
        self.radius = int(self.rect.width * 0.75 / 2)
        self.rotation = 0
        self.rotation_speed = random.randrange(ROTATION_SPEED_MIN, ROTATION_SPEED_MAX)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(SPAWN_Y_MIN, SPAWN_Y_MAX)
            self.speed_y = random.randrange(ASTEROID_SPEED_Y_MIN, ASTEROID_SPEED_Y_MAX)
        self.rotate()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rotation = (self.rotation + self.rotation_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rotation)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
