from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    safe_count = 0

    for line in lines:
        levels = list(map(int, line.split()))
        safe = check_report(levels)

        if safe:
            safe_count += 1

    return safe_count


def solve_part2(lines: list[str]) -> int:
    safe_count = 0

    for line in lines:
        levels = list(map(int, line.split()))

        safe = check_report(levels)
        if not safe:
            for i in range(len(levels)):
                safe = check_report(levels[:i] + levels[i+1:])
                if safe:
                    break

        if safe:
            safe_count += 1

    return safe_count


def check_report(levels: list[int]) -> bool:
    direction = 0
    safe = True
    for i in range(len(levels) - 1):
        if i == 0:
            direction = compute_direction(levels[i], levels[i + 1])
            if direction == 0:
                safe = False
                break

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
