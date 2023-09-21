import configparser
from enum import Enum
from os import path

IMG_DIR = path.join(path.dirname(__file__), '..\\assets\\images')

config = configparser.ConfigParser()
config.read('utils/config.ini')

SCREEN_WIDTH = config.getint('ScreenSettings', 'SCREEN_WIDTH')
SCREEN_HEIGHT = config.getint('ScreenSettings', 'SCREEN_HEIGHT')
FPS = config.getint('ScreenSettings', 'FPS')
FONT = config.get('ScreenSettings', 'FONT')
FONT_SIZE = config.getint('ScreenSettings', 'FONT_SIZE')

PLAYER_WIDTH = config.getint('PlayerSettings', 'PLAYER_WIDTH')
PLAYER_HEIGHT = config.getint('PlayerSettings', 'PLAYER_HEIGHT')
PLAYER_SPEED = config.getint('PlayerSettings', 'PLAYER_SPEED')
SPEED_CHANGE = config.getint('PlayerSettings', 'SPEED_CHANGE')
COLLIDE_RADIUS = config.getint('PlayerSettings', 'COLLIDE_RADIUS')

ASTEROID_LIST = ["asteroid1.png", "asteroid2.png", "asteroid3.png", "asteroid4.png"]
ASTEROID_SIZES = [0.8, 1, 1.1, 1.2, 1.75]
COUNT = config.getint('AsteroidSettings', 'COUNT')
ASTEROID_WIDTH = config.getint('AsteroidSettings', 'ASTEROID_WIDTH')
ASTEROID_HEIGHT = config.getint('AsteroidSettings', 'ASTEROID_HEIGHT')
SPAWN_Y_MIN = config.getint('AsteroidSettings', 'SPAWN_Y_MIN')
SPAWN_Y_MAX = config.getint('AsteroidSettings', 'SPAWN_Y_MAX')
ASTEROID_SPEED_X_MIN = config.getint('AsteroidSettings', 'ASTEROID_SPEED_X_MIN')
ASTEROID_SPEED_X_MAX = config.getint('AsteroidSettings', 'ASTEROID_SPEED_X_MAX')
ASTEROID_SPEED_Y_MIN = config.getint('AsteroidSettings', 'ASTEROID_SPEED_Y_MIN')
ASTEROID_SPEED_Y_MAX = config.getint('AsteroidSettings', 'ASTEROID_SPEED_Y_MAX')
ROTATION_SPEED_MIN = config.getint('AsteroidSettings', 'ROTATION_SPEED_MIN')
ROTATION_SPEED_MAX = config.getint('AsteroidSettings', 'ROTATION_SPEED_MAX')

ROCKET_WIDTH = config.getint('RocketSettings', 'ROCKET_WIDTH')
ROCKET_HEIGHT = config.getint('RocketSettings', 'ROCKET_HEIGHT')
ROCKET_SPEED = config.getint('RocketSettings', 'ROCKET_SPEED')
HIT_RADIUS = config.getint('RocketSettings', 'HIT_RADIUS')



class GameStates(Enum):
    RUNNING = 1
    EXIT = 2


class Colors(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 125, 0)
