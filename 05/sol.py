import numpy as np
import math
import re

inp = np.array(open('input').read().splitlines())

def bin_search(s, upper, lower):
    if len(s) == 0:
        return upper
    current = s.pop()
    mid = (upper + lower) // 2
    if current in 'FL':
        upper = mid
    else:
        lower = mid
    return bin_search(s, upper, lower)
    
def get_seat_id(bp):
    rows = list(bp[:7][::-1])
    row = bin_search(rows, 127, 0)
    seats = list(bp[7:][::-1])
    seat = bin_search(seats, 7, 0)
    return row, seat, row * 8 + seat

seats = [get_seat_id(row)[2] for row in inp]
lowest_seat = min(seats)
highest_seat = max(seats)
print('Part 1:', highest_seat)

# Visual solution by printing the airplane
# airplane = np.zeros((128,8))
# for row in inp:
#     row, seat, seat_id = get_seat_id(row)
#     airplane[row, seat] = seat_id

# for row in airplane:
#     print(row)

print('Part 2: ', set(list(range(lowest_seat, highest_seat)))-set(seats))
