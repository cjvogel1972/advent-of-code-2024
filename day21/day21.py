from functools import cache
from itertools import product

from util.file import readfile
from util.grid import manhattan_distance, cardinal_directions
from util.tuple import tuple_add


class HashableDict(dict):
    def __hash__(self):
        return hash(tuple(sorted(self.items())))


NUMERIC_KEYPAD_LOCS = HashableDict(
    {'7': (0, 0), '8': (0, 1), '9': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '1': (2, 0),
     '2': (2, 1), '3': (2, 2), '': (3, 0), '0': (3, 1), 'A': (3, 2)})
DIRECTION_KEYPAD_LOCS = HashableDict({'': (0, 0), '^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)})
DIR_CHARS = {(-1, 0): '^', (0, 1): '>', (1, 0): 'v', (0, -1): '<'}


def solve_part1(lines: list[str]) -> int:
    total = 0

    for code in lines:
        sequences = pad_sequences(NUMERIC_KEYPAD_LOCS, code)

        for _ in range(2):
            possible_next = []
            for seq in sequences:
                possible_next += pad_sequences(DIRECTION_KEYPAD_LOCS, seq)
            minlen = min(map(len, possible_next))
            sequences = [seq for seq in possible_next if len(seq) == minlen]

        total += (int(code[:3]) * len(sequences[0]))

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for code in lines:
        sequences = pad_sequences(NUMERIC_KEYPAD_LOCS, code)

        optimal = float("inf")
        for seq in sequences:
            length = 0
            for x, y in zip("A" + seq, seq):
                length += compute_length(x, y, 25)
            optimal = min(optimal, length)

        total += (int(code[:3]) * optimal)

    return total


def pad_sequences(keypad: HashableDict, buttons: str) -> list[str]:
    prev_loc = keypad['A']

    options = []
    for key in buttons:
        loc = keypad[key]
        new_seq = keypad_path(keypad, prev_loc, loc)

        options.append(new_seq)
        prev_loc = loc

    sequences = ["".join(x) for x in product(*options)]

    return sequences


@cache
def compute_length(start: str, dest: str, depth: int) -> int:
    start_loc = DIRECTION_KEYPAD_LOCS[start]
    dest_loc = DIRECTION_KEYPAD_LOCS[dest]
    if depth == 1:
        return len(keypad_path(DIRECTION_KEYPAD_LOCS, start_loc, dest_loc)[0])

    optimal = float("inf")
    for seq in keypad_path(DIRECTION_KEYPAD_LOCS, start_loc, dest_loc):
        length = 0
        for a, b in zip("A" + seq, seq):
            length += compute_length(a, b, depth - 1)
        optimal = min(optimal, length)

    return optimal


@cache
def keypad_path(keypad: HashableDict, start_loc: tuple[int, int], dest_loc: tuple[int, int]) -> list[str]:
    if start_loc == dest_loc:
        return ['A']

    sequences = []
    distance = manhattan_distance(start_loc, dest_loc)
    queue = [(start_loc, "", 0)]
    while queue:
        loc, seq, dist = queue.pop()
        if dist > distance:
            continue
        if loc == dest_loc:
            sequences.append(seq + "A")
            continue
        for direction in cardinal_directions:
            new_loc = tuple_add(loc, direction)
            if new_loc in keypad.values():
                if get_key(keypad, new_loc) == '':
                    continue
                queue.append((new_loc, seq + DIR_CHARS[direction], dist + 1))

    return sequences


@cache
def get_key(keypad: HashableDict, loc: tuple[int, int]) -> str:
    for key in keypad:
        if keypad[key] == loc:
            return key


if __name__ == '__main__':
    input_lines = readfile("day21/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
