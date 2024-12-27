from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    wires = {}
    for i in range(len(lines)):
        if lines[i] == "":
            break
        name, value = lines[i].split(": ")
        wires[name] = int(value)

    gates = {}
    for line in lines[i + 1:]:
        logic, name = line.split(" -> ")
        gates[name] = logic

    solve_circuit(gates, wires)

    return create_int(wires, 'z')


def solve_part2(lines: list[str]) -> bool:
    wires = {}
    for i in range(len(lines)):
        if lines[i] == "":
            break
        name, value = lines[i].split(": ")
        wires[name] = int(value)

    gates = {}
    for line in lines[i + 1:]:
        logic, name = line.split(" -> ")
        gates[name] = logic

    solve_circuit(gates, wires)


    x = create_int(wires, 'x')
    y = create_int(wires, 'y')
    expected_z = x + y

    return create_int(wires, 'z') == expected_z


def solve_circuit(gates, wires):
    while gates:
        keys = list(gates.keys())
        for gate in keys:
            in1, op, in2 = gates[gate].split(" ")
            if in1 not in wires or in2 not in wires:
                continue
            if op == "AND":
                wires[gate] = wires[in1] & wires[in2]
            elif op == "OR":
                wires[gate] = wires[in1] | wires[in2]
            elif op == "XOR":
                wires[gate] = wires[in1] ^ wires[in2]
            gates.pop(gate)


def create_int(wires: dict, prefix: str) -> int:
    i = 0
    result = 0
    while True:
        key = "%s%02d" % (prefix, i)
        if key not in wires:
            print(key)
            break
        result |= wires[key] << i
        i += 1

    return result


def swap_keys(gates, keys, indexes, num_swaps, swapped):
    for i in range(num_swaps):
        indices = [index for index, x in enumerate(indexes) if x == (i + 1)]
        k1 = keys[indices[0]]
        k2 = keys[indices[1]]
        swapped.append((k1, k2))
        v1 = gates[k1]
        gates[k1] = gates[k2]
        gates[k2] = v1


if __name__ == '__main__':
    input_lines = readfile("day24/input.txt")
    fixed_input_lines = readfile("day24/fixed_input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(fixed_input_lines)}')
