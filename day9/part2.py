import sys
import time
import functools

def solve(file):
    sum = 0
    with open(file, 'r') as data:
        for line in data:
            sum += extrapolate(list(map(int, line.split())))
    return sum
    
def extrapolate(line: list[str]) -> int:
    diffs = getDifferences(line)
    if diffs == [0] * len(diffs):
        return line[0]
    return line[0] - extrapolate(diffs)

def getDifferences(line: list[str]) -> list[str]:
    differences = [0] * (len(line) - 1)
    for i in range(len(line) - 1):
        differences[i] = line[i + 1] - line[i]
    return differences

start_time = time.time()
print(solve(sys.argv[1]))
print("--- %s seconds ---" % (time.time() - start_time))