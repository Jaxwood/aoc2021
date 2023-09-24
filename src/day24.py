from typing import List, Tuple
import re

ALU: Tuple[int, int, int] = (0, 0, 0)


class Instruction:

    def execute(alu: ALU):
        pass

    def __repr__(self) -> str:
        if self.__class__.__name__ == 'Inp':
            return f'{self.__class__.__name__} {self.a}'
        return f'{self.__class__.__name__} {self.a} {self.b}'


class Inp(Instruction):

    def __init__(self, a) -> ALU:
        self.a = a

    def execute(alu: ALU) -> ALU:
        return alu


class Add(Instruction):

    def __init__(self, a, b) -> ALU:
        self.a = a
        self.b = b

    def execute(alu: ALU) -> ALU:
        return alu


class Mul(Instruction):

    def __init__(self, a, b) -> ALU:
        self.a = a
        self.b = b

    def execute(alu: ALU) -> ALU:
        return alu


class Div(Instruction):

    def __init__(self, a, b) -> ALU:
        self.a = a
        self.b = b

    def execute(alu: ALU) -> ALU:
        return alu


class Mod(Instruction):

    def __init__(self, a, b) -> ALU:
        self.a = a
        self.b = b

    def execute(alu: ALU) -> ALU:
        return alu


class Eql(Instruction):

    def __init__(self, a, b) -> ALU:
        self.a = a
        self.b = b

    def execute(alu: ALU) -> ALU:
        return alu


def parse(lines: List[str]) -> List[Instruction]:
    result = []
    for line in lines:
        if line.startswith("inp"):
            result.append(Inp(line.split(" ")[1]))
        else:
            [(opt, a, b)] = re.findall("(\w+) (\w) (-?\w+)", line)
            if opt == 'add':
                result.append(Add(a, b))
            if opt == 'mul':
                result.append(Mul(a, b))
            if opt == 'div':
                result.append(Div(a, b))
            if opt == 'mod':
                result.append(Mod(a, b))
            if opt == 'eql':
                result.append(Eql(a, b))
    return result


def part1(raw: List[str]) -> int:
    print(parse(raw))
    return 0