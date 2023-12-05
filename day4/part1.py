import sys

def solve(file):
    cards = open(file, 'r')
    sum = 0
    for card in cards:
        nums = card.strip().split(': ')[1].split(' | ')
        winningNums = parse(nums[0])
        yourNums = parse(nums[1])
        n = len(yourNums.intersection(winningNums))
        if n == 0: continue
        points = 2 ** (n - 1) # 2 to the power of n - 1
        sum += points
    print(sum)

def parse(nums):
    return set(map(int, list(filter(None, nums.split()))))

solve(sys.argv[1])