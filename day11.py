import time
import copy
import heapq
import operator
import re


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    lines = [x for x in lines if x != '']
    lst = [lines[x:x + 6] for x in range(0, len(lines) - 5, 6)]
    details = []
    for j in lst:
        detail = []
        for ind, i in enumerate(j):
            if ind == 2:
                if i.split(' ')[6] == '*':
                    detail.append([operator.mul, i.split(' ')[7]])
                else:
                    detail.append([operator.add, i.split(' ')[7]])
            else:
                detail.append([int(s) for s in re.findall(r'\b\d+\b', i)])
        detail.append([0])
        details.append(detail)

    return details


def worry_score(item, monkey_details, part, divisor=1):
    score = monkey_details[2][0](item, item if monkey_details[2][1] == 'old' else int(monkey_details[2][1]))
    if part == 1:
        score = score // 3
    else:
        score = score % divisor  # Chinese Remainder Theorem
    return score


def if_devisible(score, monkey_details):
    if score % monkey_details[3][0] == 0:
        return True
    else:
        return False


def monkey_activity(monkeys, times, part):
    divisor = 1
    if part == 2:
        for i in monkeys:
            divisor *= i[3][0]
    for k in range(0, times):
        for monkey_ind, i in enumerate(monkeys):
            for item in i[1]:
                new_item = worry_score(item, i, part, divisor)
                next_step = if_devisible(new_item, i)
                if next_step:
                    monkeys[i[4][0]][1].append(new_item)
                else:
                    monkeys[i[5][0]][1].append(new_item)
                monkeys[monkey_ind][6][0] += 1
            monkeys[monkey_ind][1] = []
    return monkeys


def results(monkeys):
    r = []
    for i in monkeys:
        r.append(i[6][0])
    return heapq.nlargest(2, r)[0] * heapq.nlargest(2, r)[1]


start_time = time.time()
monkeys_data = read_file('input_day11.txt')
monkeys_data_part1 = copy.deepcopy(monkeys_data)
print('1st part answer: ' + str(results(monkey_activity(monkeys_data_part1, 20, 1))))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
monkeys_data_part2 = copy.deepcopy(monkeys_data)
print('2nd part answer: ' + str(results(monkey_activity(monkeys_data_part2, 10000, 2))))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
