import string
import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def part_1_intersect(lines):
    intersect = []
    for i in lines:
        f = set(list(i[0:(len(i) // 2)]))
        s = set(list(i[(len(i) // 2):]))
        intersect.append(list(f.intersection(s))[0])
        print()
    return intersect


def part_2_intersect(lines):
    intersect = []
    lines_3 = [lines[i:i + 3] for i in range(0, len(lines), 3)]
    for i in lines_3:
        f = set(list(i[0]))
        s = set(list(i[1]))
        t = set(list(i[2]))
        intersect.append(list(f.intersection(s).intersection(t))[0])
    return intersect


def points(letter):
    upp = letter.isupper()
    l = letter.lower()
    ind = list(string.ascii_lowercase).index(l)+1
    if upp:
        return ind+26
    else:
        return ind


start_time = time.time()
lines = read_file('input_day3.txt')
r = 0
print(part_1_intersect(lines))
for j in part_1_intersect(lines):
    r += points(j)
print('1st part answer: '+ str(r))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
r2 = 0
for j in part_2_intersect(lines):
    r2 += points(j)
print('2nd part answer: ' + str(r2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))