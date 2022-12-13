import json
import time
import itertools


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    lines = [i for i in lines if i != '']
    data = []
    for i in lines:
        data.append(json.loads(i))
    return data


def convert_to_list(i, j):
    if type(i) is int and type(j) is list:
        i = [i]
    if type(j) is int and type(i) is list:
        j = [j]
    return i, j


def couple_comparison(lst_1, lst_2):
    if type(lst_1) is int or lst_1 == []:
        lst_1 = [lst_1]
    if type(lst_2) is int or lst_2 == []:
        lst_2 = [lst_2]
    for i, j in itertools.zip_longest(lst_1, lst_2):
        i, j = convert_to_list(i, j)
        if i != j:
            if type(i) is int and type(j) is int:
                if i < j:
                    return True
                elif i > j:
                    return False
            elif j is None and i is not None:
                return False
            elif i is None and j is not None:
                return True
            elif j == [] and i != []:
                return False
            elif j != [] and i == []:
                return True
            else:
                i, j = convert_to_list(i, j)
                return couple_comparison(i, j)


def loop_and_compare(data1, data2):
    i = None
    while i is None:
        for j in range(0, len(data1) + 1):
            try:
                i = couple_comparison(data1[j], data2[j])
            except:
                if len(data1) <= j < len(data2):
                    i = True
                else:
                    i = False
            if i is not None:
                break
    return i


start_time = time.time()
data = read_file('input_day13.txt')

k = 0
result = 0
while k < len(data):
    i = loop_and_compare(data[k], data[k+1])
    if i:
        result += (k + 2) // 2
    k += 2

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
new_data = data
new_data.append([[2]])
new_data.append([[6]])
results = {}
l_new_data = len(new_data)
for ind, c1 in enumerate(new_data):
    result = 0
    for c2 in new_data:
        i = loop_and_compare(c1, c2)
        if i:
            result += 1
    results[ind] = l_new_data - result

print('2nd part answer: ' + str(results[l_new_data - 1] * results[l_new_data - 2]))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
