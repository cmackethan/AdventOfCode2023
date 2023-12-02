import sys
import re

def test():
    input = 'sq55fivetwo1three'
    firstDigit = re.search("(\d)", input)
    secondDigit = re.search("(\d)(?!.*\d)", input)
    print(firstDigit.group())
    print(secondDigit.group())
    print(int(firstDigit.group() + secondDigit.group()))

def solve():
    sum = 0
    with open('./input.txt', 'r') as file:
        for line in file:
            firstDigit = re.search("(\d)", line)
            secondDigit = re.search("(\d)(?!.*\d)", line)
            sum += int(firstDigit.group() + secondDigit.group())
    print(sum)

if len(sys.argv) == 2 and sys.argv[1] == 'T':
    test()
else:
    solve()