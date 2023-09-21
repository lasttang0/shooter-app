import sys

import pygame

from models.asteroid_model import AsteroidModel
from models.rocket_model import RocketModel
from utils.constants import Colors, GameStates, FPS


class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.game_state = GameStates.RUNNING

    def start_game(self):
        while self.game_state is GameStates.RUNNING:
            self.view.clock.tick(FPS)
            self.handle_events()
            self.render_game()
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
        hits = pygame.sprite.groupcollide(self.model.asteroids, self.model.rockets, True, True)
        self.model.add_asteroids(len(hits))
        collides = pygame.sprite.spritecollide(self.model.player, self.model.asteroids, False)
        if collides:
            self.game_state = GameStates.EXIT

    def render_game(self):
        self.view.screen.fill(Colors.BLACK.value)
        self.model.all_sprites.draw(self.view.screen)
        pygame.display.flip()

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()
