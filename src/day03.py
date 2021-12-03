from typing import List
import numpy as np

def calculate_power_consumption(instructions: List[str]) -> int:
    """calculates the power consumption
    by multiply gamma and epsilon rates"""
    gamma = 0
    epsilon = 0
    to_int = lambda xs : list(map(int, xs))
    diagnostics = np.array(list(map(to_int, instructions))).transpose()
    factor = len(diagnostics) - 1
    for diag in diagnostics:
        one = 0
        zero = 0
        for bit in diag:
            if bit == 1:
                one += 1
            else:
                zero += 1
        if one > zero:
            epsilon += pow(2, factor)
        else:
            gamma += pow(2, factor)
        factor -= 1
    return epsilon * gamma
