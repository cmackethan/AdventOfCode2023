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
    print("schema[i][j] -> " + "schema[" + str(i) + "][" + str(j) + "]= " + schema[i][j])
    print("SEARCHING")
    for k in range(max(i - 1, 0), min(i + 2, len(schema))):
        for l in range(max(j - 1, 0), min(j + 2, len(schema[k]) - 1)):
            print("schema[k][l] -> " + "schema[" + str(k) + "][" + str(l) + "]= " + schema[k][l])
            if re.search('[0-9]', schema[k][l]):
                print("MATCH FOUND")
                if firstMatch[0] == '':
                    firstMatch = getMatch(schema, k, l)
                    print("firstMatch: " + firstMatch[0])
                elif (firstMatch[0] != '' and secondMatch[0] == '' and isNewMatch(firstMatch, k, l)):
                    secondMatch = getMatch(schema, k, l)
                    print("secondMatch: " + secondMatch[0])
                elif (isNewMatch(firstMatch, k, l) and
                      isNewMatch(secondMatch, k, l)):
                    return 0
    
    if firstMatch[0] != '' and secondMatch[0] != '':
        return int(firstMatch[0]) * int(secondMatch[0])
    
    return 0

def getMatch(schema, k, l):
    match = ''; start = 0; end = 0
    for m, char in enumerate(schema[k]):
        if char.isdigit():
            match += char
            end = m
        elif l in range(start, end + 1):
            break
        else:
            match = ''
            start = m + 1
    return (match, start, end, k)

def isNewMatch(match, k, l):
    return k != match[3] or not l in range(match[1], match[2] + 1)

solve(sys.argv[1])