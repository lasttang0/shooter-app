import pytest
import pygame

from controllers.game_controller import GameController
from models.game_model import GameModel
from views.game_view import GameView


@pytest.fixture(scope="module")
def pygame_initialized():
    """
    Pytest fixture for initializing Pygame with video system support before running tests.

    Yields:
        None: The fixture is set up before tests and cleaned up after tests.
    """
    pygame.init()
    screen_width = 800
    screen_height = 600
    pygame.display.set_mode((screen_width, screen_height))
    yield
    pygame.quit()


@pytest.fixture
def game_controller():
    """
    Pytest fixture for creating an instance of GameController.

    Yields:
        GameController: An instance of GameController for testing.
    """
    pygame.init()
    screen_width = 800
    screen_height = 600
    pygame.display.set_mode((screen_width, screen_height))
    model = GameModel()
    view = GameView()
    controller = GameController(model, view)
    yield controller
    pygame.quit()


@pytest.fixture
def game_view(pygame_initialized):
    """
    Pytest fixture for creating an instance of GameView.

    Yields:
        GameView: An instance of GameView for testing.
    """
    view = GameView()
    yield view
    pygame.quit()
