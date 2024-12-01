from collections import Counter

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    left, right = parse_lines(lines)
    left.sort()
    right.sort()

    for l, r in zip(left, right):
        total += abs(l - r)

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    left, right = parse_lines(lines)
    entry_count = count_entries(right)

    for l in left:
        total += (l * entry_count.get(l, 0))

    return total


def parse_lines(lines: list[str]) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []
    for line in lines:
        l, r = map(int, line.split())
        left.append(l)
        right.append(r)

    return left, right


def count_entries(numbers: list[int]) -> Counter[int]:
    result: Counter[int] = Counter()
    for i in numbers:
        result[i] += 1

    return result


if __name__ == '__main__':
    input_lines = readfile("day01/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
