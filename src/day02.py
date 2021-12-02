from typing import List

def calculate_depth(instructions: List[str]) -> int:
    """calculates the depth"""
    depth = 0
    pos = 0
    for inst in instructions:
        n = int(inst.split()[1])
        if inst.startswith("forward"):
            pos += n
        if inst.startswith("down"):
            depth += n
        if inst.startswith("up"):
            depth -= n

    return depth * pos