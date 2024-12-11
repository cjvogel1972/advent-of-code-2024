from collections import Counter

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    stones = Counter(map(int, lines[0].strip().split()))

    for _ in range(25):
        stones = blink(stones)

    return stones.total()


def solve_part2(lines: list[str]) -> int:
    stones = Counter(map(int, lines[0].strip().split()))

    for _ in range(75):
        stones = blink(stones)

    return stones.total()


def blink(stones: Counter[int]) -> Counter[int]:
    result = Counter()

    for stone in stones:
        num_stones = stones[stone]
        if stone == 0:
            result[1] += num_stones
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            stone1, stone2 = int(stone_str[:len(stone_str) // 2]), int(stone_str[len(stone_str) // 2:])
            result[stone1] += num_stones
            result[stone2] += num_stones
        else:
            result[stone * 2024] += num_stones

    return result


if __name__ == '__main__':
    input_lines = readfile("day11/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
