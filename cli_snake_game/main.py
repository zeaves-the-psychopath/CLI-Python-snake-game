## main.py
import curses
from game import Game

class Main:
    @staticmethod
    def main() -> None:
        """
        The main entry point of the application that starts the game.
        """
        game = Game()
        game.start_game()

if __name__ == "__main__":
    Main.main()
