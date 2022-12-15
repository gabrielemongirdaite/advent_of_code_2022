import time
import re


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            ln = []
            for i in line.split(' -> '):
                ln.append([int(s) for s in re.findall(r'-?\d+', i)])
            lines.append(ln)
    return lines


def manhattan_distance(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    return x + y


def find_points_belonging_to_row(row_number, distance, x, y, part=1):
    if y - distance <= row_number <= y + distance:
        s = abs(y - row_number)
        if part == 1:
            points_in_row = range(x - (distance - s), x + (distance - s) + 1)
        else:
            points_in_row = range(max(x - (distance - s), 0), min(x + (distance - s) + 1, 4000001))
        return points_in_row


def find_border_points(x, y, distance):
    first = [(x - j - 1, y - (distance - j)) for j in range(0, distance + 1)]
    second = [(x - j - 1, y + (distance - j)) for j in range(0, distance + 1)]
    third = [(x + j + 1, y - (distance - j)) for j in range(0, distance + 1)]
    fourth = [(x + j + 1, y + (distance - j)) for j in range(0, distance + 1)]
    # border_points.extend([(x, y - distance - 1), (x, y - distance + 1)])
    return first, second, third, fourth


start_time = time.time()
points = read_file('input_day15.txt')
distances = []
for i in points:
    distances.append(manhattan_distance(i[0][0], i[0][1], i[0][2], i[0][3]))

result = []
sensors = []
beacons = []
row_of_interest = 2000000
for ind, i in enumerate(points):
    if i[0][1] == row_of_interest:
        sensors.append(i[0][0])
    if i[0][3] == row_of_interest:
        beacons.append(i[0][2])
    additional_points = find_points_belonging_to_row(row_of_interest, distances[ind], i[0][0], i[0][1])
    if additional_points is not None:
        result.extend(additional_points)
result = list(set(result))
print('1st part answer: ' + str(len([x for x in result if x not in beacons and x not in sensors])))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
border_1 = []
border_2 = []
border_3 = []
border_4 = []
for ind, i in enumerate(points):
    fi, s, t, fo = find_border_points(i[0][0], i[0][1], distances[ind])
    border_1.extend(fi)
    border_2.extend(s)
    border_3.extend(t)
    border_4.extend(fo)

p = list(set(border_1).intersection(set(border_2), set(border_3), set(border_4)))[0]
print('2nd part answer: ' + str(p[0]*4000000+p[1]))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))

