import curses
from snake import Snake
from food import Food
from score import Score

class Game:
    def __init__(self, board_width: int = 20, board_height: int = 20):
        self.snake = Snake(board_width, board_height)
        self.food = Food(board_width, board_height)
        self.score = Score()
        self.running = False
        self.paused = False
        self.board_width = board_width
        self.board_height = board_height
        self.speed = 200  # Initial speed in milliseconds

    def start_game(self) -> None:
        """Initialize the game and start the game loop."""
        self.running = True
        curses.wrapper(self.game_loop)

    def pause_game(self) -> None:
        """Pause the game."""
        self.paused = True

    def resume_game(self) -> None:
        """Resume the game."""
        self.paused = False

    def end_game(self) -> None:
        """End the game and exit."""
        self.running = False
        curses.endwin()
        print(f"Game Over! Your score is {self.score.get_points()}")

    def update_game(self, screen) -> None:
        """Update the game state and redraw the screen."""
        screen.clear()
        # Draw the snake
        for segment in self.snake.body:
            screen.addstr(segment[1], segment[0], 'O')
        # Draw the food
        screen.addstr(self.food.get_position()[1], self.food.get_position()[0], '*')
        # Draw the score
        screen.addstr(0, 0, f'Score: {self.score.get_points()}')
        screen.refresh()

    def game_loop(self, screen) -> None:
        """The main game loop."""
        curses.curs_set(0)  # Hide the cursor
        screen.nodelay(True)  # Don't block I/O calls
        key_mappings = {curses.KEY_UP: 'UP', curses.KEY_DOWN: 'DOWN', curses.KEY_LEFT: 'LEFT', curses.KEY_RIGHT: 'RIGHT'}
        while self.running:
            if self.paused:
                screen.addstr(self.board_height // 2, self.board_width // 2 - len('PAUSED') // 2, 'PAUSED')
                screen.refresh()
                curses.napms(100)  # Sleep for a while to keep the CPU usage low
                continue

            # Get user input
            key = screen.getch()
            if key in key_mappings:
                self.snake.change_direction(key_mappings[key])
            elif key == ord('p'):
                self.pause_game()
            elif key == ord('r'):
                self.resume_game()
            elif key == ord('q'):
                self.end_game()
                break
            elif key == curses.KEY_RESIZE:
                self.board_width, self.board_height = screen.getmaxyx()
                self.snake.board_width, self.snake.board_height = self.board_width, self.board_height
                self.food.board_width, self.food.board_height = self.board_width, self.board_height
                continue

            # Move the snake
            if not self.snake.move():
                self.end_game()
                break

            # Check for food collision
            if self.snake.body[0] == self.food.get_position():
                self.snake.grow()
                self.food.reposition(self.snake.body)
                self.score.increase()
                self.adjust_speed()

            self.update_game(screen)
            curses.napms(self.speed)  # Sleep for a while to control game speed

    def adjust_speed(self) -> None:
        """Adjust the game speed based on the score to increase difficulty."""
        self.speed = max(50, 200 - (self.score.get_points() // 5) * 10)
