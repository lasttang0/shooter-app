import pytest
import pygame

from controllers.game_controller import GameController
from models.game_model import GameModel
from views.game_view import GameView


# Фикстура для инициализации Pygame с поддержкой видео-системы перед тестами
@pytest.fixture(scope="module")
def pygame_initialized():
    pygame.init()
    screen_width = 800
    screen_height = 600
    pygame.display.set_mode((screen_width, screen_height))
    yield
    pygame.quit()


# Фикстура для создания экземпляра GameController
@pytest.fixture
def game_controller():
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
    view = GameView()
    yield view
    pygame.quit()
