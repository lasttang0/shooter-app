import pygame
from utils.constants import GameStates


def test_game_controller_initialization(game_controller):
    """
    Test the initialization of the GameController.

    Checks that the GameController instance is correctly initialized with a model,
    view, game state, and game over status.
    """
    assert game_controller.model is not None
    assert game_controller.view is not None
    assert game_controller.game_state == GameStates.RUNNING
    assert game_controller.game_over is True


def test_handle_events(game_controller):
    """
    Test the handle_events method of the GameController.

    Checks that the handle_events method correctly handles pygame events and updates
    the game state and model accordingly.
    """
    pygame.event.post(pygame.event.Event(pygame.QUIT))
    game_controller.handle_events()
    assert game_controller.game_state == GameStates.EXIT

    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE))
    game_controller.handle_events()
    assert len(game_controller.model.rockets) == 1
