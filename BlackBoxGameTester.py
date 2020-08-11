# Author: Sky Jacobson
# Date: 8/14/20
# Description: Series of tests to make sure BlackBoxGame.py is accurate.

import BlackBoxGame
import unittest

class BlackBoxGameTester(unittest.TestCase):
    """
    This class tests all the classes and methods within BlackBoxGame
    """

    def setUp(self):
        """Initialize an instance of BlackBoxGame"""

        self._BlackBoxGame = BlackBoxGame.BlackBoxGame([(3,2),(1,7),(4,6),(8,8)])

    def test_initialized_board(self):
        """Tests that the board initializes with the atoms in the correct locations."""

        result = self._BlackBoxGame.get_board_object().get_board()
        expected = [
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
            ['e', '', '', '', '', '', '', 'a', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', 'a', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', 'a', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', 'a', 'e'],
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
        ]
        self.assertEqual(result, expected)

    def test_invalid_shot(self):
        """Tests that an invalid shot returns False"""
        result = self._BlackBoxGame.shoot_ray(0, 0)
        self.assertFalse(result)

    def test_hit_down(self):
        """Tests that a hit registers"""
        expected = [
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
            ['e', '', '', '', '', '', '', 'a', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', 'h', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', 'a', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', 'a', 'e'],
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
        ]
        result = self._BlackBoxGame.shoot_ray(0, 2)
        self.assertEqual(result, expected)

    def test_hit_up(self):
        """Tests that a hit registers"""
        expected = [
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
            ['e', '', '', '', '', '', '', 'a', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', 'a', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', 'h', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', 'a', 'e'],
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
        ]
        result = self._BlackBoxGame.shoot_ray(9, 6)
        self.assertEqual(result, expected)

    def test_hit_right(self):
        """Tests that a hit registers"""
        expected = [
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
            ['e', '', '', '', '', '', '', 'h', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', 'a', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', 'a', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', 'a', 'e'],
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
        ]
        result = self._BlackBoxGame.shoot_ray(1, 0)
        self.assertEqual(result, expected)

    def test_hit_left(self):
        """Tests that a hit registers"""
        expected = [
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
            ['e', '', '', '', '', '', '', 'h', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', 'a', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', 'a', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', 'a', 'e'],
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
        ]
        result = self._BlackBoxGame.shoot_ray(1, 9)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()