from os import path
import pygame
from models.player_model import PlayerModel
from models.asteroid_model import AsteroidModel
from models.rocket_model import RocketModel
from models.explosion_model import ExplosionModel
from utils.constants import COUNT, SND_DIR, PEW


class GameModel:
    """
    GameModel class represents the game model responsible for managing game entities and logic.

    Attributes:
        all_sprites (pygame.sprite.Group): A group containing all game sprites.
        player (PlayerModel): The player's spaceship.
        asteroids (pygame.sprite.Group): A group containing all asteroids in the game.
        rockets (pygame.sprite.Group): A group containing all rockets fired by the player.
        score (int): The player's current score.

    Methods:
        add_player(): Add the player's spaceship to the game.
        add_asteroids(count): Add a specified number of asteroids to the game.
        add_rocket(x, y): Add a rocket fired by the player to the game.
        add_explosion(center, size): Add an explosion effect to the game.
    """

    def __init__(self):
        """
        Initialize an instance of GameModel.
        """
        self.all_sprites = pygame.sprite.Group()
        self.player = None
        self.asteroids = pygame.sprite.Group()
        self.rockets = pygame.sprite.Group()
        self.add_player()
        self.add_asteroids(COUNT)
        self.score = 0

    def add_player(self):
        """
        Add the player's spaceship to the game.
        """
        self.player = PlayerModel()
        self.all_sprites.add(self.player)

    def add_asteroids(self, count):
        """
        Add a specified number of asteroids to the game.

        Args:
            count (int): The number of asteroids to add.
        """
        for _ in range(count):
            asteroid = AsteroidModel()
            self.all_sprites.add(asteroid)
            self.asteroids.add(asteroid)

    def add_rocket(self, x, y):
        """
        Add a rocket fired by the player to the game.

        Args:
            x (int): The x-coordinate of the rocket's starting position.
            y (int): The y-coordinate of the rocket's starting position.
        """
        rocket = RocketModel(x, y)
        self.all_sprites.add(rocket)
        self.rockets.add(rocket)
        pygame.mixer.Sound(path.join(SND_DIR, PEW)).play()

    def add_explosion(self, center, size):
        """
        Add an explosion effect to the game.

        Args:
            center (tuple): The center coordinates of the explosion.
            size (int): The size of the explosion (LARGE, SMALL, DEATH).
        """
        explosion = ExplosionModel(center, size)
        self.all_sprites.add(explosion)
