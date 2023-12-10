import sys
import re

def solve(file):
    with open(file, 'r') as data:
        time = parse(data.readline())
        distance = parse(data.readline())

    num_ways = 0
    for i in range(1, time):
        if i * (time - i) > distance:
            num_ways += 1
    return num_ways

def parse(str):
    return int(''.join(re.search("[0-9].*", str).group().split()))
        

print(solve(sys.argv[1]))