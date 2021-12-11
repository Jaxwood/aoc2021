from typing import Dict, List, Tuple


def tick(state: Dict[Tuple[int, int], int], max_x: int, max_y: int) -> int:
    """simulate one tick"""
    for k, v in state.items():
        state[k] = v + 1
    return flash(state, max_x, max_y)


def neighbors(k: Tuple[int, int]) -> List[Tuple[int, int]]:
    """return all neighbors of a cell"""
    x, y = k
    return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]


def flash(state: Dict[Tuple[int, int], int], max_x: int, max_y: int) -> int:
    """flashes lights"""
    flashed = set()
    queue = list(state.keys())
    total = 0
    while len(queue) > 0:
        k = queue.pop(0)
        v = state[k]
        if v > 9:
            total += 1
            state[k] = 0
            flashed.add(k)
            for n in neighbors(k):
                if n in state:
                    if n not in flashed:
                        state[n] += 1
                        queue.append(n)
    return total


def part1(input: List[str]) -> int:
    """find number of flashes"""
    state = dict()
    for x in range(0, len(input[0])):
        for y in range(0, len(input)):
            state[(x, y)] = int(input[y][x])

    total = 0
    for _ in range(0, 100):
        total += tick(state, len(input[0]), len(input))

    return total

def part2(input: List[str]) -> int:
    """find when all flashes"""
    state = dict()

    for x in range(0, len(input[0])):
        for y in range(0, len(input)):
            state[(x, y)] = int(input[y][x])

    ticks = 0
    total = 0
    while total != len(state):
        ticks += 1
        total = tick(state, len(input[0]), len(input))

    return ticks