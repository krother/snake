
from snake.player import Snake
from snake.playing_field import PlayingField
from snake.player import UP, DOWN, LEFT, RIGHT



SNAKE_SYMBOL = 'O'
HEAD_SYMBOL = 'G'
WALL_SYMBOL = '#'
FOOD_SYMBOL = '*'



class SnakeGame:

    def __init__(self, size, start_pos):
        self.validate_positions(size, start_pos)
        self.snake = Snake(head=start_pos)
        self.playing_field = PlayingField(size)
        self.running = True
        self.playing_field.add_random_food()

    def __repr__(self):
        """returns a string representation for convenience and debugging"""
        result = ""
        symbols = {(x, y): char for x, y, char in self.get_symbols()}
        for y in range(self.size[1]):
            for x in range(self.size[0]):
                result += symbols.get((x, y), " ")
            result += "\n"
        return result[:-1]
    
    def validate_positions(self, size, start_pos):
        """starting position has to be on playing field"""
        if (
            start_pos[0] < 0 or
            start_pos[0] >= size[0] or
            start_pos[1] < 0 or
            start_pos[1] >= size[1]
        ):
            raise ValueError("starting position has to be on playing field")

    @property
    def size(self):
        return self.playing_field.size

    def get_symbols(self):
        """Generates (x, y, char) tuples for everything tile to be drawn"""
        for x, y in self.playing_field.walls:
            yield x, y, WALL_SYMBOL
        if self.playing_field.food:
            yield self.playing_field.food[0], self.playing_field.food[1], FOOD_SYMBOL
        for x, y in self.snake.tail:
            yield x, y, SNAKE_SYMBOL
        yield self.snake.head[0], self.snake.head[1], HEAD_SYMBOL

    def set_direction(self, direction):
        self.snake.direction = direction

    def update(self):
        self.snake.forward()
        self.snake.eat(self.playing_field)
        if not self.playing_field.food:
            self.playing_field.add_random_food()
        if self.snake.check_collision(self.playing_field):
            self.running = False

