import copy


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    lines = [(ind, int(i)) for ind, i in enumerate(lines)]
    return lines



order = read_file('input_day20.txt')
lst = copy.deepcopy(order)


def mixing(order, lst_f, key):
    for i in order:
        ind = lst_f.index((i[0], i[1] * key))
        ln = len(order)
        if i[1] >= 0:
            ni = (i[1] * key) % (ln-1)
            new_ind = ind + ni
            ind_abs = new_ind % ln
            if ind > ind_abs:
                ind_abs += 1
            div = ni // ln
            lst_f.pop(ind)
            # print(ind_abs + div, ind_abs, div)
            # lst_f.insert(ind_abs_positive(ind, ln, ind_abs + div) if ind_abs + div >= ln else ind_abs + div,
            #              (i[0], i[1] * key))
            lst_f.insert(ind_abs + div, (i[0], i[1] * key))
        else:
            ni = abs(i[1] * key) % (ln-1)
            new_ind = ind - ni - 1
            if new_ind <= 0:
                ind_abs_tmp = abs(new_ind) % ln
                if ind_abs_tmp == 0:
                    ind_abs = 0
                else:
                    ind_abs = ln - ind_abs_tmp
                if ind < ind_abs:
                    ind_abs -= 1
                div = (ni + 1) // ln
                lst_f.pop(ind)
                lst_f.insert(ind_abs - div + 1, (i[0], i[1] * key))
            else:
                ind_abs = new_ind + 1
                lst_f.pop(ind)
                lst_f.insert(ind_abs, (i[0], i[1] * key))
    return lst_f


zero = [i[0] for i in order if i[1] == 0][0]

lst_part_1 = mixing(order, lst, 1)
result = lst_part_1[(lst_part_1.index((zero, 0)) + 1000) % len(order)][1] + \
         lst_part_1[(lst_part_1.index((zero, 0)) + 2000) % len(order)][1] + \
         lst_part_1[(lst_part_1.index((zero, 0)) + 3000) % len(order)][1]
print(result)

lst2 = copy.deepcopy(order)
lst2 = [(i[0], i[1] * 811589153) for i in lst2]
for i in range(0, 10):
    lst2 = mixing(order, lst2, 811589153)

result = lst2[(lst2.index((zero, 0)) + 1000) % len(order)][1] + \
         lst2[(lst2.index((zero, 0)) + 2000) % len(order)][1] + \
         lst2[(lst2.index((zero, 0)) + 3000) % len(order)][1]
print(result)
