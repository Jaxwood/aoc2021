from typing import List, Tuple


def part1(input: List[str]) -> int:
    """find the number of unqiue paths in the maze"""
    # parse the input
    connections: List[Tuple[str, str]] = []
    for line in input:
        f, t = line.split("-")
        connections.append((f, t))

    # find all the possible paths
    queue = list(filter(lambda kv: kv[0] == "start", connections))

    while len(queue) > 0:
        f, t = queue.pop(0)

    # return the number of unique paths
    return len(input)