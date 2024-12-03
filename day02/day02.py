from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    safe_count = 0

    for line in lines:
        levels = list(map(int, line.split()))
        if check_report(levels):
            safe_count += 1

    return safe_count


def solve_part2(lines: list[str]) -> int:
    safe_count = 0

    for line in lines:
        levels = list(map(int, line.split()))
        if check_report(levels):
            safe_count += 1
        else:
            for i in range(len(levels)):
                if check_report(levels[:i] + levels[i + 1:]):
                    safe_count += 1
                    break

    return safe_count


def check_report(levels: list[int]) -> bool:
    direction = compute_direction(levels[0], levels[1])
    if direction == 0:
        return False

    safe = True
    for i in range(len(levels) - 1):
        if compute_direction(levels[i], levels[i + 1]) != direction or not safe_interval(levels[i], levels[i + 1]):
            safe = False
            break

    return safe


def compute_direction(first: int, second: int) -> int:
    direction = 0
    diff = first - second
    if diff != 0:
        direction = diff / abs(diff)

    return direction


def safe_interval(first: int, second: int) -> bool:
    return 1 <= abs(first - second) <= 3


if __name__ == '__main__':
    input_lines = readfile("day02/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
