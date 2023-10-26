# tests/test_game.py
from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
            new_game=Game()
            # exercise
            grid=new_game.grid
            # verify
            assert type(grid) == list
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase
            # teardown
    def is_valid(self, word):
            # setup
            new_game=Game()
            test_grid = 'KWEUEAKRZ'
            test_word = 'EUREKA'
            # exercice
            new_game.grid = list(test_grid) # Force the grid to a test case
            # verify
            assert new_game.is_valid(test_word) is True
            # teardown
            assert new_game.grid == list(test_grid) # Make sure the grid remained untouched