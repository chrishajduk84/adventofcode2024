from helper import get_input
import re

if __name__ == "__main__":
    raw_input = get_input(4, "53616c7465645f5f853e1541deca2aeb019ce32e474c04a1b4dd042bb7b1da70ae94d5b1c5837f84c47c821709a458284061ada2f0484873ad913eb463b7e3e6")

    matcher = re.compile("XMAS")

    # Rows
    rows = raw_input.split("\n")
    del rows[-1]    # Remove last row
    length = len(rows)


    # Columns
    columns = [""]*len(rows[0])
    for row in rows:
        for i in range(len(row)):
            character = row[i]
            columns[i] += character
    width = len(columns)

    # Diagonals which go from top-left to bottom-right
    # - Scan from bottom-left to top-right
    diagonal_down = [""]*(2*max(length, width) - 1)
    CENTER_OFFSET = max(length, width) - 1
    for x in range(0, length):
        for y in range(0, width):
            # y = x + b
            b = y - x + CENTER_OFFSET
            diagonal_down[b] += rows[y][x]

    # Diagonals which go from top-left to bottom-right
    # - Scan from bottom-left to top-right
    diagonal_up = [""]*(2*max(length, width) - 1)
    for x in range(0, width):
        for y in range(0, length):
            # y = -1*x + b
            b = y + x
            diagonal_up[b] += rows[y][x]

    count = 0
    for r in rows:
        m = matcher.findall(r)
        count += len(m)
        m = matcher.findall(r[::-1])
        count += len(m)

    for c in columns:
        m = matcher.findall(c)
        count += len(m)
        m = matcher.findall(c[::-1])
        count += len(m)

    for d1 in diagonal_down:
        m = matcher.findall(d1)
        count += len(m)
        m = matcher.findall(d1[::-1])
        count += len(m)

    for d2 in diagonal_up:
        m = matcher.findall(d2)
        count += len(m)
        m = matcher.findall(d2[::-1])
        count += len(m)
    print(count)

    # PART 2
    # We don't care about columns or rows, it needs to be the diagonals
    # We need to count the number of 'A's that are part of both diagonals.
    # As a consequence, we need to convert diagonal_down indices to diagonal_up indices and match them
    location_of_a = {}


    matcher = re.compile("MAS")
    for i in range(len(diagonal_down)):
        for m in matcher.finditer(diagonal_down[i]):
            start, end = m.span()

            if i <= CENTER_OFFSET:
                index_of_a = start + 1
            else:
                index_of_a = start + 1 + i - CENTER_OFFSET
            # Convert to original row-column index: y = mx + b
            offset_diagonal = i - CENTER_OFFSET  # == y - x
            y = index_of_a
            x = index_of_a - offset_diagonal
            if (x,y) not in location_of_a:
                location_of_a[(x,y)] = 1
            else:
                location_of_a[(x,y)] += 1
            # print(f"TOP{x},{y}: {rows[y][x]}")
        for m in matcher.finditer(diagonal_down[i][::-1]):
            start, end = m.span()
            if i <= CENTER_OFFSET:
                index_of_a = len(diagonal_down[i]) - end + 1
            else:
                index_of_a = len(diagonal_down[i]) - end + 1 + i - CENTER_OFFSET
            # print(m)
            # print(index_of_a)
            # print(diagonal_down[i][::-1])
            # input()
            # Convert to original row-column index: y = mx + b
            offset_diagonal = i - CENTER_OFFSET  # == y - x
            y = index_of_a
            x = index_of_a - offset_diagonal
            if (x, y) not in location_of_a:
                location_of_a[(x, y)] = 1
            else:
                location_of_a[(x, y)] += 1

            # print(diagonal_down[i][::-1])
            # print(index_of_a)

            # print(raw_input)
            # print(index_of_a)
            # print(diagonal_down[i])
            # print(diagonal_down[i][index_of_a])
            # print(f"{x},{y}: {rows[y][x]}")

    for i in range(len(diagonal_up)):
        for m in matcher.finditer(diagonal_up[i]):
            start, end = m.span()
            index_of_a = start + 1
            # Convert to original row-column index
            y = i - index_of_a
            x = index_of_a
            if (x,y) not in location_of_a:
                location_of_a[(x,y)] = 1
            else:
                location_of_a[(x,y)] += 1

        for m in matcher.finditer(diagonal_up[i][::-1]):
            start, end = m.span()
            index_of_a = len(diagonal_up[i]) - (start + 1) - 1
            # Convert to original row-column index
            y = i - index_of_a
            x = index_of_a
            if (x,y) not in location_of_a:
                location_of_a[(x,y)] = 1
            else:
                location_of_a[(x,y)] += 1

    print(location_of_a)
    num_mas = 0
    for location, count in location_of_a.items():
        if count >= 2:
            num_mas += 1
            print(f"{location}, {count}")

    print(num_mas)

    new_counter = 0
    for i in range(1, len(rows)-1):
        for j in range(1, len(rows[i])-1):
            value = rows[i][j]
            if value == "A":
                if (rows[i-1][j-1] == "M" and rows[i+1][j+1] == "S") or (rows[i-1][j-1] == "S" and rows[i+1][j+1] == "M"):
                    if rows[i+1][j-1] == "M" and rows[i - 1][j + 1] == "S":
                            new_counter += 1
                    elif rows[i+1][j-1] == "S" and rows[i - 1][j + 1] == "M":
                            new_counter += 1
    print(new_counter)