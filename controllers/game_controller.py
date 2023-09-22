import pygame

from models.game_model import GameModel
from models.explosion_model import ExplosionModel
from utils.constants import GameStates, FPS, ASTEROID_WIDTH, Explosions, DYING_TIME, HEALTH


class GameController:
    """
    GameController class manages the game's logic and controls the game loop.

    Attributes:
        model (GameModel): The game's model, containing the game's data.
        view (GameView): The game's view, responsible for rendering the game.
        game_state (GameStates): The current state of the game.
        game_over (bool): Flag indicating whether the game is over.

    Methods:
        start_game(): Starts the game loop and manages the game's flow.
        handle_events(): Handles user input events during the game.
        update_game(): Updates the game's state, including collisions and scoring.
    """

    def __init__(self, model, view):
        """
        Initialize the GameController with the provided model and view.

        Args:
            model (GameModel): The game's model, containing the game's data.
            view (GameView): The game's view, responsible for rendering the game.
        """
        self.model = model
        self.view = view
        self.game_state = GameStates.RUNNING
        self.game_over = True

    def start_game(self):
        """
        Starts the game loop and manages the game's flow.
        """
        while self.game_state is GameStates.RUNNING:
            if self.game_over:
                self.view.open_screen()
                self.game_over = False
                self.model = GameModel()
            self.view.clock.tick(FPS)
            self.handle_events()
            self.view.render_game(self.model)
            self.update_game()

    def handle_events(self):
        """
        Handles user input events during the game.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameStates.EXIT
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.model.player.hidden:
                self.model.add_rocket(self.model.player.rect.centerx, self.model.player.rect.top)

    def update_game(self):
        """
        Updates the game's state, including collisions and scoring.
        """
        self.model.all_sprites.update()

        hits = pygame.sprite.groupcollide(self.model.asteroids, self.model.rockets, True, True,
                                          pygame.sprite.collide_circle)
        for hit in hits:
            self.model.score += ASTEROID_WIDTH - hit.radius
            ExplosionModel.play_sound()
            self.model.add_explosion(hit.rect.center, Explosions.LARGE)
            self.model.add_asteroids(len(hits))

        collides = pygame.sprite.spritecollide(self.model.player, self.model.asteroids, True,
                                               pygame.sprite.collide_circle)
        for collide in collides:
            self.model.player.health -= collide.radius
            ExplosionModel.play_sound()
            self.model.add_explosion(collide.rect.center, Explosions.SMALL)
            self.model.add_asteroids(len(collides))
            if self.model.player.health <= 0:
                self.model.add_explosion(collide.rect.center, Explosions.DEATH)
                self.model.player.death_moment = pygame.time.get_ticks()
                self.model.player.hide()
                self.model.player.lives -= 1
                self.model.player.health = HEALTH
        if (self.model.player.lives == 0 and self.model.player.death_moment and
                pygame.time.get_ticks() - self.model.player.death_moment >= DYING_TIME):
            # self.model.player.kill()
            # self.game_state = GameStates.EXIT
            self.game_over = True
