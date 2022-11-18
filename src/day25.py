from typing import Dict, List, Tuple

empty = '.'
east = '>'
south = 'v'


def parse(raw: List[str]) -> Dict[Tuple[int, int], str]:
    """parse the raw strings into a dictionary"""
    seafloor: Dict[Tuple[int, int], str] = dict()
    for line in range(len(raw)):
        for point in range(len(raw[line])):
            seafloor[(point, line)] = raw[line][point]
    return seafloor


def move_east(
        size: Tuple[int, int],
        seafloor: Dict[Tuple[int, int], str]) -> Dict[Tuple[int, int], str]:
    """move all seacucumber to the east"""
    w, h = size
    next = seafloor.copy()
    for y in range(h):
        for x in range(w):
            cucumber = seafloor[(x, y)]
            num = 0 if x + 1 == w else x + 1
            if cucumber == east and seafloor[(num, y)] == empty:
                next[(x, y)] = empty
                next[(num, y)] = cucumber
    return next


def move_south(
        size: Tuple[int, int],
        seafloor: Dict[Tuple[int, int], str]) -> Dict[Tuple[int, int], str]:
    """move all seacucumber to the south"""
    w, h = size
    next = seafloor.copy()
    for y in range(h):
        for x in range(w):
            cucumber = seafloor[(x, y)]
            num = 0 if y + 1 == h else y + 1
            if cucumber == south and seafloor[(x, num)] == empty:
                next[(x, y)] = empty
                next[(x, num)] = cucumber
    return next


def log(size: Tuple[int, int], seafloor: Dict[Tuple[int, int], str]) -> None:
    """print the seafloor"""
    w, h = size
    for y in range(h):
        str = ""
        for x in range(w):
            str += seafloor[(x, y)]
        print(str)


def part1(lines: List[str]) -> int:
    """find the number of moves before the seacucumber stabilizes"""
    seafloor = parse(lines)
    size = (len(lines[0]), len(lines))
    moves = 0
    while True:
        previous = seafloor.copy()
        moves += 1
        seafloor = move_south(size, move_east(size, seafloor))
        if seafloor == previous:
            break
    return moves
