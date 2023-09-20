import pygame
from utils.constants import Colors, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGTH, PLAYER_SPEED


class PlayerModel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGTH))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.image.fill(Colors.GREEN.value)

    # def move_left(self):
    #     self.rect.x -= PLAYER_SPEED
    #     if self.rect.left < PLAYER_WIDTH:
    #         self.rect.right = 0
    #
    # def move_right(self):
    #     self.rect.x += PLAYER_SPEED
    #     if self.rect.left > PLAYER_WIDTH:
    #         self.rect.right = 0
