from enum import Enum

WIDTH = 480
HEIGHT = 600
FPS = 60


class GameStates(Enum):
    PLAYING = 1
    GAME_OVER = 2


class Colors(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
