# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day17


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day17"""
    @parameterized.expand([
        (20, 30, -10, -5, 45),
        (236, 262, -78, -58, 3003),
    ])
    def test_part1(self, x1, x2, y1, y2, expected):
        self.assertEquals(day17.part1((x1, x2), (y1, y2)), expected)


if __name__ == '__main__':
    unittest.main()
