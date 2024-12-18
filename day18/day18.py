import heapq

from util.file import readfile
from util.grid import cardinal_directions, good_square
from util.tuple import tuple_add


def solve_part1(lines: list[str], memory_size: int, num_bytes: int) -> int:
    grid, _ = parse_input(lines, memory_size, num_bytes)

    start = (0, 0)
    end = (memory_size, memory_size)

    return find_shortest_path(grid, start, end)


def solve_part2(lines: list[str], memory_size: int, num_bytes: int) -> str:
    grid, pushed_bytes = parse_input(lines, memory_size, num_bytes)

    start = (0, 0)
    end = (memory_size, memory_size)

    for i in range(num_bytes + 1, len(pushed_bytes)):
        x, y = pushed_bytes[i]
        grid[y][x] = "#"
        if find_shortest_path(grid, start, end) is None:
            break

    return ",".join(map(str, pushed_bytes[i]))


def parse_input(lines, memory_size, num_bytes) -> tuple[list[list[str]], list[tuple[int, int]]]:
    pushed_bytes = []
    for line in lines:
        x, y = line.split(",")
        pushed_bytes.append((int(x), int(y)))
    grid = [['.' for _ in range(memory_size + 1)] for _ in range(memory_size + 1)]
    for i in range(num_bytes):
        x, y = pushed_bytes[i]
        grid[y][x] = "#"

    return grid, pushed_bytes


def find_shortest_path(grid: list[list[str]], start: tuple[int, int], end: tuple[int, int]) -> int:
    queue = [(0, start)]
    visited = set()
    while queue:
        dist, loc = heapq.heappop(queue)
        if loc in visited:
            continue
        visited.add(loc)
        if loc == end:
            return dist
        for direction in cardinal_directions:
            nr, nc = tuple_add(loc, direction)
            if good_square(grid, nr, nc) and grid[nr][nc] != "#":
                if (nr, nc) not in visited:
                    heapq.heappush(queue, (dist + 1, (nr, nc)))


if __name__ == '__main__':
    input_lines = readfile("day18/input.txt")

    print(f'Part 1: {solve_part1(input_lines, 70, 1024)}')
    print(f'Part 2: {solve_part2(input_lines, 70, 1024)}')
