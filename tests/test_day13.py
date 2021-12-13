# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day13


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day13"""
    @parameterized.expand([
        ("data/day13a.txt", 17),
    ])
    def test_part1(self, filename, expected):
        f = open(filename)
        self.assertEquals(day13.part1(f.read().splitlines()), expected)


if __name__ == '__main__':
    unittest.main()
