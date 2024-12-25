from collections import Counter

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    secret_numbers = [int(line) for line in lines]

    for _ in range(2000):
        for j in range(len(secret_numbers)):
            secret_numbers[j] = calculate_next_secret_number(secret_numbers[j])

    return sum(secret_numbers)


def solve_part2(lines: list[str]) -> int:
    secret_numbers = [int(line) for line in lines]
    sequences = Counter()

    for j in range(len(secret_numbers)):
        secret_number = secret_numbers[j]
        prev_price = secret_number % 10
        price_changes = []
        seen = set()
        for i in range(2000):
            secret_number = calculate_next_secret_number(secret_number)
            current_price = secret_number % 10
            price_changes.append(current_price - prev_price)
            prev_price = current_price
            if i > 2:
                seq = tuple(price_changes[-4:])
                if seq not in seen:
                    sequences[seq] += current_price
                    seen.add(seq)

    return sequences.most_common(1)[0][1]


def calculate_next_secret_number(secret_number):
    number = secret_number * 64
    secret_number = mix(secret_number, number)
    secret_number = prune(secret_number)
    number = secret_number // 32
    secret_number = mix(secret_number, number)
    secret_number = prune(secret_number)
    number = secret_number * 2048
    secret_number = mix(secret_number, number)
    secret_number = prune(secret_number)

    return secret_number


def mix(secret_number: int, value: int) -> int:
    return secret_number ^ value


def prune(secret_number: int) -> int:
    return secret_number % 16777216


if __name__ == '__main__':
    input_lines = readfile("day22/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
