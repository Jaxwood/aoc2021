# -*- coding: utf-8 -*-
from typing import List, Tuple
import unittest
from parameterized import parameterized
from src import day23


class Day23TestSuite(unittest.TestCase):
    """Test Suite for Day23"""

    @parameterized.expand([
        ('data/day23.txt', False, 12521),
        ('data/day23a.txt', False, 16506),
        ('data/day23b.txt', True, 44169),
        ('data/day23c.txt', True, 48304),
    ])
    def test_part1(self, filename, part2, expected):
        f = open(filename)
        self.assertEqual(day23.part1(f.read().splitlines(), part2), expected)

    @parameterized.expand([
        ('data/day23.txt', (9, 2), [(9, 1)]),
        ('data/day23.txt', (9, 1), [(8, 1), (10, 1), (9, 2)]),
    ])
    def test_get_adjecent(self, filename, coord, expected):
        f = open(filename)
        burrow = day23.parse(f.read().splitlines())
        burrow[(9, 2)] = '.'
        self.assertEqual(day23.get_adjacent(burrow, coord), expected)

    @parameterized.expand([
        ('data/day23.txt', 8),
    ])
    def test_get_amphipods(self, filename, expected):
        f = open(filename)
        burrow = day23.parse(f.read().splitlines())
        self.assertEqual(len(day23.get_amphipods(burrow)), expected)

    @parameterized.expand([
        ('data/day23_room_a.txt', (4, 1), (5, 3), False, True),
        ('data/day23_room_b.txt', (4, 1), (5, 2), False, False),
        ('data/day23_room_c.txt', (9, 3), (9, 3), False, False),
    ])
    def test_room_is_free(self, filename, amphipod: Tuple[int, int],
                          move: Tuple[int, int], part2, expected):
        f = open(filename)
        burrow = day23.parse(f.read().splitlines())
        room: List[Tuple[int, int]] = day23.get_room_for_amphipod(
            burrow[amphipod], part2)
        self.assertEqual(day23.is_correct_room(burrow, room, amphipod, move),
                          expected)

    @parameterized.expand([
        ('data/day23_done_b.txt', True, True),
    ])
    def test_done(self, filename, part2, expected):
        f = open(filename)
        burrow = day23.parse(f.read().splitlines())
        self.assertEqual(day23.done(burrow, part2), expected)


if __name__ == '__main__':
    unittest.main()
