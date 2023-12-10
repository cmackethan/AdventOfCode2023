import sys
import re

def solve(file):
    with open(file, 'r') as data:
        times = parse(data.readline())
        distances = parse(data.readline())
        races = list(map(lambda x, y: (x, y), times, distances)) # -> (time, distance)

    total_num_ways = 1 # This assumes at least one race has a beatable record
    for i, (time, distance) in enumerate(races):
        num_ways = 0
        for j in range(1, time):
            if j * (time - j) > distance:
                num_ways += 1
        total_num_ways *= num_ways
    return total_num_ways

def parse(str):
    return list(map(int, re.search("[0-9].*", str).group().split()))

print(solve(sys.argv[1]))