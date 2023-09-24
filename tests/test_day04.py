# -*- coding: utf-8 -*-
import unittest
from src import day04


class Day01TestSuite(unittest.TestCase):
    """Test Suite for Day04"""

    def test_bingo_play(self):
        f = open('data/day04a.txt')
        self.assertEqual(day04.play(f.read().splitlines()), 4512)

    def test_part1(self):
        f = open('data/day04.txt')
        self.assertEqual(day04.play(f.read().splitlines()), 23177)

    def test_bingo_play_until_last_board_wins(self):
        f = open('data/day04a.txt')
        self.assertEqual(day04.play(f.read().splitlines(), True), 1924)

    def test_part2(self):
        f = open('data/day04.txt')
        self.assertEqual(day04.play(f.read().splitlines(), True), 6804)

if __name__ == '__main__':
    unittest.main()
