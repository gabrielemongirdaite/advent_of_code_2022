import time
import re


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    all_dirs = list(set([x.split(" ")[1] for x in lines if x.split(" ")[0] == 'dir']))
    # some folders have the same names, thus this part of the code adds underscore + number for repeated names
    for dirs in all_dirs:
        indices_dir = [i for i, x in enumerate(lines) if x == "dir " + dirs]
        indices_cd = [i for i, x in enumerate(lines) if x == "$ cd " + dirs]
        if len(indices_dir) > 1:
            for ind, i in enumerate(indices_dir):
                lines[i] = "dir " + dirs + "_" + str(ind)
            elements = []
            all_indices = [i for i, x in enumerate(indices_cd)]
            for ind, i in enumerate(indices_cd):
                try:
                    element = [y for y, x in enumerate(indices_dir) if x < i and i < indices_dir[y + 1]]
                    all_indices.remove(element[0])
                    elements.append(element[0])
                except:
                    elements.append(all_indices[0])
                    all_indices.pop(0)
            for ind, i in enumerate(elements):
                lines[indices_cd[ind]] = "$ cd " + dirs + "_" + str(i)
    return lines


start_time = time.time()
lst = read_file("input_day7.txt")
dict = {}
i = 0
while i < len(lst) - 1:
    is_cd = 1 if '$ cd ' in lst[i] else 0
    is_ls = 1 if '$ ls' in lst[i] else 0
    if is_cd == 1:
        key = lst[i].split(' ')[2]
        i += 1
    if is_ls == 1:
        is_cd = 0
        i += 1
        values = []
        while is_cd == 0 and i + 1 <= len(lst):
            n = re.findall(r'\b\d+\b', lst[i])
            values.append(n[0] if n != [] else lst[i].split(' ')[1])
            i += 1
            try:
                is_cd = 1 if '$ cd ' in lst[i] else 0
            except:
                pass
        dict[key] = values

dict2 = {}
dict_copy = dict.copy()

while len(dict2) != len(dict):
    for i in dict_copy:
        try:
            v = sum([int(k) for k in dict_copy[i]])
            dict2[i] = v
            for j in dict_copy:
                if i in dict_copy[j]:
                    dict_copy[j] = [str(v) if x == i else x for x in dict_copy[j]]
        except:
            pass

result = 0
for i in dict2:
    if dict2[i] <= 100000:
        result += dict2[i]
print('1st part answer: '+ str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
outer_dir = dict2['/']
unused_space = 70000000 - outer_dir
additional_required_space = 30000000 - unused_space
to_delete = []
for i in dict2:
    if dict2[i] >= additional_required_space:
        to_delete.append(dict2[i])
print('2nd part answer: ' + str(min(to_delete)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))

