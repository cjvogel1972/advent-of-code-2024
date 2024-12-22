import heapq
from collections import Counter

from util.file import readfile
from util.grid import cardinal_directions, find_start_end, left_right_straight, good_square_tuple, \
    manhattan_distance
from util.tuple import tuple_add


def solve_part1(lines: list[str], min_time_saved: int, start_dir: int) -> int:
    track = [[c for c in line] for line in lines]
    start, end = find_start_end(track)
    times = run_race(track, start, end, start_dir)
    best = times[end]
    visited = set()
    good_cheats = Counter()

    loc = start
    direction = start_dir
    while True:
        loc, direction, cheats = find_next_cheats(track, loc, direction, visited, 2)
        if loc == end:
            break
        for cheat in cheats:
            cheat_start, cheat_end = cheat
            cheat_distance = cheats[cheat]

            time = best - (times[cheat_end] - times[cheat_start] - cheat_distance)
            if best - time >= min_time_saved:
                good_cheats[time] += 1

    return good_cheats.total()


def solve_part2(lines: list[str], min_time_saved: int, start_dir: int) -> int:
    track = [[c for c in line] for line in lines]
    start, end = find_start_end(track)
    times = run_race(track, start, end, start_dir)
    best = times[end]
    visited = set()
    good_cheats = Counter()

    loc = start
    direction = start_dir
    while True:
        loc, direction, cheats = find_next_cheats(track, loc, direction, visited, 20)
        if loc == end:
            break
        for cheat in cheats:
            cheat_start, cheat_end = cheat
            cheat_distance = cheats[(cheat_start, cheat_end)]
            time = best - (times[cheat_end] - times[cheat_start] - cheat_distance)
            if best - time >= min_time_saved:
                good_cheats[time] += 1

    return good_cheats.total()


def run_race(track: list[list[str]], start: tuple[int, int], end: tuple[int, int], start_dir: int):
    times = {start: 0}
    queue = [(0, start, start_dir)]
    while queue:
        score, loc, dir_index = heapq.heappop(queue)
        if score > times.get(loc, float("inf")):
            continue
        if loc == end:
            return times
        for index in left_right_straight(dir_index):
            nr, nc = tuple_add(loc, cardinal_directions[index])
            if track[nr][nc] != "#":
                s = score + 1
                new_loc = (nr, nc)
                if s < times.get(new_loc, float("inf")):
                    heapq.heappush(queue, (s, new_loc, index))
                    times[new_loc] = s


def find_next_cheats(track: list[list[str]], loc: tuple[int, int], direction, visited: set[tuple[int, int]],
                     max_squares: int) -> tuple[    tuple[int, int], int, dict[tuple[tuple[int, int], tuple[int, int]], int]]:
    paths = {}

    for i in range(0, max_squares + 1):
        for j in range(0, max_squares + 1):
            for k in [(i, j), (-i, j), (i, -j), (-i, -j)]:
                new_loc = tuple_add(loc, k)
                nr, nc = new_loc
                dist = manhattan_distance(loc, new_loc)
                if dist < 2 or dist > max_squares:
                    continue
                if good_square_tuple(track, new_loc) and track[nr][nc] != "#" and new_loc not in visited:
                    paths[(loc, new_loc)] = dist

    nr, nc = tuple_add(loc, cardinal_directions[direction])
    if track[nr][nc] == "#":
        direction, loc = turn(track, loc, direction)
    else:
        loc = (nr, nc)

    return loc, direction, paths


def turn(track: list[list[str]], loc: tuple[int, int], direction: int):
    new_dirs = left_right_straight(direction)
    lr, lc = tuple_add(loc, cardinal_directions[new_dirs[0]])
    if track[lr][lc] != "#":
        loc = (lr, lc)
        direction = new_dirs[0]
    else:
        rr, rc = tuple_add(loc, cardinal_directions[new_dirs[1]])
        if track[rr][rc] != "#":
            loc = (rr, rc)
            direction = new_dirs[1]

    return direction, loc


if __name__ == '__main__':
    input_lines = readfile("day20/input.txt")

    print(f'Part 1: {solve_part1(input_lines, 100, 2)}')
    print(f'Part 2: {solve_part2(input_lines, 100, 2)}')
