import configparser
from enum import Enum

config = configparser.ConfigParser()
config.read('utils/config.ini')

SCREEN_WIDTH = config.getint('ScreenSettings', 'SCREEN_WIDTH')
SCREEN_HEIGHT = config.getint('ScreenSettings', 'SCREEN_HEIGHT')
FPS = config.getint('ScreenSettings', 'FPS')

PLAYER_WIDTH = config.getint('PlayerSettings', 'PLAYER_WIDTH')
PLAYER_HEIGHT = config.getint('PlayerSettings', 'PLAYER_HEIGHT')
PLAYER_SPEED = config.getint('PlayerSettings', 'PLAYER_SPEED')
SPEED_CHANGE = config.getint('PlayerSettings', 'SPEED_CHANGE')

COUNT = config.getint('AsteroidSettings', 'COUNT')
ASTEROID_WIDTH = config.getint('AsteroidSettings', 'ASTEROID_WIDTH')
ASTEROID_HEIGHT = config.getint('AsteroidSettings', 'ASTEROID_HEIGHT')
SPAWN_Y_MIN = config.getint('AsteroidSettings', 'SPAWN_Y_MIN')
SPAWN_Y_MAX = config.getint('AsteroidSettings', 'SPAWN_Y_MAX')
ASTEROID_SPEED_X_MIN = config.getint('AsteroidSettings', 'ASTEROID_SPEED_X_MIN')
ASTEROID_SPEED_X_MAX = config.getint('AsteroidSettings', 'ASTEROID_SPEED_X_MAX')
ASTEROID_SPEED_Y_MIN = config.getint('AsteroidSettings', 'ASTEROID_SPEED_Y_MIN')
ASTEROID_SPEED_Y_MAX = config.getint('AsteroidSettings', 'ASTEROID_SPEED_Y_MAX')


class GameStates(Enum):
    RUNNING = 1
    EXIT = 2


class Colors(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
