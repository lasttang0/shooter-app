import configparser
from enum import Enum
from os import path

config = configparser.ConfigParser()
config.read('utils/config.ini')

"""
Directories for image and sound assets.
"""
IMG_DIR = path.join(path.dirname(__file__), '..\\assets\\images')
SND_DIR = path.join(path.dirname(__file__), '..\\assets\\sounds')

"""
Screen and display settings, including screen dimensions, frames per second (FPS), font settings,
and asset file paths.
"""
SKY = 'sky.png'
SPACE_MUSIC = 'space.wav'
SCREEN_WIDTH = config.getint('ScreenSettings', 'SCREEN_WIDTH')
SCREEN_HEIGHT = config.getint('ScreenSettings', 'SCREEN_HEIGHT')
FPS = config.getint('ScreenSettings', 'FPS')
FONT = config.get('ScreenSettings', 'FONT')
FONT_SIZE = config.getint('ScreenSettings', 'FONT_SIZE')

"""
Sound settings.
"""
MUSIC_VOLUME = config.getfloat('SoundSettings', 'MUSIC_VOLUME')

"""
Player-related settings, including player's attributes, such as size, speed, health, lives, and more.
"""
STARSHIP = 'starship.png'
LIVES = config.getint('PlayerSettings', 'LIVES')
PLAYER_WIDTH = config.getint('PlayerSettings', 'PLAYER_WIDTH')
PLAYER_HEIGHT = config.getint('PlayerSettings', 'PLAYER_HEIGHT')
PLAYER_SPEED = config.getint('PlayerSettings', 'PLAYER_SPEED')
SPEED_CHANGE = config.getint('PlayerSettings', 'SPEED_CHANGE')
COLLIDE_RADIUS = config.getint('PlayerSettings', 'COLLIDE_RADIUS')
HEALTH = config.getint('PlayerSettings', 'HEALTH')
BAR_HEIGHT = config.getint('PlayerSettings', 'BAR_HEIGHT')
HIDING_TIME = config.getint('PlayerSettings', 'HIDING_TIME')
DYING_TIME = config.getint('PlayerSettings', 'DYING_TIME')

"""
Asteroid-related settings, including lists of asteroid images, sizes, and parameters like speed and rotation.
"""
ASTEROID_LIST = ['asteroid1.png', 'asteroid2.png', 'asteroid3.png', 'asteroid4.png']
ASTEROID_SIZES = [0.8, 1, 1, 1, 1.4, 1.5, 1.75]
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

"""
Rocket-related settings, including rocket dimensions and speed.
"""
PEW = 'pew.wav'
ROCKET_WIDTH = config.getint('RocketSettings', 'ROCKET_WIDTH')
ROCKET_HEIGHT = config.getint('RocketSettings', 'ROCKET_HEIGHT')
ROCKET_SPEED = config.getint('RocketSettings', 'ROCKET_SPEED')
HIT_RADIUS = config.getint('RocketSettings', 'HIT_RADIUS')

"""
Explosion-related settings, including explosion sound files and explosion animation sizes.
"""
EXPLOSION_SOUND = ['explosion1.wav', 'explosion2.wav']
LARGE_SIZE = config.getint('ExplosionSettings', 'LARGE_SIZE')
SMALL_SIZE = config.getint('ExplosionSettings', 'SMALL_SIZE')
DEATH_SIZE = config.getint('ExplosionSettings', 'DEATH_SIZE')


class GameStates(Enum):
    """
    Enumeration of game states.

    Attributes:
        RUNNING: Represents the running state of the game.
        EXIT: Represents the exit state of the game.
    """
    RUNNING = 0
    EXIT = 1


class Colors(Enum):
    """
    Enumeration of color values.

    Attributes:
        BLACK: Represents the color black.
        WHITE: Represents the color white.
        RED: Represents the color red.
        GREEN: Represents the color green.
        BLUE: Represents the color blue.
        YELLOW: Represents the color yellow.
        ORANGE: Represents the color orange.
    """
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    ORANGE = (255, 125, 0)


class Explosions(Enum):
    """
    Enumeration of explosion types.

    Attributes:
        LARGE: Represents a large explosion.
        SMALL: Represents a small explosion.
        DEATH: Represents a death explosion.
    """
    LARGE = 0
    SMALL = 1
    DEATH = 2
