import sys

def solve(file):
    cards = open(file, 'r').readlines()
    sum = 0
    numCards = [1] * len(cards)
    for card in cards:
        card = card.strip().split(': ')
        cardNum = int(card[0].split()[1])
        nums = card[1].split(' | ')
        winningNums = parse(nums[0])
        yourNums = parse(nums[1])
        cardsWon = len(yourNums.intersection(winningNums))
        sum += numCards[cardNum - 1]
        for i in range(cardNum, cardNum + cardsWon):
            numCards[i] += numCards[cardNum - 1]
    print(sum)

def parse(nums):
    return set(map(int, list(filter(None, nums.split()))))

solve(sys.argv[1])