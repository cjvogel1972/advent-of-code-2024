from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    patterns = lines[0].split(", ")
    designs = lines[2:]

    total = 0

    for design in designs:
        if create_design(design, patterns) > 0:
            total += 1

    return total


def solve_part2(lines: list[str]) -> int:
    patterns = lines[0].split(", ")
    designs = lines[2:]

    total = 0

    for design in designs:
        total += create_design(design, patterns)

    return total


def memoize(f):
    fast = {}

    def partner(design: str, patterns: list[str]):
        if design not in fast:
            fast[design] = f(design, patterns)
        return fast[design]

    return partner


@memoize
def create_design(design: str, patterns: list[str]) -> int:
    if design == "":
        return 1
    count = 0
    for pattern in patterns:
        if pattern == design[:len(pattern)]:
            count += create_design(design[len(pattern):], patterns)

    return count


if __name__ == '__main__':
    input_lines = readfile("day19/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
