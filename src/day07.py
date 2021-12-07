def part1(input: str) -> int:
    """find the best position to align on costing the least amout of moves"""
    nums = list(map(int, input.split(',')))
    positions = set(nums)

    best = None
    for pos in positions:
        moves = 0
        for num in nums:
            if pos != num:
                moves += abs(num - pos)
        if best is None or moves < best:
            best = moves
        
    return best

def part2(input: str) -> int:
    """find the best position to align on costing the least amout of moves"""
    nums = list(map(int, input.split(',')))
    min_pos = min(nums)
    max_pos = max(nums)

    best = None
    for pos in range(min_pos, max_pos + 1):
        moves = 0
        for num in nums:
            if pos != num:
                moves += sum(range(0, abs(num - pos) + 1))
        if best is None or moves < best:
            best = moves

    return best