import sys

import pygame

from utils.constants import Colors, FPS


class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.running = True

    def start_game(self):
        while self.running:
            self.view.clock.tick(FPS)
            self.handle_events()
            self.render_game()
            self.update_game()
        self.quit_game()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update_game(self):
        self.model.all_sprites.update()

    def render_game(self):
        self.view.screen.fill(Colors.BLACK.value)
        self.model.all_sprites.draw(self.view.screen)
        pygame.display.flip()

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()
