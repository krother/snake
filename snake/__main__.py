"""
This module contains the user interface
"""
import curses
import time
from snake.game import SnakeGame, UP, DOWN, LEFT, RIGHT


# ASCII codes of characters on the keyboard
# KEY_COMMANDS = {97: LEFT, 100: RIGHT, 119: UP, 115: DOWN}
KEY_COMMANDS = {68: LEFT, 67: RIGHT, 66: DOWN, 65: UP}

COLORS = {
    'O': 1,
    'G': 1,
    '#': 2,
    '*': 3
}

SPEED = 50000


def prepare_screen():
    """Initialize the screen"""
    screen = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.curs_set(0)
    curses.noecho()
    curses.raw()
    screen.keypad(False)
    win = curses.newwin(40, 21, 0, 0)
    win.nodelay(True)
    return win, screen


def draw(game, win, screen):
    # separate functions draw_player and draw_playground
    screen.clear()
    for y, row in enumerate(game.field):
        for x, char in enumerate(row):
            if char != ' ':
                col = COLORS.get(char, 1)
                screen.addch(y, x, char, curses.color_pair(col))

    win.refresh()
    screen.refresh()


win, screen = prepare_screen()


def game_loop(screen):
    """implements the Event Loop pattern"""
    game = SnakeGame((40, 20), (3, 10), init_food=True)
    draw(game, win, screen)

    delay = SPEED

    while game.running:
        # move the player
        char = win.getch() # returns the code of a pressed key
        direction = KEY_COMMANDS.get(char)  # direction is a tuple or None
        if direction:
            game.set_direction(direction)

        delay -= 1
        if delay == 0:
            delay = SPEED 
            game.update()
            draw(game, win, screen)

    time.sleep(2)



if __name__ == "__main__":
    curses.wrapper(game_loop)
    curses.endwin()
