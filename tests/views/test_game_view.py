import pygame
import pytest
from unittest.mock import Mock

from utils.constants import MUSIC_VOLUME
from views.game_view import GameView


@pytest.fixture
def game_view():
    return GameView()


def test_play_music(game_view, mocker):
    pygame_mixer_init_mock = mocker.patch('pygame.mixer.init')
    pygame_mixer_music_load_mock = mocker.patch('pygame.mixer.music.load')
    pygame_mixer_music_set_volume_mock = mocker.patch('pygame.mixer.music.set_volume')
    pygame_mixer_music_play_mock = mocker.patch('pygame.mixer.music.play')

    game_view.play_music()

    pygame_mixer_init_mock.assert_called_once()
    pygame_mixer_music_load_mock.assert_called_once()
    pygame_mixer_music_set_volume_mock.assert_called_once_with(MUSIC_VOLUME)
    pygame_mixer_music_play_mock.assert_called_once_with(loops=-1)


def test_draw_text(game_view):
    mock_screen = Mock()
    text = "Test Text"
    size = 20
    x, y = 100, 100

    game_view.FONT = "Arial"
    game_view.draw_text(mock_screen, text, size, x, y)

    mock_screen.blit.assert_called_once()


def test_draw_health_bar(game_view):
    x, y = 100, 100
    pct = 75

    game_view.draw_health_bar(game_view.screen, x, y, pct)


def test_quit_game(game_view, mocker):
    pygame_quit_mock = mocker.patch('pygame.quit')
    sys_exit_mock = mocker.patch('sys.exit')

    game_view.quit_game()

    pygame_quit_mock.assert_called_once()
    sys_exit_mock.assert_called_once()
