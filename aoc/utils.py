import functools
from copy import copy


def read_instructions(filename: str) -> str:
    """read the instructions file"""
    with open(filename) as file:
        return file.read()

def read_int_list(filename: str) -> list:
    return l_to_int(read_instructions(filename).split('\n'))


def product(iterable):
    """returns the product of the elements of the iterable"""
    return functools.reduce(lambda a, b: a * b, iterable, 1)


def n_smallest(iterable, n):
    """returns the min n items from the iterable"""
    return list(sorted(iterable))[:n]


def l_to_int(iterable):
    return (int(it) for it in iterable)


def l_mult(iterable, n):
    return (it * n for it in iterable)


def n_largest(iterable, n):
    """returns the max n items from the iterable"""
    return list(sorted(iterable))[-n:]


def vec_add(iter_a, iter_b):
    """element wise addition"""
    if len(iter_a) != len(iter_b):
        raise ValueError
    return (a + b for a, b in zip(iter_a, iter_b))


def is_odd(i):
    return i % 2 == 1


def is_even(i):
    return i % 2 == 0


def merge_dicts(dict_a, dict_b):
    dict_c = copy(dict_a)
    dict_c.update(dict_b)
    return dict_c
