# Part 1
def compute_acc(data):
    acc = 0
    _visited = []
    _ic = 0
    while _ic not in _visited and _ic < len(data):
        _visited.append(_ic)
        _action = data[_ic][:3]
        if _action == 'jmp':
            _ic += eval(data[_ic].split(' ')[1])
        elif _action == 'acc':
            acc += eval(data[_ic].split(' ')[1])
            _ic += 1
        else:
            _ic += 1

    return acc


inp = open('input', 'r').read().splitlines()
print('Part 1:', compute_acc(inp))


## ## ## ## ## ## ## ## ## ##

# Part 2
inp = open('input', 'r').read().splitlines()

visited = []
ic = 0
possible_edges = []
while ic not in visited and ic < len(inp):
    visited.append(ic)
    action = inp[ic][:3]
    if action == 'jmp':
        possible_edges.append(ic)
        ic += eval(inp[ic].split(' ')[1])
        continue
    elif action == 'nop':
        possible_edges.append(ic)

    ic += 1


def is_cyclic(data):
    _ic = 0
    _visited = []
    while _ic < len(data):
        if _ic in _visited:
            return True

        _visited.append(_ic)
        _action = data[_ic][:3]

        if _action == 'jmp':
            _ic += eval(data[_ic].split(' ')[1])
        else:
            _ic += 1

    return False


def find_cycle_free_graph(data, edges):
    for edge in edges:
        _data = data[:]
        action = _data[edge][:3]
        if action == 'jmp':
            _data[edge] = _data[edge].replace('jmp', 'nop')
        elif action == 'nop':
            _data[edge] = _data[edge].replace('nop', 'jmp')
        # print(_data)

        if not is_cyclic(_data):
            return _data


#
sol = find_cycle_free_graph(inp, possible_edges)
print('Part 2:', compute_acc(sol))
