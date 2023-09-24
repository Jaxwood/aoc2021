# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized
from src import day12


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day12"""
    @parameterized.expand([
        ("data/day12a.txt", True, 10),
        ("data/day12b.txt", True, 19),
        ("data/day12c.txt", True, 226),
        ("data/day12.txt", True, 4411),
        ("data/day12a.txt", False, 36),
        ("data/day12b.txt", False, 103),
        ("data/day12c.txt", False, 3509),
        ("data/day12.txt", False, 136767),
        ])
    def test_part1(self, filename, part1, expected):
        f = open(filename)
        self.assertEqual(day12.part1(f.read().splitlines(), part1), expected)


if __name__ == '__main__':
    unittest.main()
