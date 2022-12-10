import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    lst = []
    for i in lines:
        try:
            k = i.split(' ')
            lst.append([k[0], int(k[1])])
        except:
            lst.append([i])
    return lst


def combinations(instructions):
    X = 1
    cycle = 0
    combs = []
    for i in instructions:
        if i[0] == 'addx':
            for c in range(0, 2):
                cycle += 1
                if c == 1:
                    X += i[1]
                combs.append([cycle, X])

        else:
            for c in range(0, 1):
                cycle += 1
                combs.append([cycle, X])
    return combs, [[0, 1]] + combs


start_time = time.time()
instructions = read_file("input_day10.txt")
combinations, combinations_begin = combinations(instructions)
result = 0
for i in [19, 59, 99, 139, 179, 219]:
    result += [n[1] for n in combinations if n[0] == i][0] * (i + 1)
print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
print('2nd part answer: ' )
for i in range(0, 6):
    line = ''
    for j in range(40 * i, 40 * (i + 1)):
        sprite = [combinations_begin[j][1], combinations_begin[j][1] - 1, combinations_begin[j][1] + 1]
        if j - 40 * i in sprite:
            line += '#'
        else:
            line += '.'
    print(line)

print("--- %s seconds for 2nd part---" % (time.time() - start_time))
