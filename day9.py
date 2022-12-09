import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    lst = []
    for i in lines:
        k = i.split(' ')
        lst.append([k[0], int(k[1])])
    return lst


def head_coordinates(steps):
    coordinates = [(0, 0)]
    for i in steps:
        current_coordinates = coordinates[-1]
        coordinates.extend(direction(current_coordinates[0], current_coordinates[1], i[0], i[1]))
    return coordinates


def tail_coordinates(head_coordinates):
    tail_coord = [(0, 0)]
    for i in head_coordinates:
        current_coordinates = tail_coord[-1]
        if tail_movements(current_coordinates, i) != []:
            tail_coord.append(tail_movements(current_coordinates, i))
    return len(set(tail_coord)), tail_coord


def tail_movements(current_tail, current_head):
    x_diff = current_head[0] - current_tail[0]
    y_diff = current_head[1] - current_tail[1]
    if current_tail == current_head or (abs(x_diff) == 1 and abs(y_diff) == 1) \
            or (abs(x_diff) == 1 and abs(y_diff) == 0) or (abs(x_diff) == 0 and abs(y_diff) == 1):
        return []
    elif abs(x_diff) == 2 and y_diff == 0:
        if x_diff > 0:
            return (current_tail[0] + 1, current_tail[1])
        else:
            return (current_tail[0] - 1, current_tail[1])
    elif abs(y_diff) == 2 and x_diff == 0:
        if y_diff > 0:
            return (current_tail[0], current_tail[1] + 1)
        else:
            return (current_tail[0], current_tail[1] - 1)
    elif (abs(x_diff) == 2 and abs(y_diff) == 1) or (abs(x_diff) == 1 and abs(y_diff) == 2) \
            or (abs(x_diff) == 2 and abs(y_diff) == 2):
        if x_diff > 0 and y_diff > 0:
            return (current_tail[0] + 1, current_tail[1] + 1)
        elif x_diff < 0 and y_diff > 0:
            return (current_tail[0] - 1, current_tail[1] + 1)
        elif x_diff > 0 and y_diff < 0:
            return (current_tail[0] + 1, current_tail[1] - 1)
        else:
            return (current_tail[0] - 1, current_tail[1] - 1)
    else:
        return (99, 99)


def direction(x, y, dir, step):
    if dir == 'U':
        return [(x, y1) for y1 in range(y + 1, y + 1 + step)]
    elif dir == 'D':
        return [(x, y1) for y1 in range(y - 1, y - 1 - step, -1)]
    elif dir == 'R':
        return [(x1, y) for x1 in range(x + 1, x + 1 + step)]
    else:
        return [(x1, y) for x1 in range(x - 1, x - 1 - step, -1)]


start_time = time.time()
steps = read_file('input_day9.txt')
hc = head_coordinates(steps)
print('1st part answer: ' + str(tail_coordinates(hc)[0]))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
coord = hc
for i in range(0, 9):
    n, coord = tail_coordinates(coord)
print('2nd part answer: ' + str(n))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
