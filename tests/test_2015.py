from aoc2015 import *





def test_get_instructions():
    cases = [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("())", -1),
        ("))(", -1)
    ]

    for instructions, expected_output in cases:
        assert get_floor(instructions) == expected_output


def test_get_step_basement():
    cases = [
        (")", 1),
        ("()())", 5)
    ]

    for instructions, expected_output in cases:
        assert get_first_step_basement(instructions) == expected_output

