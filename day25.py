def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def convert_snafu_to_decimal(snafu):
    result = 0
    for ind, i in enumerate(snafu[::-1]):
        if i == "=":
            result += -2 * 5 ** ind
        elif i == '-':
            result += -1 * 5 ** ind
        else:
            result += int(i) * 5 ** ind
    return result


def convert_decimal_to_snafu(dec):
    power = 0
    while dec >= 2 * 5 ** power:
        power += 1
    ind = 0
    powers = []
    for i in range(power, -1, -1):
        min_tmp = dec
        for j in range(2, -3, -1):
            if ind == 0:
                if abs(j * 5 ** i - dec) <= min_tmp:
                    min_tmp = abs(j * 5 ** i - dec)
                    power_tmp = (i, j)
            else:
                current_number = 0
                for k in powers:
                    current_number += k[1] * 5 ** k[0]
                if i == 0:
                    if abs(current_number + j * 5 ** i - dec) == 0:
                        powers.append((i, j))
                        break
                else:
                    if abs(current_number + j * 5 ** i - dec) <= min_tmp:
                        min_tmp = abs(current_number + j * 5 ** i - dec)
                        power_tmp = (i, j)
        if powers == []:
            powers.append(power_tmp)
        elif power_tmp!= powers[-1]:
            powers.append(power_tmp)
        ind += 1

    return  powers


snafus = read_file('input_day25.txt')
r = 0
for i in snafus:
    r += convert_snafu_to_decimal(i)

print(r)

powers = convert_decimal_to_snafu(28061203326175)

r2 = ''
for i in powers[0:20]:
    if i[1] == -2:
        r2 += '='
    elif i[1] == -1:
        r2 += '-'
    else:
        r2 += str(i[1])

print(r2)
