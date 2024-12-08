from util.file import readfile
from util.grid import good_square, good_square_tuple
from util.tuple import tuple_subtract, tuple_add


def solve_part1(lines: list[str]) -> int:
    antenna_map = [[c for c in line] for line in lines]
    antennas = find_antennas(antenna_map)

    antinodes = set()
    for frequency in antennas:
        positions = antennas[frequency]
        for i in range(len(positions) - 1):
            for j in range(i + 1, len(positions)):
                delta = tuple_subtract(positions[i], positions[j])
                a1 = tuple_add(positions[i], delta)
                if good_square_tuple(antenna_map, a1):
                    antinodes.add(a1)
                a2 = tuple_subtract(positions[j], delta)
                if good_square_tuple(antenna_map, a2):
                    antinodes.add(a2)

    return len(antinodes)


def solve_part2(lines: list[str]) -> int:
    antenna_map = [[c for c in line] for line in lines]
    antennas = find_antennas(antenna_map)

    antinodes = set()
    for frequency in antennas:
        positions = antennas[frequency]
        for i in range(len(positions) - 1):
            for j in range(i + 1, len(positions)):
                antinodes.add(positions[i])
                antinodes.add(positions[j])
                delta = tuple_subtract(positions[i], positions[j])
                pos = positions[i]
                while True:
                    pos = tuple_add(pos, delta)
                    if good_square_tuple(antenna_map, pos):
                        antinodes.add(pos)
                    else:
                        break
                pos = positions[j]
                while True:
                    pos = tuple_subtract(pos, delta)
                    if good_square_tuple(antenna_map, pos):
                        antinodes.add(pos)
                    else:
                        break

    return len(antinodes)


def find_antennas(antenna_map: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    antennas = {}
    for r in range(len(antenna_map)):
        for c in range(len(antenna_map[0])):
            if antenna_map[r][c] != ".":
                positions = antennas.get(antenna_map[r][c], [])
                positions.append((r, c))
                antennas[antenna_map[r][c]] = positions

    return antennas


if __name__ == '__main__':
    input_lines = readfile("day08/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
