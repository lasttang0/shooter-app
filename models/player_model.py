from os import path
import pygame
from utils.constants import (IMG_DIR, Colors,
                             SCREEN_WIDTH, SCREEN_HEIGHT,
                             PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, SPEED_CHANGE,
                             COLLIDE_RADIUS, STARSHIP, HEALTH, LIVES, HIDING_TIME)


class PlayerModel(pygame.sprite.Sprite):
    """
    PlayerModel class represents the player's spaceship in the game.

    Attributes:
        image (pygame.Surface): The image of the player's spaceship.
        rect (pygame.Rect): The rectangle that defines the player's position and size.
        health (int): The current health of the player.
        speed_x (int): The horizontal speed of the player's spaceship.
        radius (int): The collision radius of the player's spaceship.
        lives (int): The remaining lives of the player.
        hidden (bool): Indicates whether the player's spaceship is hidden.
        hide_timer (int): The timestamp when the player's spaceship was hidden.
        death_moment (int): The timestamp of the player's death.

    Methods:
        update(): Update the player's position and behavior.
        hide(): Hide the player's spaceship.
    """

    def __init__(self):
        """
        Initialize an instance of PlayerModel.
        """
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
        """
        Update the player's position and behavior.
        """
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
        """
        Hide the player's spaceship and set the hide timer.
        """
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT + 200)
