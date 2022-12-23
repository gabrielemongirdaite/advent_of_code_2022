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


def find_first_not_empty_x_right(y, map):
    return min(map[y].index('.'), map[y].index('#'))


def find_first_not_empty_x_left(y, map):
    return max(map[y].rfind('.'), map[y].rfind('#'))


def find_first_not_empty_y_above(x, map):
    y_max = len(map) - 1
    for i in range(y_max, -1, -1):
        if map[i][x] == '.' or map[i][x] == '#':
            return i


def find_first_not_empty_y_below(x, map):
    y_max = len(map) - 1
    for i in range(0, y_max):
        if map[i][x] == '.' or map[i][x] == '#':
            return i


def go_steps(x, y, current_direction, new_direction, step, map):
    direction = define_direction(current_direction, new_direction)
    i = 0
    figure = '.'
    new_x = x
    new_y = y
    while i <= step and figure != '#':
        if direction == '>':
            new_x_temp = new_x + 1 if new_x + 1 < len(map[0]) and map[new_y][new_x + 1] != ' ' \
                else find_first_not_empty_x_right(y, map)
            if map[new_y][new_x_temp] != '#' and i + 1 <= step:
                new_x = new_x_temp
        elif direction == '<':
            new_x_temp = new_x - 1 if new_x - 1 >= 0 and map[new_y][new_x - 1] != ' ' \
                else find_first_not_empty_x_left(y, map)
            if map[new_y][new_x_temp] != '#' and i + 1 <= step:
                new_x = new_x_temp
        elif direction == '^':
            new_y_temp = new_y - 1 if new_y - 1 >= 0 and map[new_y - 1][new_x] != ' ' \
                else find_first_not_empty_y_above(x, map)
            if map[new_y_temp][new_x] != '#' and i + 1 <= step:
                new_y = new_y_temp
        else:
            new_y_temp = new_y + 1 if new_y + 1 < len(map) and map[new_y + 1][new_x] != ' ' \
                else find_first_not_empty_y_below(x, map)
            if map[new_y_temp][new_x] != '#' and i + 1 <= step:
                new_y = new_y_temp
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

print((start_x + 1) * 4 + (
            start_y + 1) * 1000 +
      2 if start_direction == '<' else 0 if start_direction == '>' else 1 if start_direction == 'v' else 3)
