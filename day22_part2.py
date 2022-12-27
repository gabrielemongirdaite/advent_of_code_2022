import copy


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def decode_directions(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    ln_1 = copy.deepcopy(lines[0])
    ln_1 = ln_1.replace('R', ':').replace('L', ':')
    steps = []
    directions = ['R']
    for i in ln_1.split(":"):
        steps.append(int(i))
    for i in lines[0]:
        if i == 'L' or i == 'R':
            directions.append(i)
    return steps, directions


def define_direction(current, new):
    if current == '>' and new == 'R':
        return 'v'
    elif current == '>' and new == 'L':
        return '^'
    elif current == '<' and new == 'R':
        return '^'
    elif current == '<' and new == 'L':
        return 'v'
    elif current == '^' and new == 'R':
        return '>'
    elif current == '^' and new == 'L':
        return '<'
    elif current == 'v' and new == 'R':
        return '<'
    elif current == 'v' and new == 'L':
        return '>'


def go_right(x, y):
    if x >= 149 and 0 <= y < 50:  # A
        x_new = 99
        y_new = (49 - y) + 100  # [100, 149]
        dir_new = '<'
        return x_new, y_new, dir_new
    elif x >= 99 and 50 <= y < 100:  # D
        x_new = 150 - (100 - y)  # [100, 149]
        y_new = 49
        dir_new = '^'
        return x_new, y_new, dir_new
    elif x >= 99 and 100 <= y < 150:  # E
        x_new = 149
        y_new = 149 - y  # [0,49]
        dir_new = '<'
        return x_new, y_new, dir_new
    elif x >= 49 and 150 <= y < 200:  # I
        x_new = 50 + (y - 150)  # [50, 99]
        y_new = 149
        dir_new = '^'
        return x_new, y_new, dir_new


def go_left(x, y):
    if x <= 51 and 0 <= y < 50:  # K
        x_new = 0
        y_new = (49 - y) + 100  # [100, 149]
        dir_new = '>'
        return x_new, y_new, dir_new
    elif x <= 51 and 50 <= y < 100:  # N
        x_new = 50 - (100 - y)  # [0, 49]
        y_new = 100
        dir_new = 'v'
        return x_new, y_new, dir_new
    elif x <= 1 and 100 <= y < 150:  # L
        x_new = 50
        y_new = (149 - y)  # [0, 49]
        dir_new = '>'
        return x_new, y_new, dir_new
    elif x <= 1 and 150 <= y < 200:  # H
        x_new = 100 - (200 - y)  # [50,99]
        y_new = 0
        dir_new = 'v'
        return x_new, y_new, dir_new


def go_up(x, y):
    if y <= 1 and 100 <= x < 150:  # C
        x_new = 50 - (150 - x)  # [0, 49]
        y_new = 199
        dir_new = '^'
        return x_new, y_new, dir_new
    elif y <= 1 and 50 <= x < 100:  # G
        x_new = 0
        y_new = 150 + (x - 50)  # [150, 199]
        dir_new = '>'
        return x_new, y_new, dir_new
    elif y <= 101 and 0 <= x < 50:  # M
        x_new = 50
        y_new = 50 + x  # [50, 99]
        dir_new = '>'
        return x_new, y_new, dir_new


def go_down(x, y):
    if y >= 49 and 100 <= x < 150:  # B
        x_new = 99
        y_new = 50 + (x - 100)  # [50, 99]
        dir_new = '<'
        return x_new, y_new, dir_new
    elif y >= 149 and 50 <= x < 100:  # J
        x_new = 49
        y_new = 150 + (x - 50)  # [150, 199]
        dir_new = '<'
        return x_new, y_new, dir_new
    elif y >= 199 and 0 <= x < 50:  # F
        x_new = 100 + x  # [100, 149]
        y_new = 0
        dir_new = 'v'
        return x_new, y_new, dir_new


def go_steps(x, y, current_direction, new_direction, step, map):
    direction = define_direction(current_direction, new_direction)
    i = 0
    figure = '.'
    new_x = x
    new_y = y
    while i <= step and figure != '#':
        if direction == '>':
            if new_x + 1 < len(map[0]) and map[new_y][new_x + 1] != ' ':
                new_x_temp = new_x + 1
                new_y_temp = new_y
                direction_tmp = direction
            else:
                new_x_temp, new_y_temp, direction_tmp = go_right(new_x, new_y)
            if map[new_y_temp][new_x_temp] != '#' and i + 1 <= step:
                new_x = new_x_temp
                new_y = new_y_temp
                direction = direction_tmp
        elif direction == '<':
            if new_x - 1 >= 0 and map[new_y][new_x - 1] != ' ':
                new_x_temp = new_x - 1
                new_y_temp = new_y
                direction_tmp = direction
            else:
                new_x_temp, new_y_temp, direction_tmp = go_left(new_x, new_y)
            if map[new_y_temp][new_x_temp] != '#' and i + 1 <= step:
                new_x = new_x_temp
                new_y = new_y_temp
                direction = direction_tmp
        elif direction == '^':
            if new_y - 1 >= 0 and map[new_y - 1][new_x] != ' ':
                new_x_temp = new_x
                new_y_temp = new_y - 1
                direction_tmp = direction
            else:
                new_x_temp, new_y_temp, direction_tmp = go_up(new_x, new_y)
            if map[new_y_temp][new_x_temp] != '#' and i + 1 <= step:
                new_x = new_x_temp
                new_y = new_y_temp
                direction = direction_tmp
        else:
            if new_y + 1 < len(map) and map[new_y + 1][new_x] != ' ':
                new_x_temp = new_x
                new_y_temp = new_y + 1
                direction_tmp = direction
            else:
                new_x_temp, new_y_temp, direction_tmp = go_down(new_x, new_y)
            if map[new_y_temp][new_x_temp] != '#' and i + 1 <= step:
                new_x = new_x_temp
                new_y = new_y_temp
                direction = direction_tmp
        i += 1
        figure = map[new_y][new_x]
    return new_x, new_y, direction


map = read_file('input_day22.txt')
steps, directions = decode_directions('input_day22_directions.txt')
for ind, i in enumerate(map):
    if len(i) != 150:
        map[ind] = map[ind] + ' ' * (150 - len(i))

start_x = 50
start_y = 0
start_direction = '^'

for ind, i in enumerate(steps):
    start_x, start_y, start_direction = go_steps(start_x, start_y, start_direction, directions[ind], i, map)

print(start_x, start_y, start_direction)
r1 = 2 if start_direction == '<' else 0 if start_direction == '>' else 1 if start_direction == 'v' else 3
r2 = (start_x + 1) * 4 + (start_y + 1) * 1000

print(r1+r2)
