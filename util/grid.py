from typing import Any

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

cardinal_directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def left_right_straight(dir_index: int) -> tuple[int, int, int]:
    left = dir_index - 1
    if left < 0:
        left = 3
    right = dir_index + 1
    if right > len(cardinal_directions) - 1:
        right = 0
    return left, right, dir_index


def find_start_end(track: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    start = (0, 0)
    end = (0, 0)

    for r in range(len(track)):
        for c in range(len(track[0])):
            if track[r][c] == "S":
                start = (r, c)
            elif track[r][c] == "E":
                end = (r, c)

    return start, end


def manhattan_distance(loc1: tuple[int, int], loc2: tuple[int, int]) -> int:
    """Compute the Manhattan distance between two coordinates"""
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


def good_square(grid: list[list[Any]], r: int, c: int) -> bool:
    return 0 <= r < len(grid) and 0 <= c < len(grid[r])


def good_square_tuple(grid: list[list[Any]], pos: tuple[int, int]) -> bool:
    return good_square(grid, pos[0], pos[1])


def print_grid(grid: list[list[Any]]):
    print("\n".join("".join(str(row)) for row in grid))
