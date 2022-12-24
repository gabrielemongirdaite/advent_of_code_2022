import dijkstar
import itertools


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def move_blizzards(map, n_org):
    blizzards = []
    min_y = 1
    max_y = len(map) - 2
    min_x = 1
    max_x = len(map[1]) - 2
    for y, i in enumerate(map):
        for x, j in enumerate(i):
            if j in ['v', '^', '>', '<']:
                if j == 'v':
                    n = n_org % max_y
                    if y + n <= max_y:
                        blizzards.append((x, y + n))
                        # print((x, y), '-->', (x, y + n))
                    else:
                        blizzards.append((x, (y + n) % max_y))
                        # print((x, y), '-->', (x, (y + n) % max_y))
                elif j == '^':
                    n = n_org % max_y
                    if y - n >= min_y:
                        blizzards.append((x, y - n))
                        # print((x, y), '-->', (x, y - n), '1')
                    else:
                        blizzards.append((x, max_y - (max_y if n % max_y == 0 else n % max_y) + (y - min_y + 1)))
                        # print((x, y), '-->', (x, max_y - (max_y if n % max_y == 0 else n % max_y) + (y - min_y + 1)),'2')
                elif j == '>':
                    n = n_org % max_x
                    if x + n <= max_x:
                        blizzards.append((x + n, y))
                        # print((x, y), '-->', (x + n, y))
                    else:
                        blizzards.append(((x + n) % max_x, y))
                        # print((x, y), '-->', ((x + n) % max_x, y))
                elif j == '<':
                    n = n_org % max_x
                    if x - n >= min_x:
                        blizzards.append((x - n, y))
                        # print((x, y), '-->', (x - n, y))
                    else:
                        blizzards.append((max_x - (max_x if n % max_x == 0 else n % max_x) + (x - min_x + 1), y))
                        # print((x, y), '-->', (max_x - (max_x if n % max_x == 0 else n % max_x) + (x - min_x + 1), y))
    return blizzards


def create_path(map, start, end, min):
    graph = dijkstar.Graph()

    start_node = start[1] * len(map[1]) + start[0]
    end_node = end[1] * len(map[1]) + end[0]
    path = 0
    last_added = [start]
    while path == 0:
        min += 1
        last_added_tmp = []
        blizzards = move_blizzards(map, min)
        # print(blizzards)
        for i in last_added:
            try:
                m1 = map[i[1]][i[0] + 1]
            except:
                m1 = '#'
            try:
                m2 = map[i[1]][i[0] - 1]
            except:
                m2 = '#'
            try:
                m3 = map[i[1] + 1][i[0]]
            except:
                m3 = '#'
            try:
                m4 = map[i[1] - 1][i[0]]
            except:
                m4 = '#'
            if (i[0] + 1, i[1]) not in blizzards and m1 != '#' and i[0] + 1 <= len(map[1]) - 2:
                graph.add_edge(i[1] * len(map[1]) + i[0], i[1] * len(map[1]) + (i[0] + 1), 1)
                last_added_tmp.append((i[0] + 1, i[1]))
            if (i[0] - 1, i[1]) not in blizzards and m2 != '#' and i[0] - 1 >= 1:
                graph.add_edge(i[1] * len(map[1]) + i[0], i[1] * len(map[1]) + (i[0] - 1), 1)
                last_added_tmp.append((i[0] - 1, i[1]))
            if (i[0], i[1] + 1) not in blizzards and m3 != '#' and i[1] + 1 <= len(map) - 2:
                graph.add_edge(i[1] * len(map[1]) + i[0], (i[1] + 1) * len(map[1]) + i[0], 1)
                last_added_tmp.append((i[0], i[1] + 1))
            if (i[0], i[1] - 1) not in blizzards and m4 != '#' and i[1] - 1 >= 1:
                graph.add_edge(i[1] * len(map[1]) + i[0], (i[1] - 1) * len(map[1]) + i[0], 1)
                last_added_tmp.append((i[0], i[1] - 1))
            if (i[0], i[1]) not in blizzards:
                last_added_tmp.append((i[0], i[1]))
        try:
            path = dijkstar.find_path(graph, start_node, end_node)[3]
        except:
            pass
        if last_added_tmp != []:
            last_added_tmp.sort()
            last_added = (list(k for k, _ in itertools.groupby(last_added_tmp)))
    return min


m = read_file("input_day24.txt")
print(create_path(m, (0, 1), (len(m[1]) - 2, len(m) - 2), 0) + 1)
print(create_path(m, (len(m[1]) - 2, len(m) - 1), (1, 1), 308)+1)
print(create_path(m, (0, 1), (len(m[1]) - 2, len(m) - 2), 598) + 1)
