# Formula: 2*l*w + 2*w*h + 2*h*l
# Iput: 2x3x4
# Compute: 2*6 + 2*12 + 2*8 + 6


# Part 1 
with open("in/02.in") as f:
    data = f.read().splitlines()

total = 0
for row in data:
    l, w, h = row.split('x')
    l, w, h = (int(l), int(w), int(h))

    res = 2*l*w + 2*w*h + 2*h*l
    smallest_area = min([l*w, w*h, h*l])
    res += smallest_area
    total += res

print(f"Total sqft {total}")

# Part 2
total = 0
for row in data:
    l, w, h = row.split('x')
    l, w, h = (int(l), int(w), int(h))

    res = l * w * h
    sa = list(sorted([l, w, h]))
    res += sa[0] * 2 + sa[1] * 2

    total += res

print(f"Requried ribbon {total}ft")
    
