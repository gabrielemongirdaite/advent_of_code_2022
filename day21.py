import re
import operator
import copy
import numbers
from sympy import symbols, solve


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    dct_num = {}
    dct_op = {}
    for i in lines:
        monkey = i.split(': ')[0]
        num = [int(s) for s in re.findall(r'\b\d+\b', i)]
        if num != []:
            dct_num[monkey] = num[0]
        else:
            op_sign = i.split(': ')[1].split(' ')[1]
            if op_sign == '*':
                op = operator.mul
            elif op_sign == '+':
                op = operator.add
            elif op_sign == '-':
                op = operator.sub
            else:
                op = operator.truediv
            dct_op[monkey] = [op, i.split(': ')[1].split(' ')[0], i.split(': ')[1].split(' ')[2]]
    return dct_num, dct_op


def num_yelling(stop_time, dct_operations, dct_numbers):
    while len(dct_operations) != stop_time:
        dct_op_copy = copy.deepcopy(dct_operations)
        for i in dct_op_copy:
            if isinstance(dct_operations[i][1], numbers.Number) and isinstance(dct_operations[i][2], numbers.Number):
                answer = dct_operations[i][0](dct_operations[i][1], dct_operations[i][2])
                dct_numbers[i] = answer
                del dct_operations[i]

            try:
                for ind, j in enumerate(dct_operations[i][1:]):
                    try:
                        num = dct_numbers[j]
                        if ind == 0:
                            dct_operations[i] = [dct_operations[i][0], num, dct_operations[i][2]]
                        else:
                            dct_operations[i] = [dct_operations[i][0], dct_operations[i][1], num]
                    except:
                        pass
            except:
                pass
    return dct_operations, dct_numbers

dct_num = read_file('input_day21.txt')[0]
dct_op = read_file('input_day21.txt')[1]

print(num_yelling(0, dct_op, dct_num)[1]['root'])


dct_num = read_file('input_day21.txt')[0]
del dct_num['humn']
dct_op = read_file('input_day21.txt')[1]
dct_op, dct_num = num_yelling(71, dct_op, dct_num)

dct_op_copy = copy.deepcopy(dct_op)
for i in dct_op_copy:
    try:
        for ind, j in enumerate(dct_op[i][1:]):
            try:
                num = dct_num[j]
                if ind == 0:
                    dct_op[i] = [dct_op[i][0], num, dct_op[i][2]]
                else:
                    dct_op[i] = [dct_op[i][0], dct_op[i][1], num]
            except:
                pass
    except:
        pass

humn = symbols('humn')
expr = humn - 173.0
monkey = 'mcmz'
while monkey != 'root':
    num = 1 if isinstance(dct_op[monkey][1], numbers.Number) else 2
    if dct_op[monkey][0] == operator.truediv:
        if num == 1:
            expr = dct_op[monkey][1] / expr
        else:
            expr = expr / dct_op[monkey][2]
    elif dct_op[monkey][0] == operator.sub:
        if num == 1:
            expr = dct_op[monkey][1] - expr
        else:
            expr = expr - dct_op[monkey][2]
    elif dct_op[monkey][0] == operator.add:
        expr += dct_op[monkey][num]
    else:
        expr *= dct_op[monkey][num]
    for i in dct_op:
        if dct_op[i][1] == monkey or dct_op[i][2] == monkey:
            monkey = i
            break

print(dct_op['root'])
print(solve(expr - 13439547545467))
