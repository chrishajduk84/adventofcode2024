from helper import get_input

def parse_report(data):
    list = []
    lines = data.split("\n")
    for line in lines:
        row = line.split(' ')
        if len(row) > 1:
            int_row = [int(r) for r in row]
            list.append(int_row)
    return list

def get_permutations(row):
    list_of_lists = []
    for i in range(len(row)):
        list_of_lists.append(row[0:i] + row[i+1:])
    return list_of_lists


if __name__ == "__main__":
    raw_input = get_input(2, "53616c7465645f5f853e1541deca2aeb019ce32e474c04a1b4dd042bb7b1da70ae94d5b1c5837f84c47c821709a458284061ada2f0484873ad913eb463b7e3e6")
    safe_report_count = 0

    data = parse_report(raw_input)
    for row in data:
        differences = [row[i] - row[i+1] for i in range(len(row) - 1)]
        increasing = all([i > 0 for i in differences])
        decreasing = all([i < 0 for i in differences])
        max_differences = all([abs(i) <= 3 and abs(i) >= 1 for i in differences])
        safe_report_count += 1 if (increasing ^ decreasing) and max_differences else 0
        # print(f"{differences}, {increasing}, {decreasing}, {max_differences}")
    print(safe_report_count)

    #data.append([1,2,2,1])
    # Problem dampener modification
    # safe_report_count = 0
    # for row in data:
    #     failure_count = 0
    #     differences = [row[i] - row[i+1] for i in range(len(row) - 1)]
    #     increasing_criteria = [i > 0 for i in differences]
    #     increasing_count = 0
    #     for i in increasing_criteria:
    #         increasing_count += 1 if i else 0
    #     decreasing_criteria = [i < 0 for i in differences]
    #     decreasing_count = 0
    #     for i in decreasing_criteria:
    #         decreasing_count += 1 if i else 0
    #     max_differences = [abs(i) <= 3 and abs(i) >= 1 for i in differences]
    #
    #     safe = [max_differences[i] for i in range(len(increasing_criteria))]
    #     if increasing_count > decreasing_count:
    #         safe = [safe[i] & increasing_criteria[i] for i in range(len(increasing_criteria))]
    #     elif increasing_count < decreasing_count:
    #         safe = [safe[i] & decreasing_criteria[i] for i in range(len(increasing_criteria))]
    #     else:
    #         safe = [safe[i] & (decreasing_criteria[i] & increasing_criteria[i]) for i in range(len(increasing_criteria))]
    #
    #     for i in safe:
    #         if not i:
    #             failure_count += 1
    #
    #     if failure_count <= 1:
    #         safe_report_count += 1
    #     print(f"ROW:{row}\nDIFFERENCES:{differences}\n{increasing_criteria}\n {decreasing_criteria}\n {max_differences}\n {safe} => SAFE: {failure_count <= 1}\n\n")
    #     print(increasing_count)
    #     print(decreasing_count)

    safe_report_count = 0
    for row in data:
        permutations = get_permutations(row)
        safe = False
        for d in [row] + permutations:
            differences = [d[i] - d[i+1] for i in range(len(d) - 1)]
            increasing = all([i > 0 for i in differences])
            decreasing = all([i < 0 for i in differences])
            max_differences = all([abs(i) <= 3 and abs(i) >= 1 for i in differences])
            safe = (increasing ^ decreasing) and max_differences
            if safe:
                break
        if safe:
            safe_report_count += 1
            # Try all the permutations un
        # print(f"{differences}, {increasing}, {decreasing}, {max_differences}")
    print(safe_report_count)





