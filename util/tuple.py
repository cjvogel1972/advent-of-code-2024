from operator import add, sub


def tuple_add(t1, t2: tuple[int, int]) -> tuple[int, int]:
    return tuple(map(add, t1, t2))


def tuple_subtract(t1, t2: tuple[int, int]) -> tuple[int, int]:
    return tuple(map(sub, t1, t2))
