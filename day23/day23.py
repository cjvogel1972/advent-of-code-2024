from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    connections = {}
    for line in lines:
        c1, c2 = line.split('-')
        if c1 not in connections:
            connections[c1] = set()
        if c2 not in connections:
            connections[c2] = set()
        connections[c1].add(c2)
        connections[c2].add(c1)

    total = 0
    three_computer_lan = set()
    for computer in connections:
        conns = list(connections[computer])
        for i in range(len(conns) - 1):
            for j in range(i + 1, len(conns)):
                if conns[i] in connections[conns[j]]:
                    lan = frozenset({computer, conns[i], conns[j]})
                    three_computer_lan.add(lan)

    for lan in three_computer_lan:
        starts_t = False
        for c in lan:
            if c[0] == 't':
                starts_t = True

        if starts_t:
            total += 1

    return total


def solve_part2(lines: list[str]) -> str:
    connections = {}
    for line in lines:
        c1, c2 = line.split('-')
        if c1 not in connections:
            connections[c1] = set()
        if c2 not in connections:
            connections[c2] = set()
        connections[c1].add(c2)
        connections[c2].add(c1)

    max_lan = set()
    for computer in connections:
        lan = {computer}
        conns = list(connections[computer])
        all_conns = set(conns)
        all_conns.add(computer)
        list_conns_set = []
        for conn in conns:
            new_conns = set(connections[conn])
            new_conns.add(conn)
            intersection = all_conns.intersection(new_conns)
            if len(intersection) > 2:
                list_conns_set.append(intersection)
        lan = all_conns.intersection(*list_conns_set)

        if len(lan) > 3 and len(lan) > len(max_lan):
            max_lan = lan

    return ','.join(sorted(list(max_lan)))


if __name__ == '__main__':
    input_lines = readfile("day23/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
