# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized
from src import day01


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day01"""

    @parameterized.expand([
        ('abcd', 4),
    ])
    def test_length_of_string(self, candidate, expected):
        self.assertEquals(day01.calculate(candidate), expected)


if __name__ == '__main__':
    unittest.main()
