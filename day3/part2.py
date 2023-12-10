import sys
import re

def solve(file):
    schema = open(file, 'r').readlines()
    sum = 0
    for i, line in enumerate(schema):
        line.strip()
        for j, char in enumerate(line):
            if char == '*':
                sum += gearRatio(schema, i, j)
    print(sum)

def gearRatio(schema, i, j):
    firstMatch = ('', 0, 0, 0); secondMatch = ('', 0, 0, 0) # -> (match, start, end, k)
    for k in range(max(i - 1, 0), min(i + 2, len(schema))):
        for l in range(max(j - 1, 0), min(j + 2, len(schema[k]) - 1)):
            if re.search('[0-9]', schema[k][l]):
                if firstMatch[0] == '':
                    firstMatch = getMatch(schema, k, l)
                elif secondMatch[0] == '' and isNewMatch(firstMatch, k, l):
                    secondMatch = getMatch(schema, k, l)
                elif (isNewMatch(firstMatch, k, l) and
                      isNewMatch(secondMatch, k, l)):
                    return 0

    if firstMatch[0] != '' and secondMatch[0] != '':
        return int(firstMatch[0]) * int(secondMatch[0])
    
    return 0

def getMatch(schema, k, l):
    match = schema[k][l]; start = l; end = l + 1
    while schema[k][start - 1].isdigit():
        match = schema[k][start - 1] + match
        start -= 1
    while schema[k][end].isdigit():
        match += schema[k][end]
        end += 1
    return (match, start, end, k)

def isNewMatch(match, k, l):
    return k != match[3] or not l in range(match[1], match[2])

solve(sys.argv[1])