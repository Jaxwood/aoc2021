# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day13


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day13"""
    @parameterized.expand([
        ("data/day13a.txt", True, 17),
        ("data/day13.txt", True, 621),
        ("data/day13.txt", False, 95),
    ])
    def test_part1(self, filename, one_fold_only, expected):
        f = open(filename)
        self.assertEqual(day13.part1(f.read().splitlines(), one_fold_only),
                          expected)


if __name__ == '__main__':
    unittest.main()
