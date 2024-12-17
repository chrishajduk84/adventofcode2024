import math
from helper import get_input

def parse_list(data):
    list1 = []
    list2 = []
    lines = data.split("\n")
    for line in lines:
        row = line.split('   ')
        if len(row) >= 2:
            list1.append(int(row[0]))
            list2.append(int(row[1]))
    return list1, list2

if __name__ == "__main__":
    raw_input = get_input(1, "53616c7465645f5f853e1541deca2aeb019ce32e474c04a1b4dd042bb7b1da70ae94d5b1c5837f84c47c821709a458284061ada2f0484873ad913eb463b7e3e6")
    list1, list2 = parse_list(raw_input)
    list1.sort()
    list2.sort()

    diff = 0
    for i in range(len(list1)):
        diff += math.fabs(list1[i] - list2[i])
    print(f"Difference: {diff}")

    frequency_counter = {}
    for value in list2:
        if value in frequency_counter:
            frequency_counter[value] += 1
        else:
            frequency_counter[value] = 1
    similarity_score = 0
    for value in list1:
        count = frequency_counter.get(value, 0)
        similarity_score += count * value
    print(similarity_score)
