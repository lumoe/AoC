import numpy as np
import re

inp = open('input').read().split('\n\n')
inp = [len(set(x.replace('\n', ''))) for x in inp]
print('Part 1: ', sum(inp))

def is_everywhere(c, g):
    for i in g:
        if c not in i:
            return False
    return True

inp = open('input').read().split('\n\n')
inp = [(x.split('\n')) for x in inp]
count = 0
for g in inp:
    for c in g[0]:
        if is_everywhere(c, g):
            count += 1
print('Part 2: ', count)