def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def find_elfs(map):
    elfs = []
    for y, i in enumerate(map):
        for x, j in enumerate(i):

            if map[y][x] == '#':
                elfs.append((x, y))
    return elfs


def all_directions(elf):
    x = elf[0]
    y = elf[1]
    north = [(x, y - 1), (x - 1, y - 1), (x + 1, y - 1)]
    south = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
    east = [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1)]
    west = [(x - 1, y), (x - 1, y - 1), (x - 1, y + 1)]
    return north, south, east, west


def move_elfs(elfs, directions):
    possible_moves = []
    not_moved = 0
    for i in elfs:
        n, s, e, w = all_directions(i)
        if list(set(elfs).intersection(set(n + s + e + w))) == []:
            not_moved += 1
            possible_moves.append(i)
        elif directions == ['N', 'S', 'W', 'E']:
            if list(set(elfs).intersection(set(n))) == []:
                possible_moves.append(n[0])
            elif list(set(elfs).intersection(set(s))) == []:
                possible_moves.append(s[0])
            elif list(set(elfs).intersection(set(w))) == []:
                possible_moves.append(w[0])
            elif list(set(elfs).intersection(set(e))) == []:
                possible_moves.append(e[0])
            else:
                possible_moves.append(i)
        elif directions == ['S', 'W', 'E', 'N']:
            if list(set(elfs).intersection(set(s))) == []:
                possible_moves.append(s[0])
            elif list(set(elfs).intersection(set(w))) == []:
                possible_moves.append(w[0])
            elif list(set(elfs).intersection(set(e))) == []:
                possible_moves.append(e[0])
            elif list(set(elfs).intersection(set(n))) == []:
                possible_moves.append(n[0])
            else:
                possible_moves.append(i)
        elif directions == ['W', 'E', 'N', 'S']:
            if list(set(elfs).intersection(set(w))) == []:
                possible_moves.append(w[0])
            elif list(set(elfs).intersection(set(e))) == []:
                possible_moves.append(e[0])
            elif list(set(elfs).intersection(set(n))) == []:
                possible_moves.append(n[0])
            elif list(set(elfs).intersection(set(s))) == []:
                possible_moves.append(s[0])
            else:
                possible_moves.append(i)
        elif directions == ['E', 'N', 'S', 'W']:
            if list(set(elfs).intersection(set(e))) == []:
                possible_moves.append(e[0])
            elif list(set(elfs).intersection(set(n))) == []:
                possible_moves.append(n[0])
            elif list(set(elfs).intersection(set(s))) == []:
                possible_moves.append(s[0])
            elif list(set(elfs).intersection(set(w))) == []:
                possible_moves.append(w[0])
            else:
                possible_moves.append(i)
    new_elfs = []
    dir_first = directions[0]
    directions.pop(0)
    directions.insert(3, dir_first)
    if not_moved != len(elfs):
        for ind, i in enumerate(possible_moves):
            if possible_moves.count(i) == 1:
                new_elfs.append(i)
            else:
                new_elfs.append(elfs[ind])
    else:
        new_elfs = elfs
    return new_elfs, directions, not_moved


map = read_file('input_day23.txt')
elfs = find_elfs(map)
not_moved = 0
directions = ['N', 'S', 'W', 'E']
i = 1
while not_moved != len(elfs): # and i <= 10:
    elfs, directions, not_moved = move_elfs(elfs, directions)
    i += 1

print((max([i[0] for i in elfs]) - min([i[0] for i in elfs]) + 1) * (
            max([i[1] for i in elfs]) - min([i[1] for i in elfs]) + 1)
      -len(elfs))
print(i-1)
