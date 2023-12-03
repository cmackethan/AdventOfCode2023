import sys
import re

def solve(file):
    schema = open(file, 'r').readlines()
    sum = 0
    for i, line in enumerate(schema):
        line.strip()
        partNum = ''; valid = False
        for j, char in enumerate(line):
            if char.isdigit():
                partNum += char
                if not valid: valid = symbolAdjacent(schema, i, j)
            elif valid == True:
                sum += int(partNum)
                partNum = ''; valid = False
            else:
                partNum = ''
    print(sum)

def symbolAdjacent(schema, i, j):
    print("NEW SEARCH")
    print("* schema[i][j] -> " + "schema[" + str(i) + "][" + str(j) + "]= " + schema[i][j])
    for k in range(max(i - 1, 0), min(i + 2, len(schema))):
        for l in range(max(j - 1, 0), min(j + 2, len(schema[k]) - 1)):
            print("schema[k][l] -> " + "schema[" + str(k) + "][" + str(l) + "]= " + schema[k][l])
            if re.search('[^.0-9]', schema[k][l]):
                print("SYMBOL FOUND")
                return True
    return False

solve(sys.argv[1])