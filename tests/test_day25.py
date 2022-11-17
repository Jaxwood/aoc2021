# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day25


class Day25TestSuite(unittest.TestCase):
    """Test Suite for Day25"""

    @parameterized.expand([
        ('data/day25.txt', 58),
    ])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEquals(day25.part1(f.read().splitlines()), expected)


if __name__ == '__main__':
    unittest.main()
