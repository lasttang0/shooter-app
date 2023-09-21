import random
import sys
from os import path

import pygame

from utils.constants import GameStates, FPS, ASTEROID_WIDTH, SND_DIR, EXPLOSION_SOUND, Explosions


class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.game_state = GameStates.RUNNING

    def start_game(self):
        while self.game_state is GameStates.RUNNING:
            self.view.clock.tick(FPS)
            self.handle_events()
            self.view.render_game(self.model)
            self.update_game()
        self.quit_game()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameStates.EXIT
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.model.add_rocket(self.model.player.rect.centerx, self.model.player.rect.top)

    def update_game(self):
        self.model.all_sprites.update()

        hits = pygame.sprite.groupcollide(self.model.asteroids, self.model.rockets, True, True,
                                          pygame.sprite.collide_circle)
        for hit in hits:
            self.model.score += ASTEROID_WIDTH - hit.radius
            pygame.mixer.Sound(path.join(SND_DIR, random.choice(EXPLOSION_SOUND))).play()
            self.model.add_explosion(hit.rect.center, Explosions.LARGE)
            self.model.add_asteroids(len(hits))

        collides = pygame.sprite.spritecollide(self.model.player, self.model.asteroids, True,
                                               pygame.sprite.collide_circle)
        for collide in collides:
            self.model.player.health -= collide.radius * 1.5
            self.model.add_explosion(collide.rect.center, Explosions.SMALL)
            self.model.add_asteroids(len(collides))
            if self.model.player.health <= 0:
                self.game_state = GameStates.EXIT

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()
