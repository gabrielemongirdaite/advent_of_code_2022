import time
import re
import itertools


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            ln = []
            for i in line.split(' -> '):
                ln.append([int(s) for s in re.findall(r'\b\d+\b', i)])
            lines.append(ln)
    return lines


def find_rocks(rocks_coordinates):
    coordinates = []
    for rock in rocks_coordinates:
        coordinate = []
        for ind, i in enumerate(rock):
            if ind + 1 == len(rock):
                break
            else:
                if i[0] == rock[ind + 1][0]:
                    for k in range(min(i[1], rock[ind + 1][1]), max(i[1], rock[ind + 1][1]) + 1):
                        coordinate.append([i[0], k])
                else:
                    for k in range(min(i[0], rock[ind + 1][0]), max(i[0], rock[ind + 1][0]) + 1):
                        coordinate.append([k, i[1]])
        coordinate.sort()
        coordinate = list(k for k, _ in itertools.groupby(coordinate))
        coordinates.extend(coordinate)
    return coordinates


def sand_direction(start_point, coordinates):
    if [start_point[0], start_point[1] + 1] not in coordinates:
        return [start_point[0], start_point[1] + 1]
    else:
        if [start_point[0] - 1, start_point[1] + 1] not in coordinates:
            return [start_point[0] - 1, start_point[1] + 1]
        else:
            if [start_point[0] + 1, start_point[1] + 1] not in coordinates:
                return [start_point[0] + 1, start_point[1] + 1]
            else:
                return [-1, -1]


def sand_movement_part_1(coordinates):
    steps = [0]
    cnt = 0
    while max(steps) < max_steps:
        step = 0
        start_point = [500, 0]
        while step < max_steps and start_point != [-1, -1]:
            start_point = sand_direction(start_point, coordinates)
            step += 1
            if start_point != [-1, -1]:
                save_point = start_point
        coordinates.append(save_point)
        steps.append(step)
        cnt += 1
    return cnt - 1


def sand_movement_part_2(coordinates):
    max_line_at = max([i[1] for i in coordinates]) + 1
    cnt = 0
    while [500, 0] not in coordinates:
        step = 0
        start_point = [500, 0]
        while start_point[1] < max_line_at and start_point != [-1, -1]:
            start_point = sand_direction(start_point, coordinates)
            if step == 0 and start_point == [-1, -1]:
                save_point = [500, 0]
            step += 1
            if start_point != [-1, -1]:
                save_point = start_point
        coordinates.append(save_point)
        cnt += 1
    return cnt


start_time = time.time()
rocks = read_file("input_day14.txt")
rocks_coordinates = find_rocks(rocks)
rocks_coordinates_2 = rocks_coordinates.copy()
max_steps = max([i[1] for i in rocks_coordinates]) + 1
print('1st part answer: ' + str(sand_movement_part_1(rocks_coordinates)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

# takes forever
start_time = time.time()
print('2nd part answer: ' + str(sand_movement_part_2(rocks_coordinates_2)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
