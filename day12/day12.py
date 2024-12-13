import queue

from util.file import readfile
from util.grid import cardinal_directions, good_square_tuple
from util.tuple import tuple_add


def solve_part1(lines: list[str]) -> int:
    garden = [[c for c in line] for line in lines]

    total = 0
    visited = set()
    for r in range(len(garden)):
        for c in range(len(garden[0])):
            if (r, c) not in visited:
                a, p, _ = parse_region(garden, visited, (r, c))
                total += a * p

    return total


def solve_part2(lines: list[str]) -> int:
    garden = [[c for c in line] for line in lines]

    total = 0
    visited = set()
    for r in range(len(garden)):
        for c in range(len(garden[0])):
            if (r, c) not in visited:
                a, _, s = parse_region(garden, visited, (r, c))
                total += a * s

    return total


def parse_region(garden: list[list[str]], visited: set[tuple[int, int]], location: tuple[int, int]) -> tuple[
    int, int, int]:
    q = queue.Queue()
    q.put(location)
    visited.add(location)
    perimeter = 0
    area = 0
    corners = 0

    while not q.empty():
        loc = q.get()
        area += 1
        sides = 4
        for direction in cardinal_directions:
            new_loc = tuple_add(loc, direction)
            if good_square_tuple(garden, new_loc) and garden[loc[0]][loc[1]] == garden[new_loc[0]][new_loc[1]]:
                sides -= 1
                if new_loc not in visited:
                    q.put(new_loc)
                    visited.add(new_loc)
        perimeter += sides
        corners += compute_corners(garden, loc, sides)

    return area, perimeter, corners


def compute_corners(garden: list[list[str]], location: tuple[int, int], sides: int) -> int:
    corners = 0
    if sides == 4:
        return 4
    if sides == 3:
        corners += 2
    if sides == 2:
        loc_plant = garden[location[0]][location[1]]
        for i in [(0, 1), (1, 2), (2, 3), (3, 0)]:
            loc1 = tuple_add(location, cardinal_directions[i[0]])
            loc2 = tuple_add(location, cardinal_directions[i[1]])
            loc1_in_grid = good_square_tuple(garden, loc1)
            loc2_in_grid = good_square_tuple(garden, loc2)
            if not loc1_in_grid and not loc2_in_grid:
                corners += 1
            elif not loc1_in_grid and loc2_in_grid and loc_plant != garden[loc2[0]][loc2[1]]:
                corners += 1
            elif loc1_in_grid and loc_plant != garden[loc1[0]][loc1[1]] and not loc2_in_grid:
                corners += 1
            elif loc1_in_grid and loc_plant != garden[loc1[0]][loc1[1]] and loc2_in_grid and loc_plant != \
                    garden[loc2[0]][loc2[1]]:
                corners += 1

    loc_plant = garden[location[0]][location[1]]
    for i in [(0, 1), (1, 2), (2, 3), (3, 0)]:
        loc1 = tuple_add(location, cardinal_directions[i[0]])
        loc2 = tuple_add(location, cardinal_directions[i[1]])
        inner_loc = tuple_add(loc1, cardinal_directions[i[1]])
        loc1_in_grid = good_square_tuple(garden, loc1)
        loc2_in_grid = good_square_tuple(garden, loc2)
        inner_loc_in_grid = good_square_tuple(garden, inner_loc)
        if not loc1_in_grid or not loc2_in_grid or not inner_loc_in_grid:
            continue
        loc1_plant = garden[loc1[0]][loc1[1]]
        loc2_plant = garden[loc2[0]][loc2[1]]
        inner_loc_plant = garden[inner_loc[0]][inner_loc[1]]
        if loc_plant == loc1_plant and loc_plant == loc2_plant and loc_plant != inner_loc_plant:
            corners += 1

    return corners


if __name__ == '__main__':
    input_lines = readfile("day12/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
