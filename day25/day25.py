from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    keys = []
    locks = []
    for i in range(0, len(lines), 8):
        lock = True if lines[i][0] == "#" else False
        column_lengths = [0] * 5
        pattern = lines[i+1:i+6]
        loop = range(len(pattern)) if lock else range(len(pattern) - 1, -1, -1)
        for r in loop:
            for j, c in enumerate(pattern[r]):
                if c == "#":
                    column_lengths[j] += 1

        if lock:
            locks.append(tuple(column_lengths))
        else:
            keys.append(tuple(column_lengths))

    total = 0

    for k in keys:
        for l in locks:
            for i in range(len(k)):
                if k[i] + l[i] > 5:
                    break
            else:
                total += 1

    return total


if __name__ == '__main__':
    input_lines = readfile("day25/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
