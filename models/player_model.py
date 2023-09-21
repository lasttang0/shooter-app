import pygame
from utils.constants import Colors, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, SPEED_CHANGE


class PlayerModel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10)
        self.speed = PLAYER_SPEED
        self.image.fill(Colors.GREEN.value)

    def update(self):
        self.speed = PLAYER_SPEED
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_LEFT]:
            self.speed = -SPEED_CHANGE
        if key_state[pygame.K_RIGHT]:
            self.speed = SPEED_CHANGE
        self.rect.x += self.speed
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
