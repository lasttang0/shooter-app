from controllers.game_controller import GameController
from views.game_view import GameView
from models.game_model import GameModel


def main():
    model = GameModel()
    view = GameView()
    controller = GameController(model, view)
    controller.start_game()


if __name__ == '__main__':
    main()
