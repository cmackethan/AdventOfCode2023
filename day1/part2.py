import sys
import re

def test():
    input = 'threeight'
    input = correct(input)
    print(input)
    firstDigit = re.search("(\d)", input)
    secondDigit = re.search("(\d)(?!.*\d)", input)
    print(firstDigit.group())
    print(secondDigit.group())
    print(int(firstDigit.group() + secondDigit.group()))

def solve():
    sum = 0
    with open('./input.txt', 'r') as file:
        for line in file:
            line = correct(line)
            firstDigit = re.search("(\d)", line)
            secondDigit = re.search("(\d)(?!.*\d)", line)
            sum += int(firstDigit.group() + secondDigit.group())
    print(sum)

def correct(line):
    return (
        line.replace('one', 'o1e')
        .replace('two', 't2o')
        .replace('three', 't3e')
        .replace('four', 'f4r')
        .replace('five', 'f5e')
        .replace('six', 's6x')
        .replace('seven', 's7n')
        .replace('eight', 'e8t')
        .replace('nine', 'n9e')
    )

if len(sys.argv) == 2 and sys.argv[1] == 'T':
    test()
else:
    solve()