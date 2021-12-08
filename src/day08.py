from typing import List

def part1(lines: List[str]) -> int:
    """find the amount of times digit 1, 4, 7 and 8 appear in the output"""
    counter = 0
    for line in lines:
        [digits_line, output_line] = line.split('|')
        digits = digits_line.strip().split(' ')
        outputs = output_line.strip().split(' ')
        for digit in outputs:
            size = len(digit)
            # only check for digits 1, 4, 7 and 8
            if size == 2 or size == 4 or size == 3 or size == 7:
                counter += 1
    return counter

def part2(lines: List[str]) -> int:
    """find the sum of all digits in the output"""
    total = 0
    for line in lines:
        [digits_line, output_line] = line.split('|')
        digits = digits_line.strip().split(' ')
        outputs = output_line.strip().split(' ')

        found = set()

        # find 1, 4, 7 and 8
        for digit in digits:
            if len(digit) == 2:
                one = digit
                found.add(one)
            if len(digit) == 3:
                seven = digit
                found.add(seven)
            if len(digit) == 4:
                four = digit
                found.add(four)
            if len(digit) == 7:
                eight = digit
                found.add(eight)
        # nine
        for digit in digits:
            if len(digit) == 6:
                if len(set(digit).difference(set(seven + four))) == 1:
                    nine = digit
                    found.add(nine)
        # two
        for digit in digits:
            if len(digit) == 5:
                if len(set(digit).difference(set(nine))) == 1:
                    two = digit
                    found.add(two)
        # three
        for digit in digits:
            if len(digit) == 5:
                if len(set(one + two).difference(set(digit))) == 1 and digit not in found:
                    three = digit
                    found.add(three)
        # five
        for digit in digits:
            if len(digit) == 5:
                if digit not in found:
                    five = digit
                    found.add(five)
        # six
        for digit in digits:
            if len(digit) == 6:
                if digit not in found and len(set(one).difference(set(digit))) == 1:
                    six = digit
                    found.add(six)
        # zero
        for digit in digits:
            if digit not in found:
                zero = digit
                found.add(zero)
        
        number = 0
        multiplier = 1000
        for output in outputs:
            out = set(output)
            if set(out) == set(zero):
                number += multiplier * 0
            if set(out) == set(one):
                number += multiplier * 1
            if set(out) == set(two):
                number += multiplier * 2
            if set(out) == set(three):
                number += multiplier * 3
            if set(out) == set(four):
                number += multiplier * 4
            if set(out) == set(five):
                number += multiplier * 5
            if set(out) == set(six):
                number += multiplier * 6
            if set(out) == set(seven):
                number += multiplier * 7
            if set(out) == set(eight):
                number += multiplier * 8
            if set(out) == set(nine):
                number += multiplier * 9
            multiplier //= 10
        total += number

    return total