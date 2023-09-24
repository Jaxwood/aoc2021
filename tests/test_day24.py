# -*- coding: utf-8 -*-
from typing import List, Tuple
import unittest
from parameterized import parameterized
from src import day24


class Day24TestSuite(unittest.TestCase):
    """Test Suite for Day24"""

    @parameterized.expand([
        ('data/day24a.txt', 12521),
    ])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEqual(day24.part1(f.read().splitlines()), expected)


if __name__ == '__main__':
    unittest.main()
