import copy
from dataclasses import dataclass, field
from typing import Set, Dict, List, Tuple
from queue import PriorityQueue

hallway = [(1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1)]


def amber_room(part2: bool):
    return [(3, 2), (3, 3), (3, 4), (3, 5)] if part2 else [(3, 2), (3, 3)]


def bronze_room(part2: bool):
    return [(5, 2), (5, 3), (5, 4), (5, 5)] if part2 else [(5, 2), (5, 3)]


def copper_room(part2: bool):
    return [(7, 2), (7, 3), (7, 4), (7, 5)] if part2 else [(7, 2), (7, 3)]


def desert_room(part2: bool):
    return [(9, 2), (9, 3), (9, 4), (9, 5)] if part2 else [(9, 2), (9, 3)]


def rooms(part2: bool):
    return amber_room(part2) + bronze_room(part2) + copper_room(
        part2) + desert_room(part2)


cost_lookup = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}


def get_adjacent(burrow: Dict[Tuple[int, int], str],
                 coord: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Get the adjacent cells to the given coord"""
    adjacent: List[Tuple[int, int]] = []
    x, y = coord
    for (xx, yy) in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if (xx, yy) in burrow and burrow[(xx, yy)] == '.':
            adjacent.append((xx, yy))
    return adjacent


def get_amphipods(burrow: Dict[Tuple[int, int], str]) -> List[Tuple[int, int]]:
    """Get the location of the amphipods in the burrow"""
    amphipods: List[Tuple[int, int]] = []
    for cell in burrow:
        if burrow[cell] in {'A', 'B', 'C', 'D'}:
            amphipods.append(cell)
    return sorted(amphipods)


def possible_moves(burrow: Dict[Tuple[int, int], str], coord: Tuple[int, int],
                   part2: bool) -> List[Tuple[Tuple[int, int], int]]:
    """Get all the possible moves from the given coord.
    It doesn't check if the move is valid.
    Returns a list of tuples of the form (coord, cost)"""
    queue = [(coord, 0)]
    amphipod = burrow[coord]
    result: List[Tuple[Tuple[int, int], int]] = []
    visited: Set[Tuple[int, int]] = set()
    while len(queue) > 0:
        coord, total = queue.pop(0)
        for adjecent in get_adjacent(burrow, coord):
            cell = (adjecent, total + cost_lookup[amphipod])
            if adjecent in visited:
                continue
            if adjecent in hallway or adjecent in rooms(part2):
                result.append(cell)
            visited.add(adjecent)
            queue.append(cell)
    return result


def get_room_for_amphipod(amphipod: str, part2: bool) -> List[Tuple[int, int]]:
    """Get the room for the given amphipod"""
    if amphipod == 'A':
        return amber_room(part2)
    if amphipod == 'B':
        return bronze_room(part2)
    if amphipod == 'C':
        return copper_room(part2)
    if amphipod == 'D':
        return desert_room(part2)
    raise Exception("Unknown amphipod: {}".format(amphipod))


def is_correct_room(burrow: Dict[Tuple[int, int], str], room: List[Tuple[int,
                                                                         int]],
                    amphipod: str, move: Tuple[int, int]) -> bool:
    """Is the room free?"""
    return all(map(lambda x: burrow[x] in {'.', amphipod},
                   room)) and move in room


def parse(lines: List[str]) -> Dict[Tuple[int, int], str]:
    """Parse the input"""
    burrow: Dict[Tuple[int, int], str] = dict()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            cell = lines[y][x]
            if cell != ' ' and cell != '#':
                burrow[(x, y)] = cell
    return burrow


def done(burrow: Dict[Tuple[int, int], str], part2: bool) -> bool:
    amber_room_done = all(map(lambda x: burrow[x] == 'A', amber_room(part2)))
    bronze_room_done = all(map(lambda x: burrow[x] == 'B', bronze_room(part2)))
    copper_room_done = all(map(lambda x: burrow[x] == 'C', copper_room(part2)))
    desert_room_done = all(map(lambda x: burrow[x] == 'D', desert_room(part2)))
    return all([
        amber_room_done, bronze_room_done, copper_room_done, desert_room_done
    ])


def draw(burrow: Dict[Tuple[int, int], str]) -> None:
    """print the burrow"""
    print()
    for y in range(5):
        for x in range(13):
            if (x, y) in burrow:
                print(burrow[(x, y)], end='')
            else:
                print('#', end='')
        print()


def key(burrow: Dict[Tuple[int, int], str]) -> str:
    """key for the burrow"""
    return ''.join(
        [value for _, value in sorted(burrow.items(), reverse=True)])


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Dict[Tuple[int, int], str] = field(compare=False)


def part1(lines: List[str], part2: bool) -> int:
    q = PriorityQueue()
    q.put(PrioritizedItem(0, parse(lines)))
    visited: Set[str] = set()
    while not q.empty():
        next = q.get()
        cost = next.priority
        burrow: Dict[Tuple[int, int], str] = next.item
        lookup_key = key(burrow)
        if lookup_key in visited:
            continue
        else:
            visited.add(lookup_key)
        #draw(burrow)
        amphipods = get_amphipods(burrow)
        for amphipod in amphipods:
            amphipod_room = get_room_for_amphipod(burrow[amphipod], part2)
            if is_correct_room(burrow, amphipod_room, burrow[amphipod],
                               amphipod):
                continue
            moves = possible_moves(burrow, amphipod, part2)
            if len(moves) == 0:
                continue
            # hallway to room
            if amphipod in hallway:
                for (move, total) in moves:
                    if move in amphipod_room and is_correct_room(
                            burrow, amphipod_room, burrow[amphipod], move):
                        new_burrow = copy.deepcopy(burrow)
                        new_burrow[move] = new_burrow[amphipod]
                        new_burrow[amphipod] = '.'
                        if done(new_burrow, part2):
                            return cost + total
                        q.put(PrioritizedItem(cost + total, new_burrow))
            # room to hallway or room
            if amphipod in rooms(part2):
                for (move, total) in moves:
                    new_burrow = copy.deepcopy(burrow)
                    # move from room to room
                    if move in amphipod_room and is_correct_room(
                            burrow, amphipod_room, burrow[amphipod], move):
                        new_burrow[move] = new_burrow[amphipod]
                        new_burrow[amphipod] = '.'
                        q.put(PrioritizedItem(cost + total, new_burrow))
                    # move from room to hallway
                    elif move in hallway:
                        new_burrow[move] = new_burrow[amphipod]
                        new_burrow[amphipod] = '.'
                        q.put(PrioritizedItem(cost + total, new_burrow))
                    if done(new_burrow, part2):
                        return cost + total
    return 0
