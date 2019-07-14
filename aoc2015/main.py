"""aoc 2015 implementation"""


def read_instructions(filename: str) -> str:
    """read the instructions file"""
    with open(filename) as file:
        return file.read()


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
    return get_floor(read_instructions('aoc2015/input/01A.txt'))


if __name__ == '__main__':
    print(day_01_a())
