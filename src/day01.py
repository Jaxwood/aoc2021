from typing import List
import numpy as np


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

def window_increases(measurements: List[int]) -> int:
    """find all the measurements where it 
    increases from the previous windo of measurements"""
    increments = 0
    windows = list(map(sum, np.lib.stride_tricks.sliding_window_view(measurements, 3)))
    prev = windows[0]
    for k in range(1, len(windows)):
        if windows[k] > prev:
            increments += 1
        prev = windows[k]

    return increments