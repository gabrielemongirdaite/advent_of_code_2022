import re
import dijkstar
from itertools import permutations


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            ln = []
            ln.append(int(re.findall(r'-?\d+', line)[0]))
            ln.extend(re.findall('([A-Z][A-Z])', line))
            lines.append(ln)
    return lines


data = read_file('input_day16.txt')


def add_edges(data):
    graph = dijkstar.Graph()
    dct = {}
    for i in data:
        node = i[1]
        for j in i[2:]:
            graph.add_edge(node, j, 1)
        if i[0] != 0:
            dct[i[1]] = i[0]
    return graph, dct


def possible_combinations(val_map):
    lst = list(val_map.keys())
    return list(permutations(lst, len(lst)))


def find_path(comb, graph, val_map, min):
    minutes = 0
    comb = ['AA'] + list(comb)
    pressure = 0
    for ind, j in enumerate(comb):
        try:
            minutes += dijkstar.find_path(graph, j, comb[ind + 1])[3] + 1
        except:
            pass
        if minutes > min:
            break
        else:
            try:
                pressure += (min - minutes) * val_map[comb[ind + 1]]
            except:
                pass
    return pressure


G, values_map = add_edges(data)


#look for crazy drawing in photos. Idea: remove zero flow nodes and simplify graph. Then it is clearly seen a path towards JT
print(find_path(['CA', 'JF', 'LE', 'FP', 'YH', 'UX', 'AR', 'DM'], G, values_map, 30))

combinations = possible_combinations({'CA': 1, 'JF': 1, 'LE': 1, "YH": 1, "UX": 1, "AR": 1, "FP": 1})
result = 0
for i in combinations:
    r = (find_path(i, G, values_map, 26))
    if r > result:
        result = r
        print(i)
print((result))
combinations = possible_combinations({'TU': 1, 'UK': 1, 'EK': 1, "GW": 1, "JT": 1})
result = 0
for i in combinations:
    r = (find_path(i, G, values_map, 26))
    if r > result:
        result = r
        print(i)
print((result))

