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
five_kind = []
four_kind = []
full_house = []
three_one_one_pair = []
two_one_one_pair = []
one_one_pair = []
high_cards = []

for hand in hands:
    if len(set(list(hand))) == 1:
        five_kind.append(hand)
    if len(set(list(hand))) == 2:
        if hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            four_kind.append(hand)
        else:
            full_house.append(hand)
    if len(set(list(hand))) == 3:
        if (
            hand.count(hand[0]) == 3
            or hand.count(hand[1]) == 3
            or hand.count(hand[2]) == 3
        ):
            three_one_one_pair.append(hand)
        else:
            two_one_one_pair.append(hand)
    if len(set(list(hand))) == 4:
        one_one_pair.append(hand)
    if len(set(list(hand))) == 5:
        high_cards.append(hand)

# secondary sort
five_kind = sorted(five_kind, key=functools.cmp_to_key(compare))
four_kind = sorted(four_kind, key=functools.cmp_to_key(compare))
full_house = sorted(full_house, key=functools.cmp_to_key(compare))
three_one_one_pair = sorted(three_one_one_pair, key=functools.cmp_to_key(compare))
two_one_one_pair = sorted(two_one_one_pair, key=functools.cmp_to_key(compare))
one_one_pair = sorted(one_one_pair, key=functools.cmp_to_key(compare))
high_cards = sorted(high_cards, key=functools.cmp_to_key(compare))

# primary sort
for hand in five_kind:
    ranks.append(hand)
for hand in four_kind:
    ranks.append(hand)
for hand in full_house:
    ranks.append(hand)
for hand in three_one_one_pair:
    ranks.append(hand)
for hand in two_one_one_pair:
    ranks.append(hand)
for hand in one_one_pair:
    ranks.append(hand)
for hand in high_cards:
    ranks.append(hand)

i = 1
result = 0
for hand in reversed(ranks):
    result += i * bids[hand]
    i += 1

print("PART ONE:", result)

ranks = []
five_kind = []
four_kind = []
full_house = []
three_kind = []
two_kind = []
one_pair = []
high_card = []

# PART 2 - adjust secondary rank (within kinds) so that J is weakest card 
values = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

for hand in hands:
    if len(set(list(hand))) == 1:
        five_kind.append(hand)
    if len(set(list(hand))) == 2:
        if "J" in hand:
            five_kind.append(hand)
        elif hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            four_kind.append(hand)
        else:
            full_house.append(hand)
    if len(set(list(hand))) == 3:
        if (
            hand.count(hand[0]) == 3
            or hand.count(hand[1]) == 3
            or hand.count(hand[2]) == 3
        ):
            if "J" in hand:
                four_kind.append(hand)
            else:
                three_kind.append(hand)
        else:
            if "J" in hand:
                if hand.count("J") == 2:
                    four_kind.append(hand)
                else:
                    full_house.append(hand)
            else:
                two_kind.append(hand)
    if len(set(list(hand))) == 4:
        if "J" in hand:
            three_kind.append(hand)
        else:
            one_pair.append(hand)
    if len(set(list(hand))) == 5:
        if "J" in hand:
            one_pair.append(hand)
        else:
            high_card.append(hand)

five_kind = sorted(five_kind, key=functools.cmp_to_key(compare))
four_kind = sorted(four_kind, key=functools.cmp_to_key(compare))
full_house = sorted(full_house, key=functools.cmp_to_key(compare))
three_kind = sorted(three_kind, key=functools.cmp_to_key(compare))
two_kind = sorted(two_kind, key=functools.cmp_to_key(compare))
one_pair = sorted(one_pair, key=functools.cmp_to_key(compare))
high_card = sorted(high_card, key=functools.cmp_to_key(compare))

for hand in five_kind:
    ranks.append(hand)
for hand in four_kind:
    ranks.append(hand)
for hand in full_house:
    ranks.append(hand)
for hand in three_kind:
    ranks.append(hand)
for hand in two_kind:
    ranks.append(hand)
for hand in one_pair:
    ranks.append(hand)
for hand in high_card:
    ranks.append(hand)

i = 1
answer2 = 0
for hand in reversed(ranks):
    answer2 += i * bids[hand]
    i += 1

print("Answer 2:", answer2)
