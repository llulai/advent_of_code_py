import functools


def read_instructions(filename: str) -> str:
    """read the instructions file"""
    with open(filename) as file:
        return file.read()


def product(iterable):
    """returns the product of the elements of the iterable"""
    return functools.reduce(lambda a, b: a * b, iterable, 1)


def min_n(iterable, n):
    """returns the min n items from the iterable"""
    return list(sorted(iterable))[:n]


def l_to_int(iterable):
    return (int(it) for it in iterable)


def l_mult(iterable, n):
    return (it * n for it in iterable)


def max_n(iterable, n):
    """returns the max n items from the iterable"""
    return list(sorted(iterable))[-n:]
