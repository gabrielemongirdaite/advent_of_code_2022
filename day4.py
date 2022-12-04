import time


def read_file(file_name):
    text_file = open(file_name, "r")
    line = text_file.read().split('\n')
    lst = []
    for ind in line:
        j = ind.split(',')
        m1 = []
        for k in j:
            m = k.split('-')
            m1.append(m)
        lst.append(m1)
    data = []
    for n in lst:
        data.append([range(int(n[0][0]), int(n[0][1])+1), range(int(n[1][0]), int(n[1][1])+1)])
    return data


def check_two_ranges(range_1, range_2):
    if set(range_1).issubset(range_2) or set(range_2).issubset(range_1):
        return 1
    else:
        return 0


def check_two_ranges_part_2(range_1, range_2):
    if list(set(range_1).intersection(set(range_2))):
        return 1
    else:
        return 0


start_time = time.time()
lines = read_file('input_day4.txt')
result = 0
for i in lines:
    result += check_two_ranges(i[0], i[1])
print('1st part answer: '+ str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
result2 = 0
for i in lines:
    result2 += check_two_ranges_part_2(i[0], i[1])
print('2nd part answer: '+ str(result2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))