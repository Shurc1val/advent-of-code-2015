
from read_data_function import read_data


# ----- PART ONE -----

def parse_instruction(instruction: str, lights: list[list[int]]):
    instruction = instruction.replace("turn ","")
    instruction_parts = instruction.split(" ")
    action = instruction_parts[0]
    light_range = [[int(coord) for coord in part.split(",")] for part in instruction_parts if part.replace(",","").isnumeric()]
    match action:
        case "on":
            for i in range(light_range[0][0], light_range[1][0] + 1):
                for j in range(light_range[0][1], light_range[1][1] + 1):
                    lights[i][j] = 1
        case "off":
            for i in range(light_range[0][0], light_range[1][0] + 1):
                for j in range(light_range[0][1], light_range[1][1] + 1):
                    lights[i][j] = 0
        case "toggle":
            for i in range(light_range[0][0], light_range[1][0] + 1):
                for j in range(light_range[0][1], light_range[1][1] + 1):
                    lights[i][j] = 1 - lights[i][j]

def part_one(str_input: str) -> int:
    lights = [[0 for i in range(1000)] for j in range(1000)]
    instructions = str_input.split("\n")
    for instruction in instructions:
        parse_instruction(instruction, lights)
    return sum([row.count(1) for row in lights])


def test_basic():
    assert part_one("turn on 0,0 through 999,999") == 1000000
    assert part_one("toggle 0,0 through 999,0") == 1000
    assert part_one("turn off 499,499 through 500,500") == 0
    assert part_one("""turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500""") == 998996


# ----- PART TWO -----


def parse_instruction_2(instruction: str, lights: list[list[int]]):
    instruction = instruction.replace("turn ","")
    instruction_parts = instruction.split(" ")
    action = instruction_parts[0]
    light_range = [[int(coord) for coord in part.split(",")] for part in instruction_parts if part.replace(",","").isnumeric()]
    match action:
        case "on":
            for i in range(light_range[0][0], light_range[1][0] + 1):
                for j in range(light_range[0][1], light_range[1][1] + 1):
                    lights[i][j] += 1
        case "off":
            for i in range(light_range[0][0], light_range[1][0] + 1):
                for j in range(light_range[0][1], light_range[1][1] + 1):
                    lights[i][j] = max(lights[i][j] - 1, 0)
        case "toggle":
            for i in range(light_range[0][0], light_range[1][0] + 1):
                for j in range(light_range[0][1], light_range[1][1] + 1):
                    lights[i][j] += 2


def part_two(str_input: str):
    lights = [[0 for i in range(1000)] for j in range(1000)]
    instructions = str_input.split("\n")
    for instruction in instructions:
        parse_instruction_2(instruction, lights)
    return sum([sum([num for num in row]) for row in lights])


def test_part_two():
    assert part_two("""turn on 0,0 through 0,0""") == 1
    assert part_two("""toggle 0,0 through 999,999""") == 2000000


# --------------------


if __name__ == "__main__":
    print(part_one(read_data("day_6.txt")))
    print(part_two(read_data("day_6.txt")))