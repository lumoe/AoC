import numpy as np

"""
INPUT: 
3-5 f: fgfff
3-5 f --> policy
fgfff --> password
"""

inp = open('input').readlines()
inp = [i.strip() for i in inp]

counts = [np.array(i.split(' ')[0].split('-'), dtype=np.int32) for i in inp]
rules = [i.split(' ')[1][0] for i in inp]
passwords = [i.split(' ')[2] for i in inp]
found = 0

for idx, password in enumerate(passwords):
    count = password.count(rules[idx])
    if count >= counts[idx][0] and count <= counts[idx][1]:
        found += 1

print('Part 1:', found)

found = 0
for idx, password in enumerate(passwords):
    if (password[counts[idx][0]-1] != password[counts[idx][1]-1]) \
       and (
           (password[counts[idx][0] - 1] == rules[idx])
           or (password[counts[idx][1]-1] == rules[idx])):
        found += 1

print('Part 2:', found)
