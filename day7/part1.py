import sys
import random

def solve(file):
    data = list(map(lambda x: x.split(), open(file, 'r').readlines()))

    hands = []
    for line in data:
        hands.append((strength(line[0]), line[0], int(line[1])))
        
    hands.sort(key=lambda hand: (hand[0], relativeStrength(hand[1])))

    total_winnings = 0
    for i, hand in enumerate(hands, 1):
        total_winnings += (i * hand[2])

    return total_winnings

# Return an integer representing the strength of cards
def strength(cards):
    card_counts = {card: cards.count(card) for card in cards}

    max_card_count = card_counts.get(max(card_counts, key=card_counts.get))

    if max_card_count > 3:
        return max_card_count + 2
    elif max_card_count == 3:
        return 5 if isFullHouse(card_counts) else 4
    elif max_card_count == 2:
        return 3 if hasTwoPair(card_counts) else 2
    else:
        return 1

# Return True if card_counts represents a full house, false otherwise
def isFullHouse(card_counts):
    for card in card_counts:
        if card_counts[card] == 2:
            return True
    return False

# Return True if card_counts represents a two pair, false otherwise
def hasTwoPair(card_counts):
    foundOnePair = False
    for card in card_counts:
        if card_counts[card] == 2:
            if foundOnePair == False:
                foundOnePair = True
            else:
                return True

# Return a hex number in string format representing the relative strength of cards
def relativeStrength(cards):
    return (
    cards.replace('A', 'E')
    .replace('K', 'D')
    .replace('Q', 'C')
    .replace('J', 'B')
    .replace('T', 'A')
    )

print(solve(sys.argv[1]))