# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day15


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day15"""
    @parameterized.expand([
        ("data/day15a.txt", 1, 40),
        ("data/day15.txt", 1, 673),
    ])
    def test_part1(self, filename, times, expected):
        f = open(filename)
        self.assertEquals(day15.part1(f.read().splitlines(), times), expected)


if __name__ == '__main__':
    unittest.main()
