from typing import Dict, List, Tuple
from enum import Enum


class Foldable(Enum):
    """Represent folding directions."""
    Horizontal = 0
    Vertical = 1


def parse(raw: List[str]) -> Tuple[Dict[int, int], List[Tuple[Foldable, int]]]:
    """parse the input into a list of coordinates and a list of folds."""
    dots = dict()
    coords = True
    folds = []
    for line in raw:
        if line == "":
            coords = False
            continue
        if coords:
            fst, snd = line.split(",")
            dots[(int(fst), int(snd))] = True
        else:
            fold_instruction = line.split(" ")
            t, c = fold_instruction[2].split("=")
            if t == "x":
                folds.append((Foldable.Vertical, int(c)))
            else:
                folds.append((Foldable.Horizontal, int(c)))

    return (dots, folds)


def fold_horizontal(coords: Dict[int, int], coord: int) -> None:
    """fold the horizontal line at coord."""
    max_x = max(map(lambda x: x[0], coords.keys())) + 1
    max_y = max(map(lambda x: x[1], coords.keys())) + 1
    for y in range(0, max_y):
        if y > coord:
            for x in range(0, max_x):
                if (x, y) in coords:
                    del coords[(x, y)]
                    coords[(x, coord - (y - coord))] = True


def fold_vertical(coords: Dict[int, int], coord: int) -> None:
    """fold the vertical line at coord."""
    max_x = max(map(lambda x: x[0], coords.keys())) + 1
    max_y = max(map(lambda x: x[1], coords.keys())) + 1
    for y in range(0, max_y):
        for x in range(0, max_x):
            if x > coord:
                if (x, y) in coords:
                    del coords[(x, y)]
                    coords[coord - (x - coord), y] = True


def draw(coords: Dict[int, int]):
    """draw the dots."""
    max_x = max(map(lambda x: x[0], coords.keys()))
    max_y = max(map(lambda x: x[1], coords.keys()))
    print("\n")
    for y in range(0, max_y + 1):
        line = ""
        for x in range(0, max_x + 1):
            if (x, y) in coords:
                line += "#"
            else:
                line += "."
        print(line)


def part1(raw: List[str], one_fold_only: bool) -> int:
    """find visible dots after folding."""
    coords, folds = parse(raw)
    # do only one fold
    folds = [folds[0]] if one_fold_only else folds
    for fold in folds:
        type, coord = fold
        if type == Foldable.Horizontal:
            fold_horizontal(coords, coord)
        else:
            fold_vertical(coords, coord)
    if one_fold_only == False:
        draw(coords)
    return sum(filter(lambda x: x, coords.values()))