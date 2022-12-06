import time
import re


def read_file(file_name):
    with open(file_name, 'r') as reader:
        text = reader.read()
    list_of_strings = [''.join(chars) for chars in zip(*text.splitlines())]

    buckets = [x.replace('[', '').replace(']', '').replace('n', '')\
                    .replace('\\', '').replace(' ', '') for x in list_of_strings]
    buckets = [x for x in buckets if x != '']
    return buckets


def read_moves(file_name):
    text_file = open(file_name, "r")
    line = text_file.read().split('\n')
    moves = []
    for i in line:
        moves.append([int(s) for s in re.findall(r'\b\d+\b', i)])
    return moves


def move_cranes(lst, from_bucket, to_bucket):
    crane = lst[from_bucket-1][0]
    lst[from_bucket-1] = lst[from_bucket-1][1:]
    lst[to_bucket-1] = crane + lst[to_bucket-1]
    return lst


def move_cranes_part_2(lst, n, from_bucket, to_bucket):
    crane = lst[from_bucket-1][0:n]
    lst[from_bucket-1] = lst[from_bucket-1][n:]
    lst[to_bucket-1] = crane + lst[to_bucket-1]
    return lst


start_time = time.time()
lines = read_file('input_day5_buckets.txt')
moves = read_moves('input_day5_moves.txt')
lst = lines.copy()
for i in moves:
    steps = i[0]
    while steps>=1:
        lst = move_cranes(lst, i[1], i[2])
        steps -= 1
result = ''
for i in lst:
    result += i[0]
print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
lst2 = lines.copy()
for i in moves:
    lst2 = move_cranes_part_2(lst2, i[0], i[1], i[2])
result2 = ''
for i in lst2:
    result2 += i[0]
print('2nd part answer: ' + str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))