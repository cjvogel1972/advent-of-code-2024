import re

from util.file import readfile


def solve_part1(lines: list[str], size: tuple[int, int]) -> int:
    robots = parse_robots(lines)

    for i in range(100):
        for index, robot in enumerate(robots):
            robots[index] = (move_robot(robot, size), robot[1])

    tall_half = size[1] // 2
    wide_half = size[0] // 2
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        y, x = robot[0]
        if y < tall_half and x < wide_half:
            q1 += 1
        elif y < tall_half and x > wide_half:
            q2 += 1
        elif y > tall_half and x < wide_half:
            q3 += 1
        elif y > tall_half and x > wide_half:
            q4 += 1

    return q1 * q2 * q3 * q4


def solve_part2(lines: list[str], size: tuple[int, int]) -> int:
    robots = parse_robots(lines)

    seconds = 0
    for seconds in range(size[0] * size[1]):
        grid = [['.' for y in range(size[1])] for x in range(size[0])]
        locations = set()
        for index, robot in enumerate(robots):
            robots[index] = (move_robot(robot, size), robot[1])
            grid[robot[0][1]][robot[0][0]] = "#"
            locations.add(robot[0])
        if len(locations) == len(robots):
            break

    return seconds


def parse_robots(lines):
    robots = []
    robot_parsing = re.compile("(-?\d+)")
    for line in lines:
        px, py, vx, vy = robot_parsing.findall(line)
        robots.append(((int(py), int(px)), (int(vy), int(vx))))
    return robots


def move_robot(robot: tuple[tuple[int, int], tuple[int, int]], size: tuple[int, int]) -> tuple[int, int]:
    y, x = robot[0]
    dy, dx = robot[1]
    y += dy
    x += dx
    if y < 0:
        y += size[1]
    if y >= size[1]:
        y -= size[1]
    if x < 0:
        x += size[0]
    if x >= size[0]:
        x -= size[0]

    return y, x

if __name__ == '__main__':
    input_lines = readfile("day14/input.txt")

    print(f'Part 1: {solve_part1(input_lines, (101, 103))}')
    print(f'Part 2: {solve_part2(input_lines, (101, 103))}')
