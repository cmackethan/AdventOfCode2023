import sys
import pdb

def solve(file):
    cards = open(file, 'r').readlines()
    sum = 0
    array = []
    sum = calculate(cards, sum, array)
    print("Sum: " + str(sum))

def calculate(cards, sum, array):
    for card in cards:
        card = card.strip().split(': ')
        cardNum = int(card[0].split(' ')[1])
        array.append(cardNum)
        # array.sort()
        print(array)
        nums = card[1].split(' | ')
        winningNums = parse(nums[0])
        yourNums = parse(nums[1])
        n = len(yourNums.intersection(winningNums))
        # print(n)
        # breakpoint()
        if n == 0:
            sum += 1
        else:
            sum += calculate(cards[cardNum: cardNum + n], sum, array)
    return sum
    

def parse(nums):
    return set(map(int, list(filter(None, nums.split(' ')))))

solve(sys.argv[1])