from aoc.utils import *


def get_required_fuel(mass):
    return mass // 3 - 2


def day_01_a():
    filename = 'aoc/aoc2019/input/01A.txt'
    mass_list = read_int_list(filename) 
    return sum(get_required_fuel(mass) for mass in mass_list)


def day_01_b():
    filename = 'aoc/aoc2019/input/01A.txt'
    mass_list = read_int_list(filename) 

    total_fuel = 0

    for mass in mass_list:
        while True:
            fuel_required = get_required_fuel(mass)
            if fuel_required <= 0:
                break
            total_fuel += fuel_required
            mass =  fuel_required
    
    return total_fuel


def get_values_to_operate(instructions, idx):
    a = instructions[instructions[idx * 4 + 1]]
    b = instructions[instructions[idx * 4 + 2]]
    return a, b


def follow_instructions(instructions, noun, verb):
    new_instructions = instructions[:]
    new_instructions[1] = noun
    new_instructions[2] = verb

    return get_instructions_output(new_instructions)


def get_instructions_output(instructions):
    for i in range(len(instructions) // 4 + 1):
        instruction = instructions[i * 4]
        if instruction == 1:
            a, b = get_values_to_operate(instructions, i)
            instructions[instructions[i * 4 + 3]] = a + b

        elif instruction == 2:
            a, b = get_values_to_operate(instructions, i)
            instructions[instructions[i * 4 + 3]] = a * b
            
        elif instruction == 99:
            return instructions[0]
        else:
            raise ValueError('no valid instruction')


def day_02_a():
    filename = 'aoc/aoc2019/input/02A.txt'
    noun = 12
    verb = 2
    instructions = list(l_to_int(read_instructions(filename).split(',')))
    
    return follow_instructions(instructions, noun, verb)


def day_02_b():
    filename = 'aoc/aoc2019/input/02A.txt'
    expected_output = 19690720
    instructions = list(l_to_int(read_instructions(filename).split(',')))

    for noun in range(100):
        for verb in range(100):
            try:
                if follow_instructions(instructions, noun, verb) == expected_output:
                    return noun, verb
            except ValueError:
                pass
