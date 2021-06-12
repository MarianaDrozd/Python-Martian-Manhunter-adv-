import pytest
from game import TicTacToe

my_game = TicTacToe()


def setup():
    my_game.board[4] = "X"
    my_game.board[5] = "0"
    my_game.board[6] = "X"


def test_available_moves():
    assert 4 not in my_game.available_moves()
    assert 5 not in my_game.available_moves()
    assert 3 in my_game.available_moves()
    assert 1 in my_game.available_moves()
    assert 8 in my_game.available_moves()


def test_available_moves_negative():
    with pytest.raises(AssertionError):
        assert 9 in my_game.available_moves()
        assert -1 in my_game.available_moves()


def test_make_move():
    assert my_game.make_move(4, "X") is False
    assert my_game.make_move(5, "X") is False
    assert my_game.make_move(7, "X") is True


def test_make_move_negative():
    with pytest.raises(IndexError):
        assert my_game.make_move(9, "X") is False
        assert my_game.make_move(-1, "0") is False
