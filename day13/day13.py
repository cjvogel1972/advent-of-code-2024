import math
import re

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    for i in range(0, len(lines), 4):
        ax, ay, bx, by, px, py = parse_machine_behavior(lines[i:i + 4])

        total += cost_per_machine(ax, ay, bx, by, px, py)

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for i in range(0, len(lines), 4):
        ax, ay, bx, by, px, py = parse_machine_behavior(lines[i:i + 4])
        px += 10000000000000
        py += 10000000000000

        total += cost_per_machine(ax, ay, bx, by, px, py)

    return total

def cost_per_machine(ax, ay, bx, by, px, py:int) -> int:
    b_solve = ((px * ay) - (py * ax)) / ((bx * ay) - (ax * by))
    a_solve = (px - (b_solve * bx)) / ax

    if b_solve == math.floor(b_solve) and a_solve == math.floor(a_solve):
        return compute_cost(int(a_solve), int(b_solve))

    return 0


def parse_machine_behavior(lines: list[str]) -> tuple[int, int, int, int, int, int]:
    button_regex = re.compile("X\+(\d+), Y\+(\d+)")
    prize_regex = re.compile("X=(\d+), Y=(\d+)")

    ax, ay = tuple(int(x) for x in button_regex.search(lines[0]).groups())
    bx, by = tuple(int(x) for x in button_regex.search(lines[1]).groups())
    px, py = tuple(int(x) for x in prize_regex.search(lines[2]).groups())

    return ax, ay, bx, by, px, py


def compute_cost(a: int, b: int) -> int:
    return (a * 3) + b


if __name__ == '__main__':
    input_lines = readfile("day13/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
