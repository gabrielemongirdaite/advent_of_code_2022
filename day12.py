import dijkstar
import string
import time


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            ln = []
            for j in line:
                ln.extend(j)
            ln = [list(string.ascii_lowercase).index(i) + 1 if i != 'S' and i != 'E' else i for i in ln]
            lines.append(ln)
    return lines


def above_dir(x, y, seq):
    if x - 1 >= 0:
        above = seq[x - 1][y]
    else:
        above = 100
    return above


def below_dir(x, y, seq):
    try:
        below = seq[x + 1][y]
    except:
        below = 100
    return below


def left_dir(x, y, seq):
    if y - 1 >= 0:
        left = seq[x][y - 1]
    else:
        left = 100
    return left


def right_dir(x, y, seq):
    try:
        right = seq[x][y + 1]
    except:
        right = 100
    return right


def starting_ending_points(seq):
    for x, i in enumerate(seq):
        for y, j in enumerate(i):
            if j == 'S':
                start_point = x * len(seq[0]) + y
                seq[x][y] = 1
            elif j == 'E':
                end_point = x * len(seq[0]) + y
                seq[x][y] = 26
    return seq, start_point, end_point


def add_nodes_to_graph(seq):
    graph = dijkstar.Graph()
    for x, i in enumerate(seq):
        for y, j in enumerate(i):
            current_point = x * len(seq[0]) + y
            if above_dir(x, y, seq) - 1 <= j:
                destination_point = (x - 1) * len(seq[0]) + y
                graph.add_edge(current_point, destination_point, 1)
            if below_dir(x, y, seq) - 1 <= j:
                destination_point = (x + 1) * len(seq[0]) + y
                graph.add_edge(current_point, destination_point, 1)
            if left_dir(x, y, seq) - 1 <= j:
                destination_point = x * len(seq[0]) + (y - 1)
                graph.add_edge(current_point, destination_point, 1)
            if right_dir(x, y, seq) - 1 <= j:
                destination_point = x * len(seq[0]) + (y + 1)
                graph.add_edge(current_point, destination_point, 1)
    return graph


start_time = time.time()
seq = read_file('input_day12.txt')
seq, start_point, end_point = starting_ending_points(seq)
graph = add_nodes_to_graph(seq)
print('1st part answer: ' + str(dijkstar.find_path(graph, start_point, end_point)[3]))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
all_paths = []
for x, i in enumerate(seq):
    for y, j in enumerate(i):
        if j == 1:
            current_point = x * len(seq[0]) + y
            try:
                all_paths.append(dijkstar.find_path(graph, current_point, end_point)[3])
            except:
                pass
print('2nd part answer: ' + str(min(all_paths)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))

