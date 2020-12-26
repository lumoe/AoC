inp = open('input').read().split('\n')

"""
[
    'bag_name': [
        (amount, bag),
        (amount, bag)
    ]
]
"""


def count_gold_bags(bn, bags):
    for bgs in bags[bn]:
        if 'shiny gold' in bgs[1]:
            return True
        if count_gold_bags(bgs[1], bags):
            return True


def count_gold_bags_depth(bn, bags, cbags=0, multi=1):
    for bgs in bags[bn]:
        cbags += bgs[0]*multi + multi * \
            count_gold_bags_depth(bgs[1], bags, multi=bgs[0])
    return cbags


bags = {}
for idx, i in enumerate(inp):
    # print(idx)
    bn = i.split('bags')[0].strip()
    try:
        amount = [int(x.strip().split(' ')[0])
                  for x in i.split('contain')[1].split(',')]
    except:
        amount = []
    names = [' '.join(x.strip().split(' ')[1:3])
             for x in i.split('contain')[1].split(',')]
    bags[bn] = list(zip(amount, names))

acc = 0
for bag in bags:
    res = count_gold_bags(bag, bags)
    if res:
        acc += 1

print('Part 1:', acc)


res = count_gold_bags_depth('shiny gold', bags)
print('Part 2:', res)
