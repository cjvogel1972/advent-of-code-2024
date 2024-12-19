import heapq

from util.file import readfile
from util.grid import cardinal_directions
from util.tuple import tuple_add


def solve_part1(lines: list[str]) -> int:
    start, end = parse_input(lines)

    scores = {(start, 1): 0}
    queue = [(0, start, 1)]
    end_states = set()
    while queue:
        score, loc, dir_index = heapq.heappop(queue)
        if score > scores.get((loc, dir_index), float("inf")):
            continue
        if loc == end:
            end_states.add((loc, dir_index))
        for index in left_right_straight(dir_index):
            cost, new_loc = compute_location_cost(lines, loc, dir_index, index)

            s = score + cost
            if s < scores.get((new_loc, index), float("inf")):
                heapq.heappush(queue, (s, new_loc, index))
                scores[(new_loc, index)] = s

    return min(scores[state] for state in end_states)


def solve_part2(lines: list[str]) -> int:
    start, end = parse_input(lines)

    scores = {(start, 1): 0}
    queue = [(0, start, 1)]
    predecessors = {}
    end_states = set()
    best_end_cost = float("inf")
    while queue:
        score, loc, dir_index = heapq.heappop(queue)
        if score > scores.get((loc, dir_index), float("inf")):
            continue
        if loc == end:
            if score > best_end_cost:
                continue
            best_end_cost = score
            end_states.add((loc, dir_index))
        for index in left_right_straight(dir_index):
            cost, new_loc = compute_location_cost(lines, loc, dir_index, index)

            s = score + cost
            lowest = scores.get((new_loc, index), float("inf"))
            if s > lowest:
                continue
            if s < lowest:
                predecessors[(new_loc, index)] = set()
                scores[(new_loc, index)] = s
            heapq.heappush(queue, (s, new_loc, index))
            predecessors[(new_loc, index)].add((loc, dir_index))

    path = set(end_states)
    queue = list(end_states)
    while queue:
        current = queue.pop()
        path.add(current)
        for p in predecessors.get(current, []):
            if p in path:
                continue
            path.add(p)
            queue.append(p)

    best_squares = {loc for loc, dir_index in path}
    return len(best_squares)


def compute_location_cost(lines, loc, orig_dir_index, index):
    new_loc = loc
    cost = 1000
    if index == orig_dir_index:
        nr, nc = tuple_add(loc, cardinal_directions[index])
        if lines[nr][nc] != "#":
            cost = 1
            new_loc = (nr, nc)
    return cost, new_loc


def parse_input(lines: list[str]) -> tuple[tuple[int, int], tuple[int, int]]:
    start = (0, 0)
    end = (0, 0)

    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "S":
                start = (r, c)
            elif lines[r][c] == "E":
                end = (r, c)

    return start, end


def left_right_straight(dir_index: int) -> tuple[int, int, int]:
    left = dir_index - 1
    if left < 0:
        left = 3
    right = dir_index + 1
    if right > len(cardinal_directions) - 1:
        right = 0
    return left, right, dir_index


if __name__ == '__main__':
    input_lines = readfile("day16/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
