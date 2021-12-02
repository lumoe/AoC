import numpy as np
import pandas as pd

from numpy.lib.stride_tricks import sliding_window_view


inp = 'in01.txt'

df = pd.read_csv(inp, sep=' ', header=None)

# Part 1
x = df[df.loc[:, 0] == 'forward'][1].sum()
y = df[df.loc[:, 0] == 'down'][1].sum() - df[df.loc[:, 0] == 'up'][1].sum()
print('Part 1', x*y)

# Part 2
df['x'] = df[df.loc[:, 0] == 'forward'][1].sum()
df['down'] = df[df.loc[:, 0] == 'down'][1].cumsum()
df['up'] = df[df.loc[:, 0] == 'up'][1].cumsum()

df = df.fillna(method="ffill").fillna(0)

df['aim'] = df['down'] - df['up']
df['depth'] = df[df.loc[:, 0] == 'forward'][1] * \
    df[df.loc[:, 0] == 'forward']['aim']

print('Part 2', int(df['depth'].sum() * df['x'].iloc[-1]))
