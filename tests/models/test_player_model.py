import pygame
from models.player_model import PlayerModel
from utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, HEALTH, PLAYER_SPEED, COLLIDE_RADIUS, LIVES, HIDING_TIME


# Тесты для класса PlayerModel
class TestPlayerModel:

    # Тест, проверяющий начальное состояние игрока
    def test_player_initial_state(self, pygame_initialized):
        player = PlayerModel()

        assert player.health == HEALTH
        assert player.speed_x == PLAYER_SPEED
        assert player.radius == COLLIDE_RADIUS
        assert player.lives == LIVES
        assert not player.hidden
        assert player.death_moment is None

    # Тест, проверяющий, что игрок остается в пределах экрана
    def test_player_boundary(self, pygame_initialized):
        player = PlayerModel()
        player.rect.centerx = 0

        # Вызываем метод update для игрока
        player.update()

        # Проверяем, что игрок не выходит за левую границу экрана
        assert player.rect.left == 0

        player.rect.centerx = SCREEN_WIDTH

        # Вызываем метод update для игрока
        player.update()

        # Проверяем, что игрок не выходит за правую границу экрана
        assert player.rect.right == SCREEN_WIDTH

    # Дополнительный тест для метода hide
    def test_player_hide(self, pygame_initialized):
        player = PlayerModel()
        player.hide()

        assert player.hidden
        assert player.rect.center == (SCREEN_WIDTH / 2, SCREEN_HEIGHT + 200)

    # Дополнительный тест для метода hide с проверкой таймера
    def test_player_hide_timer(self, pygame_initialized):
        player = PlayerModel()
        player.hide()
        player.hide_timer = pygame.time.get_ticks() - HIDING_TIME - 1

        player.update()

        assert not player.hidden
