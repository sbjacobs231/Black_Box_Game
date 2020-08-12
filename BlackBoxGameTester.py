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

        self._BlackBoxGame = BlackBoxGame.BlackBoxGame([(3,2),(1,7),(4,6),(8,8), (8, 2), (3, 1)])

    def test_initialized_board(self):
        """Tests that the board initializes with the atoms in the correct locations."""

        result = self._BlackBoxGame.get_board_object().get_board()
        expected = [
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
            ['e', '', '', '', '', '', '', 'a', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', 'a', 'a', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', 'a', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', '', '', '', '', '', '', '', 'e'],
            ['e', '', 'a', '', '', '', '', '', 'a', 'e'],
            ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
        ]
        self.assertEqual(result, expected)

    def test_corner_shot(self):
        """Tests that a corner shot returns False"""
        result = self._BlackBoxGame.shoot_ray(0, 0)
        self.assertFalse(result)

    def test_middle_of_the_board_shot(self):
        """Tests that a middle of the board shot returns False"""
        result = self._BlackBoxGame.shoot_ray(3, 4)
        self.assertFalse(result)

    def test_reflection_top_row(self):
        """Tests that a reflection happens in the top row"""
        result = self._BlackBoxGame.shoot_ray(0, 8)
        self.assertEqual((0, 8), result)

    def test_2_reflection_top_row(self):
        """Tests that a reflection happens in the top row"""
        result = self._BlackBoxGame.shoot_ray(0, 6)
        self.assertEqual((0, 6), result)

    def test_reflection_bottom_row(self):
        """Tests that a reflection happens in the bottom row"""
        result = self._BlackBoxGame.shoot_ray(9, 7)
        self.assertEqual((9, 7), result)

    def test_2_reflection_bottom_row(self):
        """Tests that a reflection happens in the bottom row"""
        result = self._BlackBoxGame.shoot_ray(9, 1)
        self.assertEqual((9,1), result)

    def test_reflection_right_column(self):
        """Tests that a reflection happens in the right column"""
        result = self._BlackBoxGame.shoot_ray(7, 9)
        self.assertEqual((7,9), result)

    def test_reflection_left_column(self):
        """Tests that a reflection happens in the left column"""
        result = self._BlackBoxGame.shoot_ray(2, 0)
        self.assertEqual((2,0), result)

    # def test_hit_down(self):
    #     """Tests that a hit registers"""
    #     expected = [
    #         ['c', 'e', 'u', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
    #         ['e', '', '', '', '', '', '', 'a', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', 'h', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', 'a', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', 'a', 'e'],
    #         ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
    #     ]
    #     result = self._BlackBoxGame.shoot_ray(0, 2)
    #     self.assertEqual(result, expected)
    #
    # def test_hit_up(self):
    #     """Tests that a hit registers"""
    #     expected = [
    #         ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
    #         ['e', '', '', '', '', '', '', 'a', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', 'a', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', 'h', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', 'a', 'e'],
    #         ['c', 'e', 'e', 'e', 'e', 'e', 'u', 'e', 'e', 'c']
    #     ]
    #     result = self._BlackBoxGame.shoot_ray(9, 6)
    #     self.assertEqual(result, expected)
    # #
    # def test_hit_right(self):
    #     """Tests that a hit registers"""
    #     expected = [
    #         ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
    #         ['u', '', '', '', '', '', '', 'h', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', 'a', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', 'a', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', 'a', 'e'],
    #         ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
    #     ]
    #     result = self._BlackBoxGame.shoot_ray(1, 0)
    #     self.assertEqual(result, expected)
    #
    # def test_hit_left(self):
    #     """Tests that a hit registers"""
    #     expected = [
    #         ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c'],
    #         ['e', '', '', '', '', '', '', 'h', '', 'u'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', 'a', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', 'a', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', '', 'e'],
    #         ['e', '', '', '', '', '', '', '', 'a', 'e'],
    #         ['c', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'c']
    #     ]
    #     result = self._BlackBoxGame.shoot_ray(1, 9)
    #     self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()