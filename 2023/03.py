import re 

from typing import List, Tuple


with open("in/03.in") as f:
    data = f.read().splitlines()


# data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".splitlines()

def get_neighbours(data: List[str], row: int, index: int):
    x_pos, y_pos = row, index
    neighbours = list()

    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            xi = x_pos + x
            yi = y_pos + y
            if x == 0 and y == 0:
                continue
            elif xi >= 0 and yi >= 0 and xi < len(data) and yi < len(data):
                neighbours.append(data[xi][yi])
    return neighbours

def char_is_digit_or_dot(char: str) -> bool:
    return not (char.isdigit() or char == '.')

def has_symbol_as_neighbour(data: List[str], row: int, span: Tuple[int, int]):
    for i in range(span[0], span[1]):
        # print(list(map(char_is_digit_or_dot, get_neighbours(data, row, i))))
        if any(map(char_is_digit_or_dot, get_neighbours(data, row, i))):
            return True
    return False


total = 0

for idx, line in enumerate(data):
    for entry in re.finditer(r'\d+', line):
        if has_symbol_as_neighbour(data, idx, entry.span()):
            total += int(line[entry.span()[0]:entry.span()[1]])

print(total)


# Part 2 

def gear_bounding_box(gear: re.Match, row: int, data: List[str]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    x_pos, y_pos = row, gear.span()[0]
    print("x,y@", (x_pos, y_pos), data[x_pos][y_pos])
    neighbours = list()

    xs, ys = [], []

    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            xi = x_pos + x
            yi = y_pos + y
            if xi >= 0 and yi >= 0 and xi < len(data) and yi < len(data):
                xs.append(xi)
                ys.append(yi)
    return (min(xs), min(ys)), (max(xs), max(ys))

def compute_overlap(bbox: Tuple[Tuple[int, int], Tuple[int, int]], all_numbers: List[Tuple[int, re.Match]]) -> List[int]:
    matching_numbers: List[int] = []
    print(bbox)
    y1b, x1b = bbox[0]
    y2b, x2b = bbox[1]


    for row, number in all_numbers:
        y1n, y2n = row, row
        x1n = number.span()[0]
        x2n = number.span()[1] - 1

        if x2b < x1n or x2n < x1b:
            continue
        
        if y2b < y1n or y2n < y1b:
            continue

        matching_numbers.append(number)
        
        print()
    return matching_numbers


all_numbers: List[Tuple[int, re.Match]] = []
for idx, line in enumerate(data):
    print(line)
    for entry in re.finditer(r'\d+', line):
        all_numbers.append((idx, entry))

total = 0
for idx, line in enumerate(data):
    for re_match in re.finditer(r'[*]', line):
        bbox = gear_bounding_box(re_match, idx, data)
        neighbours = compute_overlap(bbox, all_numbers)
        if len(neighbours) == 2:
            total += int(neighbours[0].group(0)) * int(neighbours[1].group(0))
                
print(total)