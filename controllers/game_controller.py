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
            self.update_game()
            self.render_game()
            self.quit_game()

    @staticmethod
    def handle_events():
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

    def update_game(self):
        pass

    def render_game(self):
        self.view.screen.fill(Colors.BLACK)
        pygame.display.flip()

    @staticmethod
    def quit_game():
        pygame.quit()
        sys.exit()
