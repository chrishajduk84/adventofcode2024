from helper import get_input
import re

def parse_input(data):
    split_data = data.split("\n")
    ordering_rule = []
    page_list = []
    for i in split_data:
        if "|" in i:
            # This is an ordering rule
            vals = i.split("|")
            ordering_rule.append((int(vals[0]), int(vals[1])))
        elif "," in i:
            # This is a page list
            vals = i.split(",")
            page_list.append([int(v) for v in vals])
    return page_list, ordering_rule


if __name__ == "__main__":
    raw_input = get_input(5, "53616c7465645f5f853e1541deca2aeb019ce32e474c04a1b4dd042bb7b1da70ae94d5b1c5837f84c47c821709a458284061ada2f0484873ad913eb463b7e3e6")

    page_lists, ordering_rules = parse_input(raw_input)
    summation = 0
    bad_ordered_page_lists = []
    for pages in page_lists:
        good_page_list = True
        for first, second in ordering_rules:
            first_detected = False
            second_detected = False
            for i in pages:
                if first == i:
                    first_detected = True
                elif second == i:
                    second_detected = True

                if first in pages and second_detected and not first_detected:
                    good_page_list = False
                    # print(f"{first} -> {second}")
                    # print(f"{pages}: {good_page_list}")
                    break

        if good_page_list:
            summation += pages[len(pages)//2]
        else:
            bad_ordered_page_lists.append(pages)

    print(summation)

    summation2 = 0
    # Part 2 - order them correctly
    for pages in bad_ordered_page_lists:
        # Do swaps until it passes
        good_page_list = False
        while not good_page_list:
            good_page_list = True
            for first, second in ordering_rules:
                first_index = -1
                second_index = -1
                for i in range(len(pages)):
                    if first == pages[i]:
                        first_index = i
                    elif second == pages[i]:
                        second_index = i

                    if first_index >= 0 and second_index >= 0 and second_index < first_index:
                        good_page_list = False
                        temp_val = pages[second_index]
                        pages[second_index] = pages[first_index]
                        pages[first_index] = temp_val
                        # print(f"{first} -> {second}")
                        # print(f"{pages}: {good_page_list}")
                        break

        summation2 += pages[len(pages) // 2]
    print(summation2)