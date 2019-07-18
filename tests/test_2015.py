import pytest
from aoc.aoc2015 import *


@pytest.mark.parametrize("instructions, expected", [
    ("(())", 0),
    ("()()", 0),
    ("(((", 3),
    ("(()(()(", 3),
    ("())", -1),
    ("))(", -1)
])
def test_get_instructions(instructions, expected):
    assert get_floor(instructions) == expected


@pytest.mark.parametrize("instructions, expected", [
    (")", 1),
    ("()())", 5)
])
def test_get_step_basement(instructions, expected):
    assert get_first_step_basement(instructions) == expected


def test_day_01_a():
    assert day_01_a() == 74


def test_day_01_b():
    assert day_01_b() == 1795


def test_day_02_a():
    assert day_02_a() == 1588178


@pytest.mark.parametrize("l, w, h, expected", [
    (2, 3, 4, 34),
    (1, 1, 10, 14)
])
def test_get_ribbon(l, w, h, expected):
    assert get_ribbon(l, w, h == expected)


def test_day_02_b():
    assert day_02_b() == 3783758


@pytest.mark.parametrize("instructions, houses", [
    ('>', 2),
    ('^>v<', 4),
    ('^v^v^v^v^v', 2)
])
def test_how_many_houses_were_visited(instructions, houses):
    assert len(get_visited_houses(instructions)) == houses


def test_day_03_a():
    assert day_03_a() == 2565


def test_day_03_b():
    assert day_03_b() == 2639


def test_day_04_a():
    assert day_04_a() == 254575


def test_day_04_b():
    assert day_04_b() == 1038736


def test_day_05_a():
    assert day_05_a() == 238


def test_day_05_b():
    assert day_05_b() == 69


def test_day_06_a():
    assert day_06_a() == 377891


def test_day_06_b():
    assert day_06_b() == 14110788


def test_day_07_a():
    assert day_07_a() == 46065


def test_day_07_b():
    assert day_07_b() == 46065

