import sys
import re
import math
import time

def solve(file):
    data = open(file, 'r').readlines()

    network = {}
    curr_nodes = []
    instructions = data[0].strip()
    for line in data[2:]:
        starting_node = re.search('[0-9A-Z]{2}A(?= = )', line)
        if starting_node != None: curr_nodes.append(starting_node.group())
        path = list(re.findall('[0-9A-Z]{3}', line))
        network[path[0]] = (path[1], path[2])

    total_steps = []
    for node in curr_nodes:
        instr_idx = 0
        steps = 0
        while node[2] != 'Z':
            if instr_idx == len(instructions):
                instr_idx = 0

            if instructions[instr_idx] == 'R':
                node = network[node][1]
            else:
                node = network[node][0]

            instr_idx += 1
            steps += 1
        total_steps.append(steps)

    return math.lcm(*total_steps)

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))