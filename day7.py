import math
from helper import get_input

def parse_list(data):
    equations = []
    lines = data.split("\n")
    for line in lines:
        row = line.split(':')
        if len(row) == 2:
            values = [ int(i) for i in row[1].strip().split(' ')]
            equations.append((int(row[0]), values))
    return equations

def expand_tree(tree, value, operations=['+', '*']):
    for node, val in tree.items():
        if isinstance(val, int):
            level_dict = {}
            if '+' in operations:
                level_dict['+'] = val+rhs[i]
            if '*' in operations:
                level_dict['*'] = val*rhs[i]
            if '||' in operations:
                level_dict['||'] = int(str(val)+str(rhs[i]))
            tree[node] = level_dict
        else:
            expand_tree(val, value, operations)

def read_last_tree_values(tree):
    values = []
    for node, val in tree.items():
        if isinstance(val, int):
            values.append(val)
        else:
            values.extend(read_last_tree_values(val))
    return values
            

if __name__ == "__main__":
    raw_input = get_input(7, "53616c7465645f5f853e1541deca2aeb019ce32e474c04a1b4dd042bb7b1da70ae94d5b1c5837f84c47c821709a458284061ada2f0484873ad913eb463b7e3e6")
    eq = parse_list(raw_input)

    calibration_result = 0
    for lhs, rhs in eq:
        tree = {'start':rhs[0]}
        for i in range(1,len(rhs)):
            expand_tree(tree, rhs[i])
        #print(f"{lhs in read_last_tree_values(tree)} - {lhs}")
        if lhs in read_last_tree_values(tree):
            calibration_result += lhs
    print(calibration_result)

###########

    calibration_result = 0
    for lhs, rhs in eq:
        tree = {'start':rhs[0]}
        for i in range(1,len(rhs)):
            expand_tree(tree, rhs[i], operations=['+','*','||'])
        if lhs in read_last_tree_values(tree):
            calibration_result += lhs
    print(calibration_result)
