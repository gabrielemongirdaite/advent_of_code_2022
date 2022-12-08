import time


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            ln = []
            for j in line:
                ln.extend(j)
            ln = [int(i) for i in ln]
            lines.append(ln)
    return lines


def above_dir(x, y, lst):
    above = []
    for i in range(x - 1, -1, -1):
        above.append(lst[i][y])
    return above


def below_dir(x, y, lst):
    heigth = len(lst)
    below = []
    for i in range(x + 1, heigth):
        below.append(lst[i][y])
    return below


def left_dir(x, y, lst):
    left = []
    for i in range(y - 1, -1, -1):
        left.append(lst[x][i])
    return left


def right_dir(x, y, lst):
    width = len(lst[0])
    right = []
    for i in range(y + 1, width):
        right.append(lst[x][i])
    return right


def count_lower_trees(direction, value):
    cnt_d = 0
    d = 1
    try:
        while value > direction[cnt_d] and cnt_d < len(direction) - 1:
            d += 1
            cnt_d += 1
    except:
        pass
    return d


def visible_trees(lst):
    s = 0
    score = []
    for x, i in enumerate(lst):
        for y, j in enumerate(i):
            above = above_dir(x, y, lst)
            left = left_dir(x, y, lst)
            below = below_dir(x, y, lst)
            right = right_dir(x, y, lst)
            if j > max(above if above != [] else [-1]) \
                    or j > max(below if below != [] else [-1]) \
                    or j > max(right if right != [] else [-1]) \
                    or j > max(left if left != [] else [-1]):
                s += 1
            a = count_lower_trees(above, j)
            b = count_lower_trees(below, j)
            l = count_lower_trees(left, j)
            r = count_lower_trees(right, j)
            score.append(r * l * a * b)
    return s, max(score)


start_time = time.time()
seq = read_file('input_day8.txt')
print('1st part answer: '+ str(visible_trees(seq)[0]))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
print('2nd part answer: ' + str(visible_trees(seq)[1]))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))