from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    disk_map = [c for c in lines[0]]

    file_id = 0
    disk = []
    file = True
    for c in disk_map:
        block = str(file_id) if file else "."
        for i in range(int(c)):
            disk.append(block)
        if file:
            file_id += 1
        file = not file

    next_free_block = find_next_free_block(disk, 0)
    last_used_block = find_last_used_block(disk, len(disk) - 1)

    while next_free_block < last_used_block:
        disk[next_free_block] = disk[last_used_block]
        disk[last_used_block] = '.'
        next_free_block = find_next_free_block(disk, next_free_block + 1)
        last_used_block = find_last_used_block(disk, last_used_block - 1)

    return compute_checksum(disk)


def solve_part2(lines: list[str]) -> int:
    disk_map = [c for c in lines[0]]

    file_id = 0
    disk = []
    file = True
    for c in disk_map:
        block = str(file_id) if file else "."
        for i in range(int(c)):
            disk.append(block)
        if file:
            file_id += 1
        file = not file

    moved = set()
    last_used_block = find_last_used_block(disk, len(disk) - 1)

    while True:
        next_free_block = find_next_free_block(disk, 0)
        if next_free_block > last_used_block:
            break
        changed = False
        end_file_size = 0
        while last_used_block - end_file_size >= 0 and disk[last_used_block - end_file_size] == disk[last_used_block]:
            end_file_size += 1

        if disk[last_used_block] not in moved:
            while not changed and next_free_block < last_used_block:
                empty_block_size = 0
                while disk[next_free_block + empty_block_size] == disk[next_free_block]:
                    empty_block_size += 1

                if end_file_size <= empty_block_size:
                    moved.add(disk[last_used_block])
                    for _ in range(end_file_size):
                        disk[next_free_block] = disk[last_used_block]
                        disk[last_used_block] = '.'
                        next_free_block += 1
                        last_used_block -= 1
                    changed = True
                else:
                    next_free_block = find_next_free_block(disk, next_free_block + empty_block_size)
        if not changed:
            last_used_block = find_last_used_block(disk, last_used_block - end_file_size)
        else:
            last_used_block = find_last_used_block(disk, last_used_block)
        if last_used_block == 0:
            break

    return compute_checksum(disk)


def find_next_free_block(disk: list[str], ptr: int) -> int:
    while True:
        if disk[ptr] == ".":
            break
        ptr += 1

    return ptr


def find_last_used_block(disk: list[str], ptr: int) -> int:
    while True:
        if disk[ptr] != ".":
            break
        ptr -= 1

    return ptr


def compute_checksum(disk: list[str]) -> int:
    total = 0

    for i in range(len(disk)):
        if disk[i] == ".":
            continue
        total += i * int(disk[i])

    return total


if __name__ == '__main__':
    input_lines = readfile("day09/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
