from os import path

import pygame

from utils.constants import (IMG_DIR, Colors,
                             SCREEN_WIDTH, SCREEN_HEIGHT,
                             PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, SPEED_CHANGE,
                             COLLIDE_RADIUS, STARSHIP, HEALTH, LIVES, HIDING_TIME, )


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
        self.lives = LIVES
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.death_moment = None

    def update(self):
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > HIDING_TIME:
            self.hidden = False
            self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - PLAYER_HEIGHT / 2)
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

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT + 200)
