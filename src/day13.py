from typing import List, Tuple
from enum import Enum


class Foldable(Enum):
    """Represent folding directions."""
    Horizontal = 0
    Vertical = 1


def parse(
    raw: List[str]
) -> Tuple[List[Tuple[int, int]], List[Tuple[Foldable, int]]]:
    """parse the input into a list of coordinates and a list of folds."""
    dots = []
    coords = True
    folds = []
    for line in raw:
        if line == "":
            coords = False
            continue
        if coords:
            fst, snd = line.split(",")
            dots.append((int(fst), int(snd)))
        else:
            fold_instruction = line.split(" ")
            t, c = fold_instruction[2].split("=")
            if t == "x":
                folds.append((Foldable.Vertical, int(c)))
            else:
                folds.append((Foldable.Horizontal, int(c)))

    return (dots, folds)


def part1(raw: List[str]) -> int:
    """find visible dots after folding."""
    coords, folds = parse(raw)
    return 0