
from typing import List, Tuple
import re
import functools

def parse(raw: List[str]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """parse the input into a list of coords"""
    for line in raw:
        line = line.strip()
        x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))
        yield (x1, y1), (x2, y2)

def sort_two_coords(coords: Tuple[Tuple[int, int], Tuple[int, int]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """sort two coords by x and y"""
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    if x1 < x2:
        return coords
    elif x1 > x2:
        return (x2, y2), (x1, y1)
    elif y1 <= y2:
        return coords
    else:
        return (x2, y2), (x1, y1)

def get_all_coords_between_two_coords(coords1: Tuple[int, int], coords2: Tuple[int, int]) -> List[Tuple[int, int]]:
    """find all coords between two coords"""
    x1, y1 = coords1
    x2, y2 = coords2
    # only consider horizontal or vertical lines
    if x1 != x2 and y1 != y2:
        return []
    else:
        return [(x, y) for x in range(x1, x2+1) for y in range(y1, y2+1)]

def overlap(raw: List[str]) -> int:
    """find all coords where atleast two lines overlap"""
    coords = parse(raw)
    lines: List[set[Tuple[int, int]]] = []

    # get all the lines
    for coord in coords:
        c1, c2 = sort_two_coords(coord)
        lines.append(set(get_all_coords_between_two_coords(c1, c2)))

    # find the intersections
    intersections = set()
    for idx in range(1, len(lines)):
        for idx2 in range(idx):
            if lines[idx] & lines[idx2]:
                intersections.update(lines[idx] & lines[idx2])

    return len(intersections)