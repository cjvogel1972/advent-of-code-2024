import math
import re

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    button_regex = re.compile("X\+(\d+), Y\+(\d+)")
    prize_regex = re.compile("X=(\d+), Y=(\d+)")
    for i in range(0, len(lines), 4):
        a_moves = tuple(int(x) for x in button_regex.search(lines[i]).groups())
        b_moves = tuple(int(x) for x in button_regex.search(lines[i + 1]).groups())
        prize = tuple(int(x) for x in prize_regex.search(lines[i + 2]).groups())

        b_solve = ((prize[0] * a_moves[1]) - (prize[1] * a_moves[0])) / (
                (b_moves[0] * a_moves[1]) - (a_moves[0] * b_moves[1]))
        a_solve = (prize[0] - (b_solve * b_moves[0])) / a_moves[0]

        if b_solve == math.floor(b_solve) and a_solve == math.floor(a_solve):
            total += compute_cost(int(a_solve), int(b_solve))

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    button_regex = re.compile("X\+(\d+), Y\+(\d+)")
    prize_regex = re.compile("X=(\d+), Y=(\d+)")
    for i in range(0, len(lines), 4):
        a_moves = tuple(int(x) for x in button_regex.search(lines[i]).groups())
        b_moves = tuple(int(x) for x in button_regex.search(lines[i + 1]).groups())
        prize = tuple(int(x) + 10000000000000 for x in prize_regex.search(lines[i + 2]).groups())

        b_solve = ((prize[0] * a_moves[1]) - (prize[1] * a_moves[0])) / (
                (b_moves[0] * a_moves[1]) - (a_moves[0] * b_moves[1]))
        a_solve = (prize[0] - (b_solve * b_moves[0])) / a_moves[0]

        if b_solve == math.floor(b_solve) and a_solve == math.floor(a_solve):
            total += compute_cost(int(a_solve), int(b_solve))

    return total


def compute_cost(a: int, b: int) -> int:
    return (a * 3) + b


if __name__ == '__main__':
    input_lines = readfile("day13/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
