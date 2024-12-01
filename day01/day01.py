from util.file import readfile

def solve_part1(lines: list[str]) -> int:
    total = 0

    left: list[int] = []
    right: list[int] = []
    for line in lines:
        numbers = line.split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))
    left.sort()
    right.sort()

    for i in range(len(left)):
        total += abs(left[i] - right[i])

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    left: list[int] = []
    right: list[int] = []
    for line in lines:
        numbers = line.split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))
    left.sort()
    right.sort()

    for i in range(len(left)):
        count = 0
        for j in range(len(right)):
            if left[i] == right[j]:
                count += 1

        total += (left[i] * count)

    return total
if __name__ == '__main__':
    input_lines = readfile("day01/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')