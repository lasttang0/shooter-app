import pygame
from models.asteroid_model import AsteroidModel


def test_asteroid_model_creation(game_controller):
    """
    Test the creation of an AsteroidModel object.

    Checks that an AsteroidModel object is created correctly with the expected attributes.
    """
    asteroid = AsteroidModel()

    assert isinstance(asteroid, AsteroidModel)
    assert isinstance(asteroid.image, pygame.Surface)
    assert isinstance(asteroid.rect, pygame.Rect)
    assert isinstance(asteroid.speed_x, int)
    assert isinstance(asteroid.speed_y, int)
    assert isinstance(asteroid.radius, int)
    assert isinstance(asteroid.rotation, int)


def test_asteroid_model_update(game_controller):
    """
    Test the update method of the AsteroidModel.

    Checks that the update method modifies the coordinates of the asteroid object
    if expected.
    """
    asteroid = AsteroidModel()

    initial_x = asteroid.rect.x
    initial_y = asteroid.rect.y

    asteroid.update()

    assert asteroid.rect.x != initial_x or asteroid.rect.y != initial_y
