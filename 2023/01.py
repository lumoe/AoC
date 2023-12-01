with open("in/01.in") as f:
    data = f.read()

# Part 1
floor = 0
for i in data:
    if i == '(':
        floor += 1
    elif i ==  ')':
        floor -= 1


print(floor)

# Part 2
floor = 0
for idx, i in enumerate(data):
    if i == '(':
        floor += 1
    elif i ==  ')':
        floor -= 1
    
    if floor == -1:
        print(f'Entering basement @{idx+1}')
        break

