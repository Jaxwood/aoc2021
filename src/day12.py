from typing import List, Tuple, Dict, Set


def part1(input: List[str]) -> int:
    """find the number of unqiue paths in the maze"""
    # parse the input
    connections: Dict[str, Set[str]] = {}
    for line in input:
        f, t = line.split("-")
        if f in connections:
            connections[f].add(t)
        else:
            connections[f] = {t}
        if t in connections:
            connections[t].add(f)
        else:
            connections[t] = {f}

    # find all the possible paths
    queue = [('start', [])]
    paths = []
    while len(queue) > 0:
        current, breadcrumb = queue.pop(0)
        if current == 'end':
            paths.append(breadcrumb + [current])
        else:
            for c in connections[current]:
                if c.islower() and c not in breadcrumb:
                    queue.append((c, breadcrumb + [current]))
                if c.isupper():
                    queue.append((c, breadcrumb + [current]))

    # return the number of unique paths
    return len(paths)