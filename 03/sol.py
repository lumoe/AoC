inp = open('input').read().splitlines()


def slope(x_, y_):
    x = x_
    y = y_
    trees = 0
    while y < len(inp):
        if (inp[y][x % len(inp[0])] == '#'):
            trees += 1
        x += x_
        y += y_
    return trees


print('Part 1:', slope(3, 1))
print('Part 2:', slope(1, 1) * slope(3, 1) *
      slope(5, 1) * slope(7, 1) * slope(1, 2))
