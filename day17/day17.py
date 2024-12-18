import re

from util.file import readfile


def solve_part1(lines: list[str]) -> str:
    input_re = re.compile("(\d+)")
    a = int(input_re.search(lines[0]).group(0))
    b = int(input_re.search(lines[1]).group(0))
    c = int(input_re.search(lines[2]).group(0))
    program = list(map(int, input_re.findall(lines[4])))

    output = run_program(program, a, b, c)

    return ",".join(str(x) for x in output)


def solve_part2(lines: list[str]) -> int:
    input_re = re.compile("(\d+)")
    program = list(map(int, input_re.findall(lines[4])))

    return search(program, 0, 0)


def search(program: list[int], iteration: int, prev_a: int) -> int:
    if iteration == len(program):
        return prev_a
    for i in range(8):
        output = []
        ptr = 0
        start_a = prev_a * 8 + i
        a = start_a
        b = 0
        c = 0
        while True:
            op = program[ptr]
            combo_op = program[ptr + 1]
            ptr += 2

            if op == 3:
                break
            ptr, a, b, c = run_op(op, combo_op, output, a, b, c, ptr)

        if output[0] == program[-(iteration + 1)]:
            ans = search(program, iteration + 1, start_a)
            if ans is None: continue
            if program != run_program(program, ans, 0, 0): continue
            return ans


def run_program(program, a, b, c) -> list[int]:
    output = []
    ptr = 0
    while True:
        op = program[ptr]
        combo_op = program[ptr + 1]
        ptr += 2

        ptr, a, b, c = run_op(op, combo_op, output, a, b, c, ptr)
        if ptr == -1:
            break

    return output


def run_op(op: int, combo_op: int, output: list[int], a: int, b: int, c: int, ptr: int) -> tuple[
    int, int, int, int]:
    op_value = combo_op_value(combo_op, a, b, c)

    if op == 0:
        a = a // (2 ** op_value)
    elif op == 1:
        b = b ^ combo_op
    elif op == 2:
        b = op_value % 8
    elif op == 3:
        ptr = -1 if a == 0 else op_value
    elif op == 4:
        b = b ^ c
    elif op == 5:
        output.append(op_value % 8)
    elif op == 6:
        b = a // (2 ** op_value)
    elif op == 7:
        c = a // (2 ** op_value)

    return ptr, a, b, c


def combo_op_value(combo_op: int, a: int, b: int, c: int) -> int:
    if combo_op < 4:
        return combo_op
    elif combo_op == 4:
        return a
    elif combo_op == 5:
        return b
    elif combo_op == 6:
        return c


if __name__ == '__main__':
    input_lines = readfile("day17/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
