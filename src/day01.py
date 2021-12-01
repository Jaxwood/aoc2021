from typing import List


def increases(measurements: List[int]) -> int:
    """find all the measurements where it 
    increases from the previous measurement"""
    increments = 0
    prev = measurements[0]
    for k in range(1, len(measurements)):
        if measurements[k] > prev:
            increments += 1
        prev = measurements[k]

    return increments
