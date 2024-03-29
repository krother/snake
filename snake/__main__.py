"""
This module contains the user interface
"""
from snake.game import SnakeGame
from snake.game import UP, DOWN, LEFT, RIGHT
import curses
import time

#
# ASCII codes of characters on the keyboard
#
# AWSD should work on all operating systems
KEY_COMMANDS = {97: LEFT, 100: RIGHT, 119: UP, 115: DOWN}

# arrow keys - codes differ between operating systems
# KEY_COMMANDS = {68: LEFT, 67: RIGHT, 66: DOWN, 65: UP}

# size of the playing field
XSIZE, YSIZE = 25, 20

# game delay (higher=slower)
SPEED = 200000

# unicode symbols for drawing
SYMBOLS = {
    '#': '\U0001F9F1',
    '*': '\U0001F34E',
    'G': '\U0001F7E9',
    'O': '\U0001F7E2',
}


def prepare_screen():
  """Initialize the screen"""
  curses.initscr()
  curses.start_color()
  curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
  curses.curs_set(0); curses.noecho(); curses.raw()


def draw(game, win, screen):
  """draws characters for playing field, fruit and snake"""
  screen.clear()
  for x,y,char in game.get_symbols():
    char = SYMBOLS.get(char, char)
    screen.addch(y,      x*2,        char,        curses  .  color_pair(1))
  win.refresh   ( )
  screen.refresh( )


def game_loop(screen):
    """implements the Event Loop pattern"""
    screen.keypad(False)
    win = curses.newwin(XSIZE, YSIZE + 1, 0, 0)
    win.nodelay(True)

    game = SnakeGame((XSIZE, YSIZE), (3, 10))
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

    # game over
    time.sleep(2)



if __name__ == "__main__":
    prepare_screen()
    curses.wrapper(game_loop)
    curses.endwin()
