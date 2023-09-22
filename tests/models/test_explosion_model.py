import pygame
from models.explosion_model import ExplosionModel
from utils.constants import Explosions


class MockSound:
    """
    A mock class for pygame.mixer.Sound to simulate sound playback.

    This class is used in unit testing to replace the actual pygame.mixer.Sound class.
    It provides a mock implementation of the play method to track whether the play
    method has been called.

    Attributes:
        play_called (bool): A flag indicating whether the play method has been called.
    """

    def __init__(self):
        """
        Initialize a new instance of MockSound.

        Initializes the MockSound instance and sets the play_called flag to False.
        """
        self.play_called = False

    def play(self):
        """
        Simulate the play method of pygame.mixer.Sound.

        This method sets the play_called flag to True when called, simulating the behavior
        of the play method in pygame.mixer.Sound.
        """
        self.play_called = True


def test_explosion_model_creation(game_controller):
    """
    Test the creation of an ExplosionModel instance.

    Args:
        game_controller: A fixture to initialize the game controller.

    The test checks if an ExplosionModel instance is created correctly with the provided center
    coordinates and size. It verifies the type of its attributes, including animation, image, rect,
    frame, and frame_rate.

    Returns:
        None
    """
    center = (100, 100)
    size = Explosions.LARGE
    explosion = ExplosionModel(center, size)

    assert isinstance(explosion, ExplosionModel)
    assert explosion.size == size
    assert isinstance(explosion.animation, dict)
    assert isinstance(explosion.image, pygame.Surface)
    assert isinstance(explosion.rect, pygame.Rect)
    assert explosion.rect.center == center
    assert explosion.frame == 0
    assert explosion.frame_rate == 50


def test_explosion_model_kill(game_controller):
    """
    Test the kill method of ExplosionModel.

    Args:
        game_controller: A fixture to initialize the game controller.

    The test checks if the kill method correctly sets the sprite's alive status to False.

    Returns:
        None
    """
    center = (100, 100)
    size = Explosions.LARGE
    explosion = ExplosionModel(center, size)

    explosion.kill()

    assert explosion.alive() is False



