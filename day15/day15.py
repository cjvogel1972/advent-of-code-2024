from util.file import readfile
from util.grid import cardinal_directions
from util.tuple import tuple_add


def solve_part1(lines: list[str]) -> int:
    walls = set()
    boxes = set()
    robot = (0, 0)
    r = 0
    for r, line in enumerate(lines):
        if line.strip() == "":
            break
        for c, square in enumerate(line):
            if square == "#":
                walls.add((r, c))
            elif square == "O":
                boxes.add((r, c))
            elif square == "@":
                robot = (r, c)

    moves = lines[r + 1:]
    for line in moves:
        for direction in line:
            new_robot_loc = move(robot, direction)

            if new_robot_loc in walls:
                continue
            if new_robot_loc in boxes:
                pushed = push_box(new_robot_loc, boxes, walls, direction)
                if pushed:
                    robot = new_robot_loc
                continue

            robot = new_robot_loc

    total = 0
    for box in boxes:
        total += box[0] * 100 + box[1]

    return total


def solve_part2(lines: list[str]) -> int:
    walls = set()
    boxes = set()
    robot = (0, 0)
    r = 0
    for r, line in enumerate(lines):
        if line.strip() == "":
            break
        for c, square in enumerate(line):
            if square == "#":
                walls.add((r, 2 * c))
                walls.add((r, 2 * c + 1))
            elif square == "O":
                boxes.add(((r, 2 * c), (r, 2 * c + 1)))
                # boxes.add((r, 2 * c + 1))
            elif square == "@":
                robot = (r, 2 * c)

    moves = lines[r + 1:]
    for line in moves:
        for direction in line:
            new_robot_loc = move(robot, direction)

            if new_robot_loc in walls:
                continue
            for box in boxes:
                if new_robot_loc in box:
                    if direction in "<>":
                        pushed = push_double_boxes_left_right(box, boxes, walls, direction)
                        if pushed:
                            robot = new_robot_loc
                        break
                    else:
                        boxes_to_push = set()
                        boxes_to_push.add(box)
                        pushed = push_double_boxes_up_down(boxes_to_push, boxes, walls, direction)
                        if pushed:
                            robot = new_robot_loc
                        break
            else:
                robot = new_robot_loc

    total = 0
    for box in boxes:
        total += box[0][0] * 100 + box[0][1]

    return total


def move(loc: tuple[int, int], direction: str) -> tuple[int, int]:
    if direction == "^":
        new_loc = tuple_add(loc, cardinal_directions[0])
    elif direction == ">":
        new_loc = tuple_add(loc, cardinal_directions[1])
    elif direction == "v":
        new_loc = tuple_add(loc, cardinal_directions[2])
    else:
        new_loc = tuple_add(loc, cardinal_directions[3])

    return new_loc


def push_box(loc: tuple[int, int], boxes: set[tuple[int, int]], walls: set[tuple[int, int]], direction: str) -> bool:
    new_loc = move(loc, direction)
    if new_loc in walls:
        return False
    if new_loc in boxes:
        pushed = push_box(new_loc, boxes, walls, direction)
        if pushed:
            boxes.add(new_loc)
            boxes.remove(loc)
        return pushed

    boxes.add(new_loc)
    boxes.remove(loc)
    return True


def push_double_boxes_left_right(box: tuple[tuple[int, int], tuple[int, int]], boxes: set[tuple[int, int], tuple[int, int]], walls: set[tuple[int, int]], direction: str) -> bool:
    new_loc = (move(box[0], direction), move(box[1], direction))
    if new_loc[0] in walls or new_loc[1] in walls:
        return False
    for b in boxes:
        if b == box:
            continue
        if new_loc[0] in b or new_loc[1] in b:
            pushed = push_double_boxes_left_right(b, boxes, walls, direction)
            if pushed:
                boxes.add(new_loc)
                boxes.remove(box)
            return pushed

    boxes.add(new_loc)
    boxes.remove(box)
    return True


def push_double_boxes_up_down(boxes_to_push: set[tuple[tuple[int, int]], tuple[int, int]], boxes: set[tuple[int, int], tuple[int, int]], walls: set[tuple[int, int]], direction: str) -> bool:
    next_boxes_to_push = set()
    boxes_new_locs = set()
    for box in boxes_to_push:
        new_loc = (move(box[0], direction), move(box[1], direction))
        boxes_new_locs.add(new_loc)
        if new_loc[0] in walls or new_loc[1] in walls:
            return False

        for b in boxes:
            if b == box:
                continue
            if new_loc[0] in b or new_loc[1] in b:
                next_boxes_to_push.add(b)

    if len(next_boxes_to_push) == 0:
        for box in boxes_to_push:
            boxes.remove(box)
        boxes.update(boxes_new_locs)
        return True

    pushed = push_double_boxes_up_down(next_boxes_to_push, boxes, walls, direction)
    if pushed:
        for box in boxes_to_push:
            boxes.remove(box)
        boxes.update(boxes_new_locs)

    return pushed


if __name__ == '__main__':
    input_lines = readfile("day15/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
