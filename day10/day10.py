from util.file import readfile
from util.grid import cardinal_directions, good_square_tuple
from util.tuple import tuple_add


def solve_part1(lines: list[str]) -> int:
    total = 0

    topo_map = [[int(c) for c in line] for line in lines]

    for r in range(len(topo_map)):
        for c in range(len(topo_map[0])):
            if topo_map[r][c] == 0:
                visited = set()
                total += follow_path(topo_map, visited, (r, c))

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    topo_map = [[int(c) for c in line] for line in lines]

    for r in range(len(topo_map)):
        for c in range(len(topo_map[0])):
            if topo_map[r][c] == 0:
                total += find_rating(topo_map, (r, c))

    return total


def follow_path(topo_map: list[list[int]], visited: set[tuple[int, int]], location: tuple[int, int]) -> int:
    visited.add(location)
    if topo_map[location[0]][location[1]] == 9:
        return 1
    reached_end = 0

    for direction in cardinal_directions:
        new_location = tuple_add(location, direction)
        if good_square_tuple(topo_map, new_location) and topo_map[location[0]][location[1]] + 1 == \
                topo_map[new_location[0]][new_location[1]] and new_location not in visited:
            reached_end += follow_path(topo_map, visited, new_location)

    return reached_end


def find_rating(topo_map: list[list[int]], location: tuple[int, int]) -> int:
    if topo_map[location[0]][location[1]] == 9:
        return 1
    reached_end = 0

    for direction in cardinal_directions:
        new_location = tuple_add(location, direction)
        if good_square_tuple(topo_map, new_location) and topo_map[location[0]][location[1]] + 1 == \
                topo_map[new_location[0]][new_location[1]]:
            reached_end += find_rating(topo_map, new_location)

    return reached_end


if __name__ == '__main__':
    input_lines = readfile("day10/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
