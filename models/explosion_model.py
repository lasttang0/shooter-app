import random
from os import path
import pygame
from utils.constants import IMG_DIR, Colors, Explosions, LARGE_SIZE, SMALL_SIZE, DEATH_SIZE, SND_DIR, EXPLOSION_SOUND


class ExplosionModel(pygame.sprite.Sprite):
    """
    ExplosionModel class represents an explosion in the game.

    Attributes:
        size (int): The size of the explosion (LARGE, SMALL, DEATH).
        animation (dict): A dictionary containing lists of explosion images for each size.
        image (pygame.Surface): The current image of the explosion.
        rect (pygame.Rect): The rectangular bounds of the explosion.
        frame (int): The current frame of the explosion animation.
        last_update (int): The time of the last frame update.
        frame_rate (int): The frame rate of the explosion animation.

    Methods:
        explosion_animation(): Create the explosion animation for different sizes.
        update(): Update the explosion animation.
        play_sound(): Play a random explosion sound.
    """

    def __init__(self, center, size):
        """
        Initialize an instance of ExplosionModel.

        Args:
            center (tuple): The center coordinates of the explosion.
            size (int): The size of the explosion (LARGE, SMALL, DEATH).
        """
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.animation = self.explosion_animation()
        self.image = self.animation[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    @staticmethod
    def explosion_animation():
        """
        Create the explosion animation for different sizes.

        Returns:
            dict: A dictionary containing lists of explosion images for each size.
        """
        animation = {
            Explosions.LARGE: [],
            Explosions.SMALL: [],
            Explosions.DEATH: [],
        }
        for x in range(9):
            file = f'explosion{x}.png'
            image = pygame.image.load(path.join(IMG_DIR, 'explosion', file)).convert()
            image.set_colorkey(Colors.BLACK.value)
            animation[Explosions.LARGE].append(pygame.transform.scale(image, (LARGE_SIZE, LARGE_SIZE)))
            animation[Explosions.SMALL].append(pygame.transform.scale(image, (SMALL_SIZE, SMALL_SIZE)))
            animation[Explosions.DEATH].append(pygame.transform.scale(image, (DEATH_SIZE, DEATH_SIZE)))
        return animation

    def update(self):
        """
        Update the explosion animation.
        """
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.animation[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.animation[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    @staticmethod
    def play_sound():
        """
        Play a random explosion sound.
        """
        pygame.mixer.Sound(path.join(SND_DIR, random.choice(EXPLOSION_SOUND))).play()
