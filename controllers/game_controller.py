import sys

import pygame

from utils.constants import GameStates, FPS, ASTEROID_WIDTH


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
        self.model.add_asteroids(len(hits))
        collides = pygame.sprite.spritecollide(self.model.player, self.model.asteroids, False,
                                               pygame.sprite.collide_circle)
        if collides:
            self.game_state = GameStates.EXIT

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()
