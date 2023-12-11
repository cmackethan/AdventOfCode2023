import sys
import re
import time

def solve(file):
    data = open(file, 'r').readlines()

    network = {}
    instructions = data[0].strip()
    for line in data[2:]:
        line = list(re.findall('[A-Z]{3}', line))
        network[line[0]] = (line[1], line[2])

    curr_node = 'AAA'
    instr_idx = 0
    steps = 0
    while curr_node != 'ZZZ':
        if instr_idx == len(instructions):
            instr_idx = 0

        if instructions[instr_idx] == 'R':
            curr_node = network[curr_node][1]
        else:
            curr_node = network[curr_node][0]

        instr_idx += 1
        steps += 1

    return steps

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))