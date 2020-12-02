import itertools
import numpy as np
import pandas as pd


data = pd.read_csv('input')
inp = data.values.flatten()
prod = itertools.combinations(inp, 2)
prod = np.array(list(prod))
for i in prod:
    if np.sum(i) == 2020:
        print('Part 1:', np.prod(i))
        break


data = pd.read_csv('input')
inp = data.values.flatten()
prod = itertools.combinations(inp, 3)
prod = np.array(list(prod))
for i in prod:
    if np.sum(i) == 2020:
        print('Part 2:', np.prod(i))
        break
