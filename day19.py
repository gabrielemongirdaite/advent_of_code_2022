import itertools
import re


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace('\n', '')
            lines.append([int(s) for s in re.findall(r'\b\d+\b', line)])
    return lines


def one_step(current_states, blueprint):
    new_states = []
    for state in current_states:
        for i in range(0, 5):
            ore = state[0]
            clay = state[1]
            obsidian = state[2]
            geode = state[3]
            ore_robot = state[4]
            clay_robot = state[5]
            obsidian_robot = state[6]
            geode_robot = state[7]
            if i == 0:  # not building any robots
                ore += ore_robot
                clay += clay_robot
                obsidian += obsidian_robot
                geode += geode_robot
                new_states.append((ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot))
            elif i == 1 and ore >= blueprint[5] and obsidian >= blueprint[6]:
                ore -= blueprint[5]
                obsidian -= blueprint[6]
                ore += ore_robot
                clay += clay_robot
                obsidian += obsidian_robot
                geode += geode_robot
                geode_robot += 1
                new_states.append((ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot))
                break
            elif i == 2 and ore >= blueprint[3] and clay >= blueprint[4]:
                ore -= blueprint[3]
                clay -= blueprint[4]
                ore += ore_robot
                clay += clay_robot
                obsidian += obsidian_robot
                geode += geode_robot
                obsidian_robot += 1
                new_states.append((ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot))
                break
            elif i == 3 and ore >= blueprint[2]:  # building clay robot
                ore -= blueprint[2]
                ore += ore_robot
                clay += clay_robot
                obsidian += obsidian_robot
                geode += geode_robot
                clay_robot += 1
                new_states.append((ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot))
            elif i == 4 and ore >= blueprint[1]:  # building ore robot
                ore -= blueprint[1]
                ore += ore_robot
                clay += clay_robot
                obsidian += obsidian_robot
                geode += geode_robot
                ore_robot += 1
                new_states.append((ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot))
    new_states.sort()
    new_states = (list(k for k, _ in itertools.groupby(new_states)))
    return new_states


blueprints = read_file('input_day19.txt')

# obviously not an optimal solution
result = 0
for ind, i in enumerate(blueprints):
    initial_state = [(0, 0, 0, 0, 1, 0, 0, 0)]
    for k in range(0, 24):
        initial_state = one_step(initial_state, i)
        print(ind, k)

    geodes = []
    for g in initial_state:
        geodes.append(g[3])

    result += max(geodes)*i[0]

print(result)

result = 1
for ind, i in enumerate(blueprints[0:3]):
    initial_state = [(0, 0, 0, 0, 1, 0, 0, 0)]
    for k in range(0, 32):
        initial_state = one_step(initial_state, i)
        print(ind, k)

    geodes = []
    for g in initial_state:
        geodes.append(g[3])

    result *= max(geodes)

print(result)