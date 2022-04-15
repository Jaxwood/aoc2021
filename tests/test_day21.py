# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day21


class Day21TestSuite(unittest.TestCase):
    """Test Suite for Day21"""
    @parameterized.expand([
        (4, 8, 739785),
        (2, 7, 805932),
    ])
    def test_part1(self, player1, player2, expected):
        self.assertEquals(day21.part1(player1, player2), expected)


if __name__ == '__main__':
    unittest.main()
