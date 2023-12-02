import sys

def solve(file):
    sum = 0
    with open(file, 'r') as data:
        for game in data:
            maximums = getMaximums(game.split(': ')[1].split('; '))
            power = 1
            for max in maximums:
                power *= max
            sum += power
    print(sum)

def getMaximums(handfuls):
    maxRed = 0; maxGreen = 0; maxBlue = 0
    for handful in handfuls:
        handful = handful.split(', ')
        for cube in handful:
            cubeNum = int(cube.split(' ')[0])
            cubeColor = cube.split(' ')[1].strip()
            if cubeColor == 'red' and cubeNum > maxRed:
                maxRed = cubeNum
            elif cubeColor == 'green' and cubeNum > maxGreen:
                maxGreen = cubeNum
            elif cubeColor == 'blue' and cubeNum > maxBlue:
                maxBlue = cubeNum
    return [maxRed, maxGreen, maxBlue]

solve(sys.argv[1])