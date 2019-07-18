"""aoc 2015 implementation"""
import itertools

from aoc.utils import *


# day 01
def get_floor(instructions: str) -> int:
    """get the floor to go to for the given instructions"""
    floor = 0
    for word in instructions:
        if word == "(":
            floor += 1
        elif word == ")":
            floor -= 1
        else:
            raise ValueError(f"{word} is not a valid instruction")
    return floor


def get_first_step_basement(instructions: str) -> int:
    """get the first step that reaches the first basement"""
    floor = 0

    for step, word in enumerate(instructions):
        if word == "(":
            floor += 1
        elif word == ")":
            floor -= 1
        else:
            raise ValueError(f"{word} is not a valid instruction")
        if floor == -1:
            return step + 1

    raise ValueError(f"with the given instructions it did not reach the -1 floor")


def day_01_a() -> int:
    """solve first challenge for day 01"""
    return get_floor(read_instructions('aoc/aoc2015/input/01A.txt'))


def day_01_b() -> int:
    """solve second challenge for day 01"""
    return get_first_step_basement(read_instructions('aoc/aoc2015/input/01A.txt'))


# day 02
def get_wrapping_paper(*args) -> int:
    squares = [a * b for a, b in itertools.combinations(args, 2)]
    return min(squares) + sum(2 * sq for sq in squares)


def get_ribbon(*args) -> int:
    return sum(l_mult(min_n(args, 2), 2)) + product(args)


def day_02_a() -> int:
    """solve first challenge for day 02"""
    instructions = read_instructions('aoc/aoc2015/input/02A.txt').split('\n')
    return sum(get_wrapping_paper(*l_to_int(box.split('x'))) for box in instructions)


def day_02_b() -> int:
    """solve second challenge for day 02"""
    instructions = read_instructions('aoc/aoc2015/input/02A.txt').split('\n')
    return sum(get_ribbon(*l_to_int(box.split('x'))) for box in instructions)


# day 03
def day_03_a() -> int:
    """solve first challenge for day 03"""
    return 0


def day_03_b() -> int:
    """solve second challenge for day 03"""
    return 0


# day 04
def day_04_a() -> int:
    """solve first challenge for day 04"""
    return 0


def day_04_b() -> int:
    """solve second challenge for day 04"""
    return 0


# day 05
def day_05_a() -> int:
    """solve first challenge for day 05"""
    return 0


def day_05_b() -> int:
    """solve second challenge for day 05"""
    return 0


# day 06
def day_06_a() -> int:
    """solve first challenge for day 06"""
    return 0


def day_06_b() -> int:
    """solve second challenge for day 06"""
    return 0


# day 07
def day_07_a() -> int:
    """solve first challenge for day 07"""
    return 0


def day_07_b() -> int:
    """solve second challenge for day 07"""
    return 0



