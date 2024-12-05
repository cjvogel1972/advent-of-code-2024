from functools import cmp_to_key

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    rules, updates = parse_input(lines)
    for line in updates:
        pages = list(map(int, line.split(",")))
        if is_update_correct(pages, rules):
            total += pages[len(pages) // 2]

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    rules, updates = parse_input(lines)
    for line in updates:
        pages = list(map(int, line.split(",")))
        if not is_update_correct(pages, rules):
            fixed = reorder_pages(pages, rules)
            total += fixed[len(fixed) // 2]

    return total


def parse_input(lines: list[str]) -> tuple[dict[int, list[int]], list[str]]:
    rules = {}
    update_start = 0
    for i, line in enumerate(lines):
        if line.strip() == "":
            update_start = i + 1
            break
        l, r = map(int, line.split("|"))
        rule = rules.get(l, [])
        rule.append(r)
        rules[l] = rule

    updates = lines[update_start:]
    return rules, updates


def is_update_correct(pages, rules) -> bool:
    for i in range(len(pages)):
        rule = rules.get(pages[i], [])
        if not all(page in rule for page in pages[i + 1:]):
            return False
    return True


def reorder_pages(pages: list[int], rules: dict[int, list[int]]) -> list[int]:
    return sorted(pages, key=cmp_to_key(lambda page1, page2: -1 if page2 in rules.get(page1, []) else 1))


if __name__ == '__main__':
    input_lines = readfile("day05/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
