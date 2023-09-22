import pygame
from models.player_model import PlayerModel


# Тест для проверки инициализации GameModel
def test_game_model_initialization(game_controller):
    game_model = game_controller.model

    # Проверяем, что игровые объекты были инициализированы
    assert isinstance(game_model.all_sprites, pygame.sprite.Group)
    assert isinstance(game_model.player, PlayerModel)
    assert isinstance(game_model.asteroids, pygame.sprite.Group)
    assert isinstance(game_model.rockets, pygame.sprite.Group)
    assert game_model.score == 0


# Тест для проверки добавления игрока
def test_game_model_add_player(game_controller):
    game_model = game_controller.model
    initial_player_count = len(game_model.all_sprites.sprites())

    # Добавляем игрока
    game_model.add_player()

    # Проверяем, что игрок был успешно добавлен
    assert len(game_model.all_sprites.sprites()) == initial_player_count + 1
    assert isinstance(game_model.player, PlayerModel)


