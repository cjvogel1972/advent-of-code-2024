from copy import deepcopy

from util.file import readfile
from util.grid import good_square, cardinal_directions
from util.tuple import tuple_add


def solve_part1(lines: list[str]) -> int:
    lab = [[c for c in line] for line in lines]
    guard = (0, 0)
    direction_index = 0
    for y in range(len(lab)):
        for x in range(len(lab[0])):
            if lab[y][x] == '^':
                guard = (y, x)
                lab[y][x] = '.'

    positions = {guard: True}
    while True:
        new_location = tuple_add(guard, cardinal_directions[direction_index])
        if not good_square(lab, *new_location):
            break
        if lab[new_location[0]][new_location[1]] == '.':
            positions[new_location] = True
            guard = new_location
        else:
            direction_index += 1
            if direction_index >= len(cardinal_directions):
                direction_index = 0

    return len(positions)


def solve_part2(lines: list[str]) -> int:
    initial_lab = [[c for c in line] for line in lines]
    initial_guard = (0, 0)
    initial_direction_index = 0
    for y in range(len(initial_lab)):
        for x in range(len(initial_lab[0])):
            if initial_lab[y][x] == '^':
                initial_guard = (y, x)
                initial_lab[y][x] = '.'

    obstacle_count = 0
    for y in range(len(initial_lab)):
        for x in range(len(initial_lab[0])):
            guard = initial_guard[:]
            direction_index = initial_direction_index
            lab = deepcopy(initial_lab)
            if lab[y][x] == '.':
                lab[y][x] = '#'
                if has_loop(lab, guard, direction_index):
                    obstacle_count += 1

    return obstacle_count


def has_loop(lab, guard, direction_index) -> bool:
    loop = False
    positions = {(guard, direction_index): True}
    while True:
        new_location = tuple_add(guard, cardinal_directions[direction_index])
        if not good_square(lab, *new_location):
            break
        if lab[new_location[0]][new_location[1]] == '.':
            if positions.get((new_location, direction_index), False):
                loop = True
                break
            positions[(new_location, direction_index)] = True
            guard = new_location
        else:
            direction_index += 1
            if direction_index >= len(cardinal_directions):
                direction_index = 0
    return loop


if __name__ == '__main__':
    input_lines = readfile("day06/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
