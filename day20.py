import copy


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    lines = [(ind, int(i)) for ind, i in enumerate(lines)]
    return lines


order = read_file('input_day20.txt')
lst = copy.deepcopy(order)

for i in order:
    ind = lst.index(i)
    ln = len(order)
    if i[1] >= 0:
        new_ind = ind + i[1]
        ind_abs = new_ind % ln
        div = i[1] // ln
        lst.pop(ind)
        if ind > ind_abs:
            ind_abs += 1
        lst.insert(ind_abs + div, i)
    else:
        new_ind = ind + i[1] - 1
        if new_ind <= 0:
            ind_abs_tmp = abs(new_ind) % ln
            if ind_abs_tmp == 0:
                ind_abs = 0
            else:
                ind_abs = ln - ind_abs_tmp
            div = (abs(i[1]) + 1) // ln
            lst.pop(ind)
            if ind < ind_abs:
                ind_abs -= 1
            lst.insert(ind_abs - div + 1, i)
        else:
            ind_abs = new_ind + 1
            lst.pop(ind)
            lst.insert(ind_abs, i)


zero = [i[0] for i in order if i[1] == 0][0]

print(lst[(lst.index((zero, 0)) + 1000) % len(order)][1], lst[(lst.index((zero, 0)) + 2000) % len(order)][1], lst[
    (lst.index((zero, 0)) + 3000) % len(order)][1])
result = lst[(lst.index((zero, 0)) + 1000) % len(order)][1] + lst[(lst.index((zero, 0)) + 2000) % len(order)][1] + lst[
    (lst.index((zero, 0)) + 3000) % len(order)][1]
print(result)
