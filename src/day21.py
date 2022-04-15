import functools
import itertools
from typing import Tuple


class Die:
    def __init__(self):
        self.face = 1
        self.rolls = 0

    def roll(self) -> int:
        self.rolls += 1
        die = self.face
        self.face = 1 if self.face == 100 else self.face + 1
        return die


class Player:
    def __init__(self, position: int, points: int = 0):
        self.position = position
        self.points = points

    def move(self, die: int) -> None:
        self.position = 10 if (self.position +
                               die) % 10 == 0 else (self.position + die) % 10

        if self.position > 10 or self.position <= 0:
            raise Exception("Player is out of bounds")

    def score(self):
        self.points += self.position


def part1(player1_position: int, player2_position: int) -> int:
    """play a game of Dirac dice"""
    player1 = Player(player1_position)
    player2 = Player(player2_position)
    die = Die()
    while player1.points < 1000 and player2.points < 1000:
        for _ in range(3):
            player1.move(die.roll())
        player1.score()

        if player1.points >= 1000:
            break

        for _ in range(3):
            player2.move(die.roll())
        player2.score()

    return player2.points * die.rolls if player1.points >= 1000 else player1.points * die.rolls


die_combinations = [
    (1, 1, 1),
    (1, 1, 2),
    (1, 1, 3),
    (1, 2, 1),
    (1, 2, 2),
    (1, 2, 3),
    (1, 3, 1),
    (1, 3, 2),
    (1, 3, 3),
    (2, 1, 1),
    (2, 1, 2),
    (2, 1, 3),
    (2, 2, 1),
    (2, 2, 2),
    (2, 2, 3),
    (2, 3, 1),
    (2, 3, 2),
    (2, 3, 3),
    (3, 1, 1),
    (3, 1, 2),
    (3, 1, 3),
    (3, 2, 1),
    (3, 2, 2),
    (3, 2, 3),
    (3, 3, 1),
    (3, 3, 2),
    (3, 3, 3),
]


@functools.lru_cache(maxsize=None)
def part2(position1: int, score1: int, position2: int,
          score2: int) -> Tuple[int, int]:
    """play a game of Dirac dice"""
    win1 = win2 = 0
    for die in die_combinations:
        total = (position1 + sum(die)) % 10
        p1_copy = 10 if total == 0 else total
        s1_copy = score1 + p1_copy
        if s1_copy >= 21:
            win1 += 1
        else:
            w2_copy, w1_copy = part2(position2, score2, p1_copy, s1_copy)
            win1 += w1_copy
            win2 += w2_copy
    return win1, win2
