from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        test_value, numbers = line.split(":")
        test_value = int(test_value)
        nums = list(map(int, numbers.split()))

        for i in range(2 ** (len(nums) - 1)):
            result = nums[0]
            tmp = i
            for j in range(1, len(nums)):
                if tmp % 2 == 0:
                    result *= nums[j]
                else:
                    result += nums[j]

                tmp = tmp // 2

            if result == test_value:
                total += result
                break

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for line in lines:
        test_value, numbers = line.split(":")
        test_value = int(test_value)
        nums = list(map(int, numbers.split()))

        for i in range(3 ** (len(nums) - 1)):
            result = nums[0]
            tmp = i
            for j in range(1, len(nums)):
                if tmp % 3 == 0:
                    result *= nums[j]
                elif tmp % 3 == 1:
                    result += nums[j]
                else:
                    result = int(str(result) + str(nums[j]))

                tmp = tmp // 3

            if result == test_value:
                total += result
                break

    return total


if __name__ == '__main__':
    input_lines = readfile("day07/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
