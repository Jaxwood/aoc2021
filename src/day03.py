from typing import Counter, List, Tuple
import numpy as np

def to_int(strs: List[str]) -> List[int]:
    """convert list of str to int"""
    return list(map(int, strs))

def count_one_zero(bits: List[int]) -> Tuple[int, int]:
    """counts the numbers of 0 and 1 in the list"""
    zero = 0
    one = 0
    for bit in bits:
        if bit == 1:
            one += 1
        else:
            zero += 1
    return (zero, one)

def transpose(nums: List[List[int]]) -> List[List[int]]:
    return np.array(list(map(to_int, nums))).transpose()

def calculate_power_consumption(instructions: List[str]) -> int:
    """calculates the power consumption
    by multiply gamma and epsilon rates"""
    gamma = 0
    epsilon = 0
    candidates = list(map(to_int, instructions))
    diagnostics = transpose(candidates)
    factor = len(diagnostics) - 1
    for diag in diagnostics:
        (zero, one) = count_one_zero(diag)
        if one > zero:
            epsilon += pow(2, factor)
        else:
            gamma += pow(2, factor)
        factor -= 1
    return epsilon * gamma

def calculate_life_support_rating(instructions: List[str]) -> int:
    """calculates the life support rating
    by multiply oxygen generator and CO2 scrubber rating"""
    diagnostics = np.array(list(map(to_int, instructions))).transpose()

    oxygen = list(map(to_int, instructions))
    for idx in range(0, len(diagnostics)):
        (zero, one) = count_one_zero(diagnostics[idx])
        if zero == one or one > zero:
            oxygen = list(filter(lambda i: i[idx] == 1, oxygen))
        else:
            oxygen = list(filter(lambda i: i[idx] == 0, oxygen))
        if len(oxygen) == 1:
            break
        diagnostics = transpose(oxygen)

    diagnostics = np.array(list(map(to_int, instructions))).transpose()

    co2 = list(map(to_int, instructions))
    for idx in range(0, len(diagnostics)):
        (zero, one) = count_one_zero(diagnostics[idx])
        if zero == one or one > zero:
            co2 = list(filter(lambda i: i[idx] == 0, co2))
        else:
            co2 = list(filter(lambda i: i[idx] == 1, co2))
        if len(co2) == 1:
            break
        diagnostics = transpose(co2)


    oxygen_total = 0
    co2_total = 0
    factor = len(oxygen[0]) - 1
    for x in range(0, len(oxygen[0])):
        if oxygen[0][x] == 1:
            oxygen_total += pow(2, factor)
        if co2[0][x] == 1:
            co2_total += pow(2, factor)
        factor -= 1

    return oxygen_total * co2_total
