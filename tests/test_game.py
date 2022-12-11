import pytest

from snake.game import SnakeGame, RIGHT
from unittest.mock import MagicMock, patch

START_SMALL_LEFT = """
######
#*   #
#G   #
#    #
######
""".strip()

START_SMALL_CENTER = """
######
#*   #
# G  #
#    #
######
""".strip()


def test_create_game():
    """game object is created"""
    s = SnakeGame(size=(10, 10), start_pos=(5, 5))
    assert s.size == (10, 10)
    assert s.running


def test_create_out_of_bounds():
    """start position has to be within playing field"""
    with pytest.raises(ValueError):
        s = SnakeGame(size=(10, 10), start_pos=(-99, -99))


@patch("random.randint", MagicMock(return_value=1))
def test_move():
    """update moves player"""
    s = SnakeGame(size=(6, 5), start_pos=(1, 2))
    s.update()
    assert str(s) == START_SMALL_CENTER


@patch("random.randint", MagicMock(return_value=1))
def test_move_up():
    """player changes direction"""
    s = SnakeGame(size=(6, 5), start_pos=(1, 2))
    s.set_direction(RIGHT)
    s.update()
    assert str(s) == START_SMALL_CENTER


@patch("random.randint", MagicMock(return_value=1))
@pytest.mark.parametrize(
    "start_pos,expected",
    [
        ((1, 2), START_SMALL_LEFT),
        ((2, 2), START_SMALL_CENTER),
    ],
)
def test_string_repr(start_pos, expected):
    """start_pos puts player in correct position"""
    s = SnakeGame(size=(6, 5), start_pos=start_pos)
    assert str(s) == expected
