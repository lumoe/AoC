import numpy as np
import pandas as pd

inp = 'in01.txt'

df = pd.read_csv(inp, sep=' ', header=None, dtype="string")
df = df[0].str.split('', expand=True)

# Part 1
gamma = ''.join([df[x].value_counts().index[0]
                 for x in range(1, len(df.columns) - 1)])
epsilon = ''.join([df[x].value_counts().index[1]
                   for x in range(1, len(df.columns) - 1)])

print('Part 1', int(epsilon, 2) * int(gamma, 2))
