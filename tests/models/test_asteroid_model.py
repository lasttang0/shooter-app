import pygame

from models.asteroid_model import AsteroidModel


def test_asteroid_model_creation(game_controller):
    asteroid = AsteroidModel()

    # Проверяем, что объект AsteroidModel был создан корректно
    assert isinstance(asteroid, AsteroidModel)
    assert isinstance(asteroid.image, pygame.Surface)
    assert isinstance(asteroid.rect, pygame.Rect)
    assert isinstance(asteroid.speed_x, int)
    assert isinstance(asteroid.speed_y, int)
    assert isinstance(asteroid.radius, int)
    assert isinstance(asteroid.rotation, int)


def test_asteroid_model_update(game_controller):
    asteroid = AsteroidModel()

    # Запоминаем начальные координаты
    initial_x = asteroid.rect.x
    initial_y = asteroid.rect.y

    # Вызываем метод update
    asteroid.update()

    # Проверяем, что координаты  изменились (если ожидается)
    assert asteroid.rect.x != initial_x or asteroid.rect.y != initial_y



