import random

class Food:
    def __init__(self, board_width: int, board_height: int):
        """
        Initialize the food object with a random position on the board.
        
        Args:
            board_width (int): The width of the game board.
            board_height (int): The height of the game board.
        """
        self.board_width = board_width
        self.board_height = board_height
        self.position = self._generate_random_position()

    def _generate_random_position(self) -> tuple:
        """
        Generate a random position on the board that is not occupied by the snake.
        
        Returns:
            tuple: A tuple representing the random position on the board.
        """
        return (random.randint(0, self.board_width - 1),
                random.randint(0, self.board_height - 1))

    def reposition(self, snake_body) -> None:
        """
        Reposition the food to a new random location on the board that is not occupied by the snake.
        
        Args:
            snake_body (list): A list of tuples representing the snake's body.
        """
        new_position = self._generate_random_position()
        while new_position in snake_body:
            new_position = self._generate_random_position()
        self.position = new_position

    def get_position(self) -> tuple:
        """
        Get the current position of the food.
        
        Returns:
            tuple: A tuple representing the food's position on the board.
        """
        return self.position
