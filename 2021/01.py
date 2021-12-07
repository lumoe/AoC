import numpy as np
import pandas as pd

from numpy.lib.stride_tricks import sliding_window_view

inp = 'in01.txt'

df = pd.read_csv(inp, header=None)
df = np.array(df.iloc[:, 0])

# Part 1
v = sliding_window_view(df, (2,))
print(((v[:, 1] - v[:, 0]) > 0).sum())


# Part 2
v = sliding_window_view(df, (3,))
sums = v[:, 2] + v[:, 1] + v[:, 0]
sums = sliding_window_view(sums, (2,))
print(((sums[:, 1] - sums[:, 0]) > 0).sum())
