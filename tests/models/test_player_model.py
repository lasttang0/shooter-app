import pygame
from models.player_model import PlayerModel
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, HEALTH, PLAYER_SPEED, COLLIDE_RADIUS, LIVES, HIDING_TIME


def test_player_initial_state(pygame_initialized):
    """
    Test the initial state of the player.
    """
    player = PlayerModel()

    assert player.health == HEALTH
    assert player.speed_x == PLAYER_SPEED
    assert player.radius == COLLIDE_RADIUS
    assert player.lives == LIVES
    assert not player.hidden
    assert player.death_moment is None


def test_player_boundary(pygame_initialized):
    """
    Test that the player stays within the screen boundaries.
    """
    player = PlayerModel()
    player.rect.centerx = 0

    player.update()

    assert player.rect.left == 0

    player.rect.centerx = SCREEN_WIDTH

    player.update()

    assert player.rect.right == SCREEN_WIDTH


def test_player_hide(pygame_initialized):
    """
    Test hiding the player.
    """
    player = PlayerModel()
    player.hide()

    assert player.hidden
    assert player.rect.center == (SCREEN_WIDTH / 2, SCREEN_HEIGHT + 200)


def test_player_hide_timer(pygame_initialized):
    """
    Test hiding the player with a timer check.
    """
    player = PlayerModel()
    player.hide()
    player.hide_timer = pygame.time.get_ticks() - HIDING_TIME - 1

    player.update()

    assert not player.hidden
