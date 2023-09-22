import pygame
from models.player_model import PlayerModel


def test_game_model_initialization(game_controller):
    """
    Test the initialization of GameModel.

    Args:
        game_controller: A fixture to initialize the game controller.

    The test checks if the GameModel instance is initialized correctly with the expected attributes,
    including all_sprites, player, asteroids, rockets, and score.

    Returns:
        None
    """
    game_model = game_controller.model

    assert isinstance(game_model.all_sprites, pygame.sprite.Group)
    assert isinstance(game_model.player, PlayerModel)
    assert isinstance(game_model.asteroids, pygame.sprite.Group)
    assert isinstance(game_model.rockets, pygame.sprite.Group)
    assert game_model.score == 0


def test_game_model_add_player(game_controller):
    """
    Test the addition of a player to GameModel.

    Args:
        game_controller: A fixture to initialize the game controller.

    The test checks if adding a player to GameModel results in an increase in the number of sprites
    in all_sprites and if the added player is an instance of PlayerModel.

    Returns:
        None
    """
    game_model = game_controller.model
    initial_player_count = len(game_model.all_sprites.sprites())

    game_model.add_player()

    assert len(game_model.all_sprites.sprites()) == initial_player_count + 1
    assert isinstance(game_model.player, PlayerModel)
