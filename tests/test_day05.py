# -*- coding: utf-8 -*-
import unittest
from src import day05


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day05"""

    def test_overlaps(self):
        coords = [
            "0,9 -> 5,9",
            "8,0 -> 0,8",
            "9,4 -> 3,4",
            "2,2 -> 2,1",
            "7,0 -> 7,4",
            "6,4 -> 2,0",
            "0,9 -> 2,9",
            "3,4 -> 1,4",
            "0,0 -> 8,8",
            "5,5 -> 8,2"
        ]
        self.assertEquals(day05.overlap(coords), 5)

    def test_part1(self):
        f = open('data/day05.txt')
        self.assertEquals(day05.overlap(f.read().splitlines()), 6311)

if __name__ == '__main__':
    unittest.main()
