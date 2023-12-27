## snake.py

class Snake:
    def __init__(self, board_width: int, board_height: int):
        # Default initial position and direction
        self.body = [(10, 10), (10, 9), (10, 8)]  # List of tuples representing the snake's body
        self.direction = 'RIGHT'  # Default direction
        self.board_width = board_width
        self.board_height = board_height

    def change_direction(self, new_direction: str) -> None:
        """Change the direction of the snake if the new direction is not opposite to the current one."""
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

    def move(self) -> bool:
        """Move the snake in the current direction. Return False if the snake hits the wall or itself."""
        head_x, head_y = self.body[0]
        new_head = {
            'UP': (head_x, head_y - 1),
            'DOWN': (head_x, head_y + 1),
            'LEFT': (head_x - 1, head_y),
            'RIGHT': (head_x + 1, head_y)
        }.get(self.direction, self.body[0])

        # Check for wall collisions
        if (new_head[0] < 0 or new_head[0] >= self.board_width or
                new_head[1] < 0 or new_head[1] >= self.board_height):
            return False

        # Check if the new head position is already part of the snake's body (collision with itself)
        if new_head in self.body:
            return False

        # Insert the new head position at the beginning of the body list
        self.body.insert(0, new_head)

        # Remove the last segment of the snake's body to simulate movement
        self.body.pop()

        return True

    def grow(self) -> None:
        """Grow the snake by adding a new segment at the position of the current tail."""
        tail_x, tail_y = self.body[-1]
        if len(self.body) > 1:
            second_last_segment_x, second_last_segment_y = self.body[-2]
            new_tail = (tail_x + (tail_x - second_last_segment_x), tail_y + (tail_y - second_last_segment_y))
        else:
            # If the snake has only one segment, simply duplicate the tail
            new_tail = (tail_x, tail_y)
        self.body.append(new_tail)
