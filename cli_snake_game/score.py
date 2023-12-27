## score.py

class Score:
    def __init__(self):
        """
        Initialize the score with a default value of 0.
        """
        self._points = 0

    def increase(self, amount: int = 1) -> None:
        """
        Increase the score by a specified amount, defaulting to 1.

        Args:
            amount (int): The amount to increase the score by. Defaults to 1.
        """
        self._points += amount

    def reset(self) -> None:
        """
        Reset the score to 0.
        """
        self._points = 0

    def get_points(self) -> int:
        """
        Get the current score points.

        Returns:
            int: The current score points.
        """
        return self._points
