import functools

# read input
with open("input.txt") as f:
    input_list = f.read().splitlines()
bids = {}
hands = []
for line in input_list:
    cards, bid = line.split()
    bid = int(bid)
    bids[cards] = bid
    hands.append(cards)

# custom sort
"""
If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.
"""

def compare(hand1, hand2):
    for x in range(6):
        if values.index(hand1[x]) < values.index(hand2[x]):
            return -1
        if values.index(hand1[x]) > values.index(hand2[x]):
            return 1
    return 0

# sorted strongest -> lowest 
values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

ranks = []
fives = []
fours = []
full_house = []
three_one_pairs = []
two_one_pairs = []
one_pairs = []
high_cards = []

for hand in hands:
    if len(set(list(hand))) == 1:
        fives.append(hand)
    if len(set(list(hand))) == 2:
        if hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            fours.append(hand)
        else:
            full_house.append(hand)
    if len(set(list(hand))) == 3:
        if (
            hand.count(hand[0]) == 3
            or hand.count(hand[1]) == 3
            or hand.count(hand[2]) == 3
        ):
            three_one_pairs.append(hand)
        else:
            two_one_pairs.append(hand)
    if len(set(list(hand))) == 4:
        one_pairs.append(hand)
    if len(set(list(hand))) == 5:
        high_cards.append(hand)

# secondary sort
fives = sorted(fives, key=functools.cmp_to_key(compare))
fours = sorted(fours, key=functools.cmp_to_key(compare))
full_house = sorted(full_house, key=functools.cmp_to_key(compare))
three_one_pairs = sorted(three_one_pairs, key=functools.cmp_to_key(compare))
two_one_pairs = sorted(two_one_pairs, key=functools.cmp_to_key(compare))
one_pairs = sorted(one_pairs, key=functools.cmp_to_key(compare))
high_cards = sorted(high_cards, key=functools.cmp_to_key(compare))

# primary sort
for hand in fives:
    ranks.append(hand)
for hand in fours:
    ranks.append(hand)
for hand in full_house:
    ranks.append(hand)
for hand in three_one_pairs:
    ranks.append(hand)
for hand in two_one_pairs:
    ranks.append(hand)
for hand in one_pairs:
    ranks.append(hand)
for hand in high_cards:
    ranks.append(hand)

i = 1
result = 0
for hand in reversed(ranks):
    result += i * bids[hand]
    i += 1

print("Sum:", result)
