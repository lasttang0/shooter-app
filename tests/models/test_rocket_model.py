import pygame
from models.rocket_model import RocketModel
from utils.constants import HIT_RADIUS


def test_rocket_model_creation(pygame_initialized):
    x, y = 100, 200
    rocket = RocketModel(x, y)

    assert isinstance(rocket, RocketModel)
    assert isinstance(rocket.image, pygame.Surface)
    assert isinstance(rocket.rect, pygame.Rect)
    assert rocket.rect.centerx == x
    assert rocket.rect.bottom == y
    assert isinstance(rocket.speed_y, int)
    assert rocket.radius == HIT_RADIUS


def test_rocket_model_update(pygame_initialized):
    x, y = 100, 200
    rocket = RocketModel(x, y)
    initial_rect_y = rocket.rect.y

    rocket.update()

    assert rocket.rect.y == initial_rect_y + rocket.speed_y
