import random
from os import path
import pygame
from utils.constants import (Colors, IMG_DIR,
                             SCREEN_WIDTH, SCREEN_HEIGHT,
                             ASTEROID_LIST, ASTEROID_SIZES,
                             ASTEROID_WIDTH, ASTEROID_HEIGHT, SPAWN_Y_MIN, SPAWN_Y_MAX,
                             ASTEROID_SPEED_X_MIN, ASTEROID_SPEED_X_MAX, ASTEROID_SPEED_Y_MIN, ASTEROID_SPEED_Y_MAX,
                             ROTATION_SPEED_MIN, ROTATION_SPEED_MAX)


class AsteroidModel(pygame.sprite.Sprite):
    """
    AsteroidModel class represents an asteroid in the game.

    Attributes:
        image_orig (pygame.Surface): The original image of the asteroid.
        image (pygame.Surface): The current image of the asteroid.
        rect (pygame.Rect): The rectangular bounds of the asteroid.
        speed_x (int): The horizontal speed of the asteroid.
        speed_y (int): The vertical speed of the asteroid.
        radius (int): The radius of the asteroid.
        rotation (int): The current rotation angle of the asteroid.
        rotation_speed (int): The speed at which the asteroid rotates.
        last_update (int): The time of the last rotation update.

    Methods:
        update(): Update the position and rotation of the asteroid.
        rotate(): Rotate the asteroid.
    """

    def __init__(self):
        """
        Initialize an instance of AsteroidModel.
        """
        pygame.sprite.Sprite.__init__(self)
        some_asteroid = random.choice(ASTEROID_LIST)
        scale = random.choice(ASTEROID_SIZES)
        self.image_orig = pygame.transform.scale(pygame.image.load(path.join(IMG_DIR, 'asteroids',
                                                                             some_asteroid)).convert(),
                                                 (ASTEROID_WIDTH * scale, ASTEROID_HEIGHT * scale))
        self.image_orig.set_colorkey(Colors.BLACK.value)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(SPAWN_Y_MIN, SPAWN_Y_MAX)
        self.speed_x = random.randint(ASTEROID_SPEED_X_MIN, ASTEROID_SPEED_X_MAX)
        self.speed_y = random.randint(ASTEROID_SPEED_Y_MIN, ASTEROID_SPEED_Y_MAX)
        self.radius = int(self.rect.width * 0.75 / 2)
        self.rotation = 0
        self.rotation_speed = random.randint(ROTATION_SPEED_MIN, ROTATION_SPEED_MAX)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        """
        Update the position and rotation of the asteroid.
        """
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(SPAWN_Y_MIN, SPAWN_Y_MAX)
            self.speed_y = random.randint(ASTEROID_SPEED_Y_MIN, ASTEROID_SPEED_Y_MAX)
        self.rotate()

    def rotate(self):
        """
        Rotate the asteroid.
        """
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rotation = (self.rotation + self.rotation_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rotation)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
