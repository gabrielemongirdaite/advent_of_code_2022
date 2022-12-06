import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return list(lines[0]), lines[0]


def all_comb(lst, part_aoc):
    all_combinations = []
    if part_aoc == 1:
        marker = 3
    else:
        marker = 13
    for ind, i in enumerate(lst):
        step = 0
        comb = []
        while step <= marker and ind + step < len(lst):
            comb.append(lst[ind + step])
            step += 1
        all_combinations.append(comb)
    return all_combinations


def find_different_values(combinations, original_string, part_aoc):
    for i in combinations:
        if len(i) == len(set(i)):
            if part_aoc == 1:
                return original_string.index(''.join(i))+1+3
            else:
                return original_string.index(''.join(i)) + 1 + 13


start_time = time.time()
lst, original_string = read_file('input_day6.txt')
combinations = all_comb(lst, 1)
print('1st part answer: '+ str(find_different_values(combinations, original_string, 1)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
combinations2 = all_comb(lst, 2)
print('2nd part answer: ' + str(find_different_values(combinations2, original_string, 2)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))