import numpy as np
import re


def has_properties(p, props=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
    p = ''.join(p)
    return all(x in p for x in props)


inp = np.array(open('input').read().splitlines())
pp = np.where(inp == '')[0]
pp = np.append(pp, [len(inp)])
pp = np.insert(pp, 0, 0, axis=0)
found = 0
for idx, p in enumerate(pp[:-1]):
    if has_properties(inp[p:pp[idx + 1]]):
        found += 1

print('Part 1:', found)

# Using regex instead of split
# would result most probably in a much cleaner solution


def check_year_property(p, prop, minv, maxv):
    v = int(p.split(prop + ':')[1][:4])
    return v >= minv and v <= maxv


def check_height_property(p):
    v = p.split('hgt:')[1].split(' ')[0]
    h = int(v[:-2])
    u = v[-2:]
    return h >= 150 and h <= 193 if u == 'cm' else h >= 59 and h <= 76


def check_hair_color(p):
    v = p.split('hcl:')[1].split(' ')[0][:7]
    return re.search('#[0-9a-f]{6}', v) != None


def check_eye_color(p):
    ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    v = p.split('ecl:')[1].split(' ')[0][:4]
    return any(x in v for x in ecl)


def check_pid(p):
    v = p.split('pid:')[1].split(' ')[0]
    return len(v) == 9 and v.isdigit()


years = [
    ['byr', 1920, 2002],
    ['iyr', 2010, 2020],
    ['eyr', 2020, 2030],
]


found = 0
for idx, p in enumerate(pp[:-1]):
    cur = inp[p:pp[idx + 1]]
    cur = ' '.join(cur)
    # if(has_properties(cur) and ):
    if has_properties(cur) \
            and all(check_year_property(cur, x[0], x[1], x[2]) for x in years) \
            and check_height_property(cur) \
            and check_hair_color(cur) \
            and check_eye_color(cur) \
            and check_pid(cur):

        found += 1

print('Part 2: ', found)
