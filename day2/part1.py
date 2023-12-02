import sys

max = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def solve(file):
    sum = 0
    with open(file, 'r') as data:
        for game in data:
            gameNum = int(game.split(': ')[0].split(' ')[1])
            if possible(game.split(': ')[1].split('; ')):
                sum += gameNum
    print(sum)

def possible(handfuls):
    for handful in handfuls:
        handful = handful.split(', ')
        for cube in handful:
            cubeNum = int(cube.split(' ')[0])
            cubeColor = cube.split(' ')[1].strip()
            if cubeNum > max[cubeColor]:
                return False
    return True

solve(sys.argv[1])