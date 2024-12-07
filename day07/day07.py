from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    return solve(lines, 2)


def solve_part2(lines: list[str]) -> int:
    return solve(lines, 3)


def solve(lines: list[str], number_operators: int) -> int:
    total = 0

    for line in lines:
        test_value, numbers = parse_line(line)

        for i in range(number_operators ** (len(numbers) - 1)):
            result = numbers[0]
            tmp = i
            for j in range(1, len(numbers)):
                result = compute(result, numbers[j], tmp % number_operators)
                tmp = tmp // number_operators

            if result == test_value:
                total += result
                break

    return total


def parse_line(line: str) -> tuple[int, list[int]]:
    test_value, numbers = line.split(":")
    test_value = int(test_value)
    nums = list(map(int, numbers.split()))

    return test_value, nums


def compute(left: int, right: int, op: int) -> int:
    if op == 0:
        result = left + right
    elif op == 1:
        result = left * right
    else:
        result = int(str(left) + str(right))

    return result


if __name__ == '__main__':
    input_lines = readfile("day07/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
