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
    a = instructions[instructions[idx + 1]]
    b = instructions[instructions[idx + 2]]
    return a, b


def follow_instructions(instructions, noun, verb):
    new_instructions = instructions[:]
    new_instructions[1] = noun
    new_instructions[2] = verb

    return get_instructions_output(new_instructions)


def get_instructions_output(instructions):
    i = 0
    while True:
        instruction = instructions[i]
        if instruction == 1:
            a, b = get_values_to_operate(instructions, i)
            instructions[instructions[i + 3]] = a + b
            i += 4

        elif instruction == 2:
            a, b = get_values_to_operate(instructions, i)
            instructions[instructions[i + 3]] = a * b
            i += 4

        elif instruction == 3:
            a = instructions[i + 1]
            instructions[a] = a
            i += 2

        elif instruction == 4:
            a = instructions[i + 1]
            return instructions[a]
            
        elif instruction == 99:
            return instructions[0]
        else:
            print(instruction)
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


def get_steps(instruction):
    return int(instruction[1:])


def get_direction(direction):
    if direction == 'R':
        return 0, 1
    if direction == 'L':
        return 0, -1
    if direction == 'U':
        return 1, 1
    if direction == 'D':
        return 1, -1


def get_cable_trace(instructions):
    trace = set()
    pos = [0, 0]

    for instruction in instructions:
        idx, delta = get_direction(instruction[0])
        steps = get_steps(instruction)      

        for _ in range(steps):
            pos[idx] += delta
            trace.add(tuple(pos))

    return trace


def manhattan_distance(*vectors):
    return sum(abs(abs(a) - abs(b)) for a, b in zip(*vectors))


def calculate_distances(crosses):
    return {cross: manhattan_distance(cross, (0, 0)) for cross in crosses}


def calculate_steps(instructions_a, instructions_b, crosses):
    return {cross: get_min_steps(instructions_a, cross) + get_min_steps(instructions_b, cross) for cross in crosses}


def get_min_steps(instructions, point):
    pos = [0, 0]
    num_steps = 0

    for instruction in instructions:
        idx, delta = get_direction(instruction[0])
        steps = get_steps(instruction)  
        
        for _ in range(steps):
            pos[idx] += delta
            num_steps += 1

            if pos == list(point):
                return num_steps


def day_03_a():
    filename = 'aoc/aoc2019/input/03A.txt'
    instructions = read_instructions(filename).split('\n')
    cable_a = instructions[0].split(',')
    cable_b = instructions[1].split(',')

    trace_a = get_cable_trace(cable_a)
    trace_b = get_cable_trace(cable_b)
    
    crosses = trace_a & trace_b

    distance_matrix = calculate_distances(crosses)

    return min(distance_matrix.values())


def day_03_b():
    filename = 'aoc/aoc2019/input/03A.txt'
    instructions = read_instructions(filename).split('\n')
    instructions_a = instructions[0].split(',')
    instructions_b = instructions[1].split(',')

    trace_a = get_cable_trace(instructions_a)
    trace_b = get_cable_trace(instructions_b)
    
    crosses = trace_a & trace_b

    steps_matrix = calculate_steps(instructions_a, instructions_b, crosses)

    return min(steps_matrix.values())



def is_increasing(num):
    str_num = str(num)
    for a, b in zip(str_num, str_num[1:]):
        if b < a:
            return False
    return True


def has_consecutive(num):
    str_num = str(num)
    for a, b in zip(str_num, str_num[1:]):
        if b == a:
            return True
    return False

def has_consecutive_no_larger(num):
    str_num = str(num)

    curr_digit = ''
    curr_count = 0
    repeating = []

    for digit in str_num:
        if digit == curr_digit:
            curr_count += 1
        else:
            repeating.append(curr_count)
            curr_count = 1
        curr_digit = digit
    repeating.append(curr_count)

    return 2 in repeating


def check_number(num):
    return is_increasing(num) and has_consecutive(num)


def check_numbers(low, up, requirements):
    count = 0
    for num in range(low, up + 1):
        if all(requirement(num) for requirement in requirements):
            count += 1
    return count

def day_04_a():
    low_limit, up_limit = 152085, 670283
    return check_numbers(low_limit, up_limit, [is_increasing, has_consecutive])

def day_04_b():
    low_limit, up_limit = 152085, 670283
    return check_numbers(low_limit, up_limit, [is_increasing, has_consecutive_no_larger])


def get_def_0(text, idx):
    try:
        return int(text[idx])
    except IndexError:
        return 0


def parse_instruction(instruction):
    str_instruction = str(instruction)
    optcode = int(str_instruction[2:])
    first_mode =  get_def_0(str_instruction, -3)
    second_mode = get_def_0(str_instruction, -4)
    third_mode = get_def_0(str_instruction, -5)

    return optcode, first_mode, second_mode, third_mode


def get_instructions_output_l2(instructions):
    i = 0
    while True:
        optcode = parse_instruction(instructions[i])
        if optcode == 1:
            a, b = get_values_to_operate(instructions, i)
            instructions[instructions[i + 3]] = a + b
            i += 4

        elif optcode == 2:
            a, b = get_values_to_operate(instructions, i)
            instructions[instructions[i + 3]] = a * b
            i += 4

        elif optcode == 3:
            a = instructions[i + 1]
            instructions[a] = a
            i += 2

        elif optcode == 4:
            a = instructions[i + 1]
            return instructions[a]
            
        elif optcode == 99:
            return instructions[0]
        else:
            print(instruction)
            raise ValueError('no valid instruction')


def day_05_a():
    return parse_instruction(1002)