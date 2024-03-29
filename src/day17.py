from typing import List, Tuple


def within_target(coord: Tuple[int, int], xs: Tuple[int, int],
                  ys: Tuple[int, int]) -> bool:
    """check if coord is within target area"""
    x, y = coord
    x1, x2 = xs
    y1, y2 = ys
    return x1 <= x <= x2 and y1 <= y <= y2


def miss_target(coord: Tuple[int, int], xs: Tuple[int, int],
                ys: Tuple[int, int]) -> bool:
    """check if coord is past target area"""
    x1, x2 = xs
    y1, y2 = ys
    x, y = coord
    return min(y1, y2) > y or max(x1, x2) < x


def tick(coord: Tuple[int, int],
         velocity: Tuple[int, int]) -> List[Tuple[int, int]]:
    """move coord one step"""
    x, y = coord
    vx, vy = velocity
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    elif vx < 0:
        vx += 1
    vy -= 1
    return [(x, y), (vx, vy)]


def part1(xs: Tuple[int, int], ys: Tuple[int, int]) -> int:
    """find the highest velocity"""
    y_max = 0
    to_x = max(xs[0], xs[1])
    to_y = min(ys[0], ys[1])
    total = 0
    for x in range(0, to_x + 1):
        for y in range(to_y, abs(to_y - 1)):
            coord = (0, 0)
            velocity = (x, y)
            best = 0
            while not miss_target(coord, xs, ys):
                coord, velocity = tick(coord, velocity)
                best = max(best, coord[1])
                if within_target(coord, xs, ys):
                    y_max = max(y_max, best)
                    total += 1
                    break
    return (y_max, total)