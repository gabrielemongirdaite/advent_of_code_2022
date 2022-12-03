import heapq
import time

def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines

def calories(lines):
    results = []
    i = 0
    while i < len(lines):
        j = i
        result = 0
        while lines[j] != '':
            result += int(lines[j])
            j += 1
            i += 1
        results.append(result)
        i += 1
    return results

start_time = time.time()
lines = read_file('input_day1.txt')
r1 = calories(lines)
print('1st part answer: '+ str(max(r1)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
r2 = sum(heapq.nlargest(3, r1))
print('2nd part answer: ' + str(r2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))