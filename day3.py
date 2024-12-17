from helper import get_input
import re

# def parse_memory(data):
#     list = []
#     lines = data.split("\n")
#     for line in lines:
#         row = line.split(' ')
#         if len(row) > 1:
#             int_row = [int(r) for r in row]
#             list.append(int_row)
#     return list

if __name__ == "__main__":
    raw_input = get_input(3, "53616c7465645f5f853e1541deca2aeb019ce32e474c04a1b4dd042bb7b1da70ae94d5b1c5837f84c47c821709a458284061ada2f0484873ad913eb463b7e3e6")
    mul_matcher = re.compile("mul\(([0-9]{1,3}),([0-9]{1,3})\)")
    match_iterator = mul_matcher.finditer(raw_input)

    value = 0
    for match in match_iterator:
        value += int(match.group(1)) * int(match.group(2))
    print(value)

    mul_matcher = re.compile("mul\(([0-9]{1,3}),([0-9]{1,3})\)|do\(\)|don't\(\)")
    match_iterator = mul_matcher.finditer(raw_input)

    value = 0
    enabled = True
    for match in match_iterator:
        if "do()" in match.group():
            enabled = True
        elif "don't()" in match.group():
            enabled = False
        elif "mul" in match.group() and enabled:
            value += int(match.group(1)) * int(match.group(2))
    print(value)