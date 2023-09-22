import random
import pygame
from utils.constants import (Colors,
                             ROCKET_WIDTH, ROCKET_HEIGHT, ROCKET_SPEED, HIT_RADIUS)


class RocketModel(pygame.sprite.Sprite):
    """
    RocketModel class represents a rocket in the game.

    Attributes:
        image (pygame.Surface): The surface representing the rocket's appearance.
        rect (pygame.Rect): The rectangle defining the rocket's position and size.
        speed_y (int): The vertical speed of the rocket.
        radius (int): The hit radius of the rocket.

    Methods:
        update(): Update the rocket's position.
    """

    def __init__(self, x, y):
        """
        Initialize an instance of RocketModel.

        Args:
            x (int): The initial x-coordinate of the rocket.
            y (int): The initial y-coordinate of the rocket.
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((ROCKET_WIDTH, ROCKET_HEIGHT))
        self.image.fill(random.choice([Colors.RED.value, Colors.ORANGE.value, Colors.YELLOW.value]))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_y = ROCKET_SPEED
        self.radius = HIT_RADIUS

    def update(self):
        """
        Update the rocket's position as it moves vertically.
        """
        self.rect.y += self.speed_y
        if self.rect.bottom < 0:
            self.kill()
