
from snake.game import SnakeGame, UP

START_SMALL = """
######
#    #
#G   #
#    #
######
""".strip()

START_SMALL_UP = """
######
#G   #
#    #
#    #
######
""".strip()

START_SMALL_CENTER = """
######
#    #
# G  #
#    #
######
""".strip()

def test_create_game():
    s = SnakeGame(size=(10, 10), start_pos=(5, 5))
    assert s.size == (10, 10)
    assert s.running

def test_to_string():
    s = SnakeGame(size=(6, 5), start_pos=(1, 2))
    assert s.to_string() == START_SMALL

def test_to_string2():
    s = SnakeGame(size=(6, 5), start_pos=(2, 2))
    assert s.to_string() == START_SMALL_CENTER

def test_move():
    s = SnakeGame(size=(6, 5), start_pos=(1, 2))
    s.update()
    assert s.to_string() == START_SMALL_CENTER

def test_set_direction():
    s = SnakeGame(size=(6, 5), start_pos=(1, 2))
    s.set_direction(UP)
    s.update()
    assert s.to_string() == START_SMALL_UP

def test_move_up():
    s = SnakeGame(size=(6, 5), start_pos=(1, 2))
    s.set_direction(UP)
    s.update()
    assert s.to_string() == START_SMALL_UP