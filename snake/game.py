
from snake.player import Snake
from snake.playing_field import PlayingField
from snake.player import UP, DOWN, LEFT, RIGHT



SNAKE_SYMBOL = 'O'
HEAD_SYMBOL = 'G'
WALL_SYMBOL = '#'
FOOD_SYMBOL = '*'



class SnakeGame:

    def __init__(self, size, start_pos):
        self.snake = Snake(*start_pos)
        self.playing_field = PlayingField(size)
        self.running = True
        self.playing_field.add_random_food()

    @property
    def size(self):
        return self.playing_field.size

    @property
    def field(self):
        field = [
            [' ' for x in range(self.playing_field.xsize)]
            for y in range(self.playing_field.ysize)
            ]
        for x, y in self.playing_field.walls:
            field[y][x] = WALL_SYMBOL
        if self.playing_field.food:
            field[self.playing_field.food[1]][self.playing_field.food[0]] = FOOD_SYMBOL

        for x, y in self.snake.tail:
            field[y][x] = SNAKE_SYMBOL
        field[self.snake.head[1]][self.snake.head[0]] = HEAD_SYMBOL
        return field

    def to_string(self):
        return '\n'.join([''.join(row) for row in self.field])
    
    def set_direction(self, direction):
        self.snake.direction = direction

    def update(self):
        self.snake.forward()
        self.snake.eat(self.playing_field)
        if not self.playing_field.food:
            self.playing_field.add_random_food()
        if self.snake.check_collision(self.playing_field):
            self.running = False

