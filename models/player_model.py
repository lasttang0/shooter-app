from os import path

import pygame

from utils.constants import (IMG_DIR, Colors,
                             SCREEN_WIDTH, SCREEN_HEIGHT,
                             PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, SPEED_CHANGE,
                             COLLIDE_RADIUS, STARSHIP, HEALTH, )


class PlayerModel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path.join(IMG_DIR, STARSHIP)).convert(),
                                            (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.set_colorkey(Colors.BLACK.value)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - PLAYER_HEIGHT / 2)
        self.health = HEALTH
        self.speed_x = PLAYER_SPEED
        self.radius = COLLIDE_RADIUS
        self.death_moment = None


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
