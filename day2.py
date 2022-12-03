import string
import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    l = []
    for i in lines:
        i.split(' ')
        l.append([i[0], i[2]])
    return l


def game_outcome(player_1, player_2, part):
    if part == 1:
        alphabet = list(string.ascii_uppercase)
        player_2_updated = alphabet[(alphabet.index(player_2)+3)%26]
    else:
        player_2_updated = player_2
    game = [player_1, player_2_updated]
    if player_1==player_2_updated:
        return [3,3]
    elif game == ['A', 'C'] or game == ['C', 'B'] or game == ['B', 'A']:
        return [6,0]
    else:
        return [0,6]


def points(figure):
    if figure in ['A', 'X']:
        return 1
    elif figure in ['B', 'Y']:
        return 2
    else:
        return 3


def which_to_play(player_1, outcome):
    order = ['A', 'C', 'B']
    ind = order.index(player_1)
    forward = order[(ind+1)%3]
    backward = order[ind-1]
    if outcome == 'Y':
        return player_1
    elif outcome == 'Z':
        return backward
    else:
        return forward


start_time = time.time()
lines = read_file('input_day2.txt')
player_1_points = 0
player_2_points = 0
for i in lines:
    player_1 = i[0]
    player_2 = i[1]
    g = game_outcome(player_1, player_2, 1)
    player_1_points += g[0]+points(player_1)
    player_2_points += g[1]+points(player_2)
print('1st part answer: '+ str(player_2_points))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
player_1_points = 0
player_2_points = 0
for i in lines:
    player_1 = i[0]
    player_2 = which_to_play(player_1, i[1])
    g = game_outcome(player_1, player_2, 2)
    player_1_points += g[0]+points(player_1)
    player_2_points += g[1]+points(player_2)
print('2nd part answer: ' + str(player_2_points))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))