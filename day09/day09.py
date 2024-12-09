from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    disk, file_sizes = parse_disk_map(lines[0])

    next_free_block = find_next_free_block(disk, file_sizes, 0)
    last_used_block = find_last_used_block(disk, len(disk) - 1)

    while next_free_block < last_used_block:
        disk[next_free_block] = disk[last_used_block]
        disk[last_used_block] = -1
        next_free_block = find_next_free_block(disk, file_sizes, next_free_block + 1)
        last_used_block = find_last_used_block(disk, last_used_block - 1)

    return compute_checksum(disk)


def solve_part2(lines: list[str]) -> int:
    disk, file_sizes = parse_disk_map(lines[0])

    moved = set()
    last_used_block = find_last_used_block(disk, len(disk) - 1)

    while True:
        next_free_block = find_next_free_block(disk, file_sizes, 0)
        if next_free_block > last_used_block:
            break

        end_file_size = file_sizes[disk[last_used_block]]

        if disk[last_used_block] not in moved:
            while next_free_block < last_used_block:
                empty_block_size = 0
                while disk[next_free_block + empty_block_size] == disk[next_free_block]:
                    empty_block_size += 1

                if end_file_size <= empty_block_size:
                    moved.add(disk[last_used_block])
                    move_file(disk, end_file_size, last_used_block, next_free_block)
                    break
                else:
                    next_free_block = find_next_free_block(disk, file_sizes, next_free_block + empty_block_size)

        last_used_block = find_last_used_block(disk, last_used_block - end_file_size)

    return compute_checksum(disk)


def parse_disk_map(disk_map: str) -> (list[int], dict[int, int]):
    file_id = 0
    disk = []
    file_sizes = {}
    file = True

    for c in disk_map:
        block = file_id if file else -1
        for i in range(int(c)):
            disk.append(block)
        if file:
            file_sizes[file_id] = int(c)
            file_id += 1
        file = not file

    return disk, file_sizes


def find_next_free_block(disk: list[int], files: dict[int, int], ptr: int) -> int:
    while True:
        if disk[ptr] == -1:
            break
        ptr += files[disk[ptr]]

    return ptr


def find_last_used_block(disk: list[int], ptr: int) -> int:
    while True:
        if disk[ptr] != -1:
            break
        ptr -= 1

    return ptr


def move_file(disk: list[int], file_size, move_from, move_to):
    for _ in range(file_size):
        disk[move_to] = disk[move_from]
        disk[move_from] = -1
        move_to += 1
        move_from -= 1


def compute_checksum(disk: list[int]) -> int:
    total = 0

    for i in range(len(disk)):
        if disk[i] == -1:
            continue
        total += i * disk[i]

    return total


if __name__ == '__main__':
    input_lines = readfile("day09/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
