from typing import List

def part1(lines: List[str]) -> int:
    """find the sum of the lowest points"""
    integers = list(map(lambda xs: list(map(int, xs)), lines))
    cave = dict()
    # map into dictionary
    for x in range(0, len(integers[0])):
        for y in range(0, len(integers)):
            cave[(x,y)] = integers[y][x]

    # check for low points
    sum = 0
    for x in range(0, len(integers[0])):
        for y in range(0, len(integers)):
            # check for adjacent points
            point = cave[(x, y)]
            valid = True

            if x > 0 and cave[(x-1, y)] <= point:
                valid = False
            
            if x < len(integers[0]) - 1 and cave[(x+1,y)] <= point:
                valid = False
                
            if y > 0 and cave[(x, y-1)] <= point:
                valid = False
                
            if y < len(integers) - 1 and cave[(x,y+1)] <= point:
                valid = False

            if valid == True:
                sum += point + 1
    return sum