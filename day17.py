import time
import itertools
import csv


def read_file(file_name):
    f = open(file_name, "r")
    return f.read()


def figure_one(y):
    return [(2, y + 3), (3, y + 3), (4, y + 3), (5, y + 3)]


def figure_two(y):
    return [(3, y + 3), (2, y + 4), (3, y + 4), (4, y + 4), (3, y + 5)]


def figure_three(y):
    return [(2, y + 3), (3, y + 3), (4, y + 3), (4, y + 4), (4, y + 5)]


def figure_four(y):
    return [(2, y + 3), (2, y + 4), (2, y + 5), (2, y + 6)]


def figure_five(y):
    return [(2, y + 3), (3, y + 3), (2, y + 4), (3, y + 4)]


def min_max_x_y(figure):
    y = [i[1] for i in figure]
    x = [i[0] for i in figure]
    return min(y), min(x), max(x), max(y)


def fall_down(current_rocks, directions, figure, full_directions):
    y_min = min_max_x_y(figure)[0]
    figure_bottom_row = [i for i in figure if i[1] == y_min]
    d = 0
    while sum([1 if i in current_rocks else 0 for i in figure_bottom_row]) == 0:
        try:
            direction = directions[d]
        except:
            direction = (directions + full_directions)[d]
        if direction == '>':
            possible_figure = [(i[0] + 1, i[1] + 1) for i in figure]
            if min_max_x_y(figure)[2] != 6 and sum([1 if i in current_rocks else 0 for i in possible_figure]) == 0:
                figure = [(i[0] + 1, i[1]) for i in figure]
        elif direction == '<':
            possible_figure = [(i[0] - 1, i[1] + 1) for i in figure]
            if min_max_x_y(figure)[1] != 0 and sum([1 if i in current_rocks else 0 for i in possible_figure]) == 0:
                figure = [(i[0] - 1, i[1]) for i in figure]
        d += 1
        if sum([1 if i in current_rocks else 0 for i in figure]) == 0:
            figure_new = [(i[0], i[1] - 1) for i in figure]
            figure = figure_new
        else:
            break

    figure_to_save = [(i[0], i[1] + 1) for i in figure]
    current_rocks.extend(figure_to_save)
    return current_rocks, d


def calculate_height(direction, number_figure, **kwargs):
    current_rocks = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]
    figure_cycle = kwargs.get('figure_cycle', None)
    d = 0
    for i in range(0, number_figure):
        figure = (i % 5) + 1
        y_max = min_max_x_y(current_rocks)[3]
        if figure == 1:
            current_rocks, d1 = fall_down(current_rocks, direction[d:], figure_one(y_max), direction)
            d += d1
        elif figure == 2:
            current_rocks, d1 = fall_down(current_rocks, direction[d:], figure_two(y_max), direction)
            d += d1
        elif figure == 3:
            current_rocks, d1 = fall_down(current_rocks, direction[d:], figure_three(y_max), direction)
            d += d1
        elif figure == 4:
            current_rocks, d1 = fall_down(current_rocks, direction[d:], figure_four(y_max), direction)
            d += d1
        elif figure == 5:
            current_rocks, d1 = fall_down(current_rocks, direction[d:], figure_five(y_max), direction)
            d += d1
        if d > len(direction):
            d = d % len(direction)
        current_rocks.sort()
        current_rocks = list(k for k, _ in itertools.groupby(current_rocks))
        if figure_cycle is not None:
            if sum([1 for i in current_rocks if i == (0, figure_cycle)]) + sum(
                    [1 for i in current_rocks if i == (3, figure_cycle)]) \
                    + sum([1 for i in current_rocks if i == (5, figure_cycle)]) == 3:
                break
    return max([i[1] for i in current_rocks]), current_rocks, i


start_time = time.time()
directions = read_file("input_day17.txt")

print('1st part answer: ' + str(calculate_height(directions, 2022)[0]))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
# to export data in excel to find cycles
rocks = calculate_height(directions, 3000)[1]  # 3000 is by error and trial method
rows = {}
for i in rocks:
    try:
        rows[i[1]].append(i[0])
    except:
        rows[i[1]] = [i[0]]

with open('dict.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in rows.items():
        writer.writerow([key, value])

# cycle: from row 1485 to 4237: 0, 3, 5 (in excel with countif function)
# let's find figures numbers

row_1 = calculate_height(directions, 3000, figure_cycle=1485)[2]
row_2 = calculate_height(directions, 3000, figure_cycle=4237)[2]
sum_1 = calculate_height(directions, row_1)[0]
sum_2 = calculate_height(directions, row_2)[0]
cycle_height = sum_2 - sum_1
cycle_n = row_2 - row_1
n = (1000000000000 - row_1) // cycle_n
row_3 = (1000000000000 - row_1) % cycle_n
sum_3 = calculate_height(directions, row_3+row_1)[0] - sum_1
print('2nd part answer: ' + str(cycle_height * n + sum_1 + sum_3))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))