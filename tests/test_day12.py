# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day12


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day12"""
    @parameterized.expand([("data/day12a.txt", 10), ("data/day12.txt", 4411)])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEquals(day12.part1(f.read().splitlines()), expected)


if __name__ == '__main__':
    unittest.main()
