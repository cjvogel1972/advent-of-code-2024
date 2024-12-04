from util.file import readfile
from util.grid import good_square


def solve_part1(lines: list[str]) -> int:
    total = 0

    puzzle = [[c for c in line] for line in lines]
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == "X":
                total += find_mas(puzzle, "MAS", i, j, -1, -1)
                total += find_mas(puzzle, "MAS", i, j, -1, 0)
                total += find_mas(puzzle, "MAS", i, j, -1, 1)
                total += find_mas(puzzle, "MAS", i, j, 0, 1)
                total += find_mas(puzzle, "MAS", i, j, 1, 1)
                total += find_mas(puzzle, "MAS", i, j, 1, 0)
                total += find_mas(puzzle, "MAS", i, j, 1, -1)
                total += find_mas(puzzle, "MAS", i, j, 0, -1)

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    puzzle = [[c for c in line] for line in lines]
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == "A":
                total += find_ms(puzzle, i, j)

    return total


def find_mas(puzzle: list[list[str]], word: str, row: int, col: int, dx: int, dy: int) -> int:
    if good_square(puzzle, row + dx, col + dy):
        if puzzle[row + dx][col + dy] == word[0]:
            if len(word) == 1:
                return 1
            return find_mas(puzzle, word[1:], row + dx, col + dy, dx, dy)
    return 0


def find_ms(puzzle: list[list[str]], row: int, col: int) -> int:
    if good_square(puzzle, row - 1, col - 1) and good_square(puzzle, row + 1, col + 1):
        if (puzzle[row - 1][col - 1] == 'M'and puzzle[row + 1][col + 1] == 'S') or (puzzle[row - 1][col - 1] == 'S'and puzzle[row + 1][col + 1] == 'M'):
            if good_square(puzzle, row + 1, col - 1) and good_square(puzzle, row - 1, col + 1):
                if (puzzle[row + 1][col - 1] == 'M' and puzzle[row - 1][col + 1] == 'S') or (
                        puzzle[row + 1][col - 1] == 'S' and puzzle[row - 1][col + 1] == 'M'):
                    return 1
    return 0


if __name__ == '__main__':
    input_lines = readfile("day04/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
