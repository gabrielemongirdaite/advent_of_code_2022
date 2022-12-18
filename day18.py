import time
import re


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            lines.append([int(s) for s in re.findall(r'\b\d+\b', line)])
    return lines


def find_all_adjacant_cubes(cube):
    x = cube[0]
    y = cube[1]
    z = cube[2]
    adjacant_cubes = [[x - 1, y, z], [x + 1, y, z], [x, y - 1, z], [x, y + 1, z], [x, y, z - 1], [x, y, z + 1]]
    return adjacant_cubes


def check_x(cube, all_cubes, min_x, max_x):
    x = cube[0]
    y = cube[1]
    z = cube[2]
    answer = []
    for i in range(x, max_x + 1):
        if [i, y, z] in all_cubes:
            answer.append([i, y, z])
            break
    for i in range(x, min_x - 1, -1):
        if [i, y, z] in all_cubes:
            answer.append([i, y, z])
            break
    return len(answer), answer


def check_y(cube, all_cubes, min_y, max_y):
    x = cube[0]
    y = cube[1]
    z = cube[2]
    answer = []
    for i in range(y, max_y + 1):
        if [x, i, z] in all_cubes:
            answer.append([x, i, z])
            break
    for i in range(y, min_y - 1, -1):
        if [x, i, z] in all_cubes:
            answer.append([x, i, z])
            break
    return len(answer), answer


def check_z(cube, all_cubes, min_z, max_z):
    x = cube[0]
    y = cube[1]
    z = cube[2]
    answer = []
    for i in range(z, max_z + 1):
        if [x, y, i] in all_cubes:
            answer.append([x, y, i])
            break
    for i in range(z, min_z - 1, -1):
        if [x, y, i] in all_cubes:
            answer.append([x, y, i])
            break
    return len(answer), answer


start_time = time.time()
cubes = read_file('input_day18.txt')

all_cubes = []
for i in cubes:
    all_cubes.extend(find_all_adjacant_cubes(i))

for i in cubes:
    all_cubes = list(filter(lambda a: a != i, all_cubes))

print('1st part answer: ' + str(len(all_cubes)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
x = []
y = []
z = []
for i in cubes:
    x.append(i[0])
    y.append(i[1])
    z.append(i[2])

x.sort()
y.sort()
z.sort()

x_min, x_max = x[0], x[-1]
y_min, y_max = y[0], y[-1]
z_min, z_max = z[0], z[-1]

missing_cubes = []
for x in range(x_min + 1, x_max):
    for y in range(y_min + 1, y_max):
        for z in range(z_min + 1, z_max):
            c = [x, y, z]
            cx, cx1 = check_x(c, cubes, x_min, x_max)
            cy, cy1 = check_y(c, cubes, y_min, y_max)
            cz, cz1 = check_z(c, cubes, z_min, z_max)
            if c not in cubes and cx == 2 and cy == 2 and cz == 2:
                missing_cubes.append([x, y, z])

# if there is a path from an adjacent cell, then it shouldn't be considered
remove_missing = []
for i in missing_cubes:
    adjecent = find_all_adjacant_cubes(i)
    d = 0
    for j in adjecent:
        c = [j[0], j[1], j[2]]
        cx, cx1 = check_x(c, cubes, x_min, x_max)
        cy, cy1 = check_y(c, cubes, y_min, y_max)
        cz, cz1 = check_z(c, cubes, z_min, z_max)
        if cx == 2 and cy == 2 and cz == 2:
            d += 1
    if d != 6:
        remove_missing.append(i)

for i in remove_missing:
    missing_cubes = [j for j in missing_cubes if j != i]

all_cubes_part_2 = []
cubes = cubes + missing_cubes

for i in cubes:
    all_cubes_part_2.extend(find_all_adjacant_cubes(i))

for i in cubes:
    all_cubes_part_2 = list(filter(lambda a: a != i, all_cubes_part_2))

print('2nd part answer: ' + str(len(all_cubes_part_2)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
