from os import path

import pygame

from utils.constants import IMG_DIR, Colors, Explosions, LARGE_SIZE, SMALL_SIZE


class ExplosionModel(pygame.sprite.Sprite):
    def __init__(self, center, size):
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
        animation = {
            Explosions.LARGE: [],
            Explosions.SMALL: [],
        }
        for x in range(9):
            file = f'explosion{x}.png'
            image = pygame.image.load(path.join(IMG_DIR, 'explosion', file)).convert()
            image.set_colorkey(Colors.BLACK.value)
            animation[Explosions.LARGE].append(pygame.transform.scale(image, (LARGE_SIZE, LARGE_SIZE)))
            animation[Explosions.SMALL].append(pygame.transform.scale(image, (SMALL_SIZE, SMALL_SIZE)))
        return animation

    def update(self):
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
