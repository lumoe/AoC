import numpy as np

with open("in/01.in") as f:
    data = f.read().splitlines()

# Part 1
def compute_total(arr):
    total = 0
    for row in arr:
        numbers = list(filter(lambda x: x.isdigit(), row))
        number = int(numbers[0] + numbers[-1])
        total += number
    return total

print(f"Sum of numbers: {compute_total(data)}")


def indexOf(string: str | list, key: str | list):
    if isinstance(string, list):
        string = ''.join(string)
    if isinstance(key, list):
        key = ''.join(key)
    
    # print(key)
    # print(string)
    try:
        return string.index(key)
    except Exception as e:
        return 9999999

# Part 2
mapping = { k:str(idx + 1) for idx, k in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])}
print(mapping)

new_data = []


for row in data:
    li = [(key, indexOf(row, key)) for key in mapping.keys()]
    hi = [(key, (len(row) - indexOf(list(reversed(row)), list(reversed(key))))) for key in mapping.keys()]  

    li = sorted(li, key=lambda x: x[1])
    hi = sorted(hi, key=lambda x: -x[1])

    row = list(row)
    try:
        row[hi[0][1] - 1] = mapping[hi[0][0]]
    except Exception as e:
        pass

    try:
        row[li[0][1]] = mapping[li[0][0]]
    except Exception as e:
        pass 

    row = "".join(row)

    new_data.append(row)

print(f"Sum of numbers part 2: {compute_total(new_data)}")
