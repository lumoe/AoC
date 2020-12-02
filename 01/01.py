import itertools
import numpy as np
mport pandas as pd

data = pd.read_csv('input')
inp = data.values.flatten()
prod = itertools.combinations(inp, 3)
prod = np.array(list(prod))
for i in prod:
    if np.sum(i) == 2020:
        print(np.prod(i))
