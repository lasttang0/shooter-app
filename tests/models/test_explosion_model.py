from unittest.mock import MagicMock

import pygame
from models.explosion_model import ExplosionModel
from utils.constants import Explosions


class MockSound:
    def __init__(self):
        self.play_called = False

    def play(self):
        self.play_called = True


# Тесты для класса ExplosionModel
def test_explosion_model_creation(game_controller):
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
    center = (100, 100)
    size = Explosions.LARGE
    explosion = ExplosionModel(center, size)

    explosion.kill()

    assert explosion.alive() is False


# Тесты для класса ExplosionModel
def test_explosion_model_play_sound(game_controller, monkeypatch):
    # Мокируем pygame.mixer.Sound и его метод play
    mock_sound = MagicMock()
    mock_play = MagicMock()
    mock_sound.play = mock_play
    monkeypatch.setattr(pygame.mixer, 'Sound', lambda x: mock_sound)

    ExplosionModel.play_sound()

    # Утверждаем, что метод play был вызван
    mock_play.assert_called_once()
