from copy import deepcopy

from util.file import readfile
from util.grid import good_square, cardinal_directions
from util.tuple import tuple_add


def solve_part1(lines: list[str]) -> int:
    lab, guard, direction_index = parse_lab_map(lines)

    positions = determine_path(lab, guard, direction_index)

    return len(positions)


def solve_part2(lines: list[str]) -> int:
    initial_lab, initial_guard, initial_direction_index = parse_lab_map(lines)

    positions = determine_path(initial_lab, initial_guard, initial_direction_index)

    obstacle_count = 0
    for position in positions:
            guard = initial_guard[:]
            direction_index = initial_direction_index
            lab = deepcopy(initial_lab)
            lab[position[0]][position[1]] = '#'
            if has_loop(lab, guard, direction_index):
                obstacle_count += 1

    return obstacle_count


def parse_lab_map(lines: list[str]) -> (list[list[str]], tuple[int, int], int):
    lab = [[c for c in line] for line in lines]

    guard = (0, 0)
    direction_index = 0

    for y in range(len(lab)):
        for x in range(len(lab[0])):
            if lab[y][x] == '^':
                guard = (y, x)
                lab[y][x] = '.'

    return lab, guard, direction_index


def determine_path(lab: list[list[str]], guard: tuple[int, int], direction_index: int) -> dict[tuple[int, int], bool]:
    positions = {guard: True}

    while True:
        new_location = tuple_add(guard, cardinal_directions[direction_index])
        if not good_square(lab, *new_location):
            break
        if lab[new_location[0]][new_location[1]] == '.':
            positions[new_location] = True
            guard = new_location
        else:
            direction_index = turn(direction_index)

    return positions


def has_loop(lab: list[list[str]], guard: tuple[int, int], direction_index: int) -> bool:
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
            direction_index = turn(direction_index)

    return loop


def turn(direction_index):
    direction_index += 1
    if direction_index >= len(cardinal_directions):
        direction_index = 0

    return direction_index


if __name__ == '__main__':
    input_lines = readfile("day06/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
