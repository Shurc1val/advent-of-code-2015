import pytest

from read_data_function import read_data

# ----- PART ONE -----


def parse_instruction(instruction_string: str):
    instructions = instruction_string.strip().split()
    match len(instructions):
        case 1:
            if instructions[0].isnumeric():
                return int(instructions[0])
            return instructions[0]
        case 2:
            instruction_dict = {
                'operation': 'NOT'
            }
            if instructions[1].isnumeric():
                instruction_dict['inputs'] = [int(instructions[1])]
            else:
                instruction_dict['inputs'] = [instructions[1]]
            return instruction_dict
        case other:
            operation = instructions[1]
            inputs = []
            for input in [instructions[0], instructions[2]]:
                if input.isnumeric():
                    inputs.append(int(input))
                else:
                    inputs.append(input)
            return {
                'operation': operation,
                'inputs': inputs
            }


def get_value(value: str, wires: dict) -> int:
    if isinstance(value, dict):
        return execute_instruction(value, wires)
    if isinstance(value, int):
        return value
    wires[value] = get_value(wires[value], wires)
    return wires[value]
    

def execute_instruction(instruction: dict, wires: dict) -> int:
    match instruction['operation']:
        case 'NOT':
            return ~get_value(instruction['inputs'][0], wires)
        case 'AND':
            return get_value(instruction['inputs'][0], wires) & get_value(instruction['inputs'][1], wires)
        case 'OR':
            return get_value(instruction['inputs'][0], wires) | get_value(instruction['inputs'][1], wires)
        case 'LSHIFT':
            return get_value(instruction['inputs'][0], wires) << get_value(instruction['inputs'][1], wires)
        case 'RSHIFT':
            return get_value(instruction['inputs'][0], wires) >> get_value(instruction['inputs'][1], wires)

def part_one(str_input: str, wire_key: str):
    wires = {}
    for line in str_input.split('\n'):
        wires[line.split("->")[1].strip()] = parse_instruction(line.split('->')[0])
    return get_value(wire_key, wires)

def test_part_one():
    assert part_one("""123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""", 'd') == 72


# ----- PART TWO -----


def part_two(str_input: str):
    wires = {}
    for line in str_input.split('\n'):
        wires[line.split("->")[1].strip()] = parse_instruction(line.split('->')[0])
    wires['b'] = part_one(str_input, 'a')
    return get_value('a', wires)

def test_part_two():
    assert part_two("""""") == None


# --------------------


if __name__ == "__main__":
    print(part_one(read_data("day_7.txt"), 'a'))
    print(part_two(read_data("day_7.txt")))