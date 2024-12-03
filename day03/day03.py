import re

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        matches = re.findall("mul\((\d+),(\d+)\)", line)
        for l,r in matches:
            total += int(l) * int(r)

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0
    enabled = True

    for line in lines:
        matches = re.findall("(do|don't|mul)\(((\d+),(\d+))?\)", line)

        for match in matches:
            if match[0] == "do":
                enabled = True
                continue
            if match[0] == "don't":
                enabled = False
                continue
            if enabled:
                total += int(match[2]) * int(match[3])

    return total


if __name__ == '__main__':
    input_lines = readfile("day03/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
