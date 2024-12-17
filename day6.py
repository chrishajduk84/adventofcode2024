import copy
import enum

from click import option

from day2 import parse_report
from helper import get_input
import re

class Direction(str, enum.Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

def is_out_of_bounds(i, j, map):
    if 0 <= i < len(map):
        if 0 <= j < len(map[i]):
            return False
    return True

def parse_input(data):
    return data.split("\n")

def print_map(map, guard_position):
    i = guard_position[0]
    j = guard_position[1]
    map2 = copy.deepcopy(map)
    map2[i] = map2[i][:j] + guard_position[2] + map2[i][j + 1:]
    for i in range(len(map2)):
        print(map2[i])


def sim(map):
    # Find the guard position
    guard_position = [0, 0, Direction.UP]
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] in (Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT):
                direction = Direction(map[i][j])
                guard_position = [i, j, direction]

    unique_locations = set()
    unique_locations.add((guard_position[0], guard_position[1], guard_position[2]))
    # Iterate through the guard path
    while True:
        i = guard_position[0]
        j = guard_position[1]
        if guard_position[2] == Direction.UP:
            if is_out_of_bounds(i-1, j, map):
                guard_position[0] -= 1
                break
            if "#" == map[i-1][j]:
                guard_position[2] = Direction.RIGHT
                continue
            guard_position[0] -= 1
        elif guard_position[2] == Direction.DOWN:
            if is_out_of_bounds(i+1, j, map):
                guard_position[0] += 1
                break
            if "#" == map[i+1][j]:
                guard_position[2] = Direction.LEFT
                continue
            guard_position[0] += 1
        elif guard_position[2] == Direction.LEFT:
            if is_out_of_bounds(i, j-1, map):
                guard_position[1] -= 1
                break
            if "#" == map[i][j-1]:
                guard_position[2] = Direction.UP
                continue
            guard_position[1] -= 1
        elif guard_position[2] == Direction.RIGHT:
            if is_out_of_bounds(i, j+1, map):
                guard_position[1] += 1
                break
            if "#" == map[i][j + 1]:
                guard_position[2] = Direction.DOWN
                continue
            guard_position[1] += 1

        # print(guard_position)
        # print(is_out_of_bounds(i, j, map))
        if is_out_of_bounds(i, j, map):
            break
        if (guard_position[0], guard_position[1], guard_position[2]) in unique_locations:
            # print_map(map, guard_position)
            break
        unique_locations.add((guard_position[0], guard_position[1], guard_position[2]))
    return unique_locations, is_out_of_bounds(i, j, map), (guard_position[0], guard_position[1], guard_position[2]) in unique_locations, (i,j)

if __name__ == "__main__":
    raw_input = get_input(6, "53616c7465645f5f853e1541deca2aeb019ce32e474c04a1b4dd042bb7b1da70ae94d5b1c5837f84c47c821709a458284061ada2f0484873ad913eb463b7e3e6")

    map = parse_input(raw_input)


# PART 1
unique_locations, out_of_bounds, looping, final_location = sim(map)
print(len(unique_locations))

# Part 2
option_count = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        map2 = copy.deepcopy(map)
        if map2[i][j] not in (Direction.UP, Direction.DOWN, Direction.RIGHT, Direction.LEFT):
            map2[i] = map2[i][:j] + "#" + map2[i][j+1:]
        else:
            continue
        locations, out_of_bounds, looping, final_location = sim(map2)
        if looping:
            option_count += 1

print(option_count)