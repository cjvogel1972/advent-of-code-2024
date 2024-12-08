from util.file import readfile
from util.grid import good_square


def solve_part1(lines: list[str]) -> int:
    antenna_map = [[c for c in line] for line in lines]
    antennas = {}
    for r in range(len(antenna_map)):
        for c in range(len(antenna_map[0])):
            if antenna_map[r][c] != ".":
                positions = antennas.get(antenna_map[r][c], [])
                positions.append((r,c))
                antennas[antenna_map[r][c]] = positions

    antinodes = set()
    for frequency in antennas:
        positions = antennas[frequency]
        for i in range(len(positions) - 1):
            for j in range(i + 1, len(positions)):
                dr = positions[i][0] - positions[j][0]
                dc = positions[i][1] - positions[j][1]
                a1r = positions[i][0] + dr
                a1c = positions[i][1] + dc
                a2r = positions[j][0] - dr
                a2c = positions[j][1] - dc
                if good_square(antenna_map, a1r, a1c):
                    antinodes.add((a1r, a1c))
                if good_square(antenna_map, a2r, a2c):
                    antinodes.add((a2r, a2c))

    return len(antinodes)


def solve_part2(lines: list[str]) -> int:
    antenna_map = [[c for c in line] for line in lines]
    antennas = {}
    for r in range(len(antenna_map)):
        for c in range(len(antenna_map[0])):
            if antenna_map[r][c] != ".":
                positions = antennas.get(antenna_map[r][c], [])
                positions.append((r,c))
                antennas[antenna_map[r][c]] = positions

    antinodes = set()
    for frequency in antennas:
        positions = antennas[frequency]
        for i in range(len(positions) - 1):
            for j in range(i + 1, len(positions)):
                antinodes.add((positions[i][0], positions[i][1]))
                antinodes.add((positions[j][0], positions[j][1]))
                dr = positions[i][0] - positions[j][0]
                dc = positions[i][1] - positions[j][1]
                r = positions[i][0]
                c = positions[i][1]
                while True:
                    r += dr
                    c += dc
                    if good_square(antenna_map, r, c):
                        antinodes.add((r, c))
                    else:
                        break
                r = positions[j][0]
                c = positions[j][1]
                while True:
                    r -= dr
                    c -= dc
                    if good_square(antenna_map, r, c):
                        antinodes.add((r, c))
                    else:
                        break

    return len(antinodes)



if __name__ == '__main__':
    input_lines = readfile("day08/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
