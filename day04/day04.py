from util.file import readfile
from util.grid import good_square, directions


def solve_part1(lines: list[str]) -> int:
    total = 0

    puzzle = [[c for c in line] for line in lines]
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == "X":
                for d in directions:
                    total += find_xmas(puzzle, "XMAS", i, j, d[0], d[1])

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    puzzle = [[c for c in line] for line in lines]
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == "A":
                total += find_x_mas(puzzle, i, j)

    return total


def find_xmas(puzzle: list[list[str]], word: str, row: int, col: int, dx: int, dy: int) -> int:
    if good_square(puzzle, row + (dx * (len(word) - 1)), col + (dy * (len(word) - 1))):
        if all([puzzle[row + (dx * i)][col + (dy * i)] == word[i] for i in range(len(word))]):
            return 1
    return 0


def find_x_mas(puzzle: list[list[str]], row: int, col: int) -> int:
    if good_square(puzzle, row - 1, col - 1) and good_square(puzzle, row + 1, col + 1):
        diag1 = puzzle[row - 1][col - 1] + puzzle[row + 1][col + 1]
        diag2 = puzzle[row + 1][col - 1] + puzzle[row - 1][col + 1]
        if diag1 in ["MS", "SM"] and diag2 in ["MS", "SM"]:
            return 1
    return 0


if __name__ == '__main__':
    input_lines = readfile("day04/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
