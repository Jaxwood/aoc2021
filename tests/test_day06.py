# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day06


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day06"""

    @parameterized.expand([
        (False, 5),
        (True, 12)
    ])
    def test_part1(self, days, expected):
        sequence = "3,4,3,1,2"
        self.assertEquals(day06.part1(sequence, days, expected))

if __name__ == '__main__':
    unittest.main()
