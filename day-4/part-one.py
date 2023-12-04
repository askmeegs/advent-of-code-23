"""
Scratchcards: 

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53

Each card # has [winning numbers] | [your numbers] 
Goal: which of the numbers I have appear in the winning numbers?

My card 1 numbers contain 4 winning nubmers: 
48, 83, 17, and 86

meaning I get 2^(matches-1) or 8 points 

sum up the points of all cards 
"""

# parse input

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

winners = []
mine = []
for line in lines:
    line = line.split(" | ")
    # process winners
    t = line[0]
    t = t.strip().split(": ")
    t = t[1].strip().split(" ")
    t = [n for n in t if n != ""]
    w = [int(n) for n in t]
    winners.append(w)

    # process mine
    m = line[1]
    m = m.split(" ")
    m = [n.strip() for n in m]
    m = [n for n in m if n != ""]
    m = [int(n) for n in m]
    mine.append(m)

print("WINNERS:")
for w in winners:
    print(w)

print("\n\n MINE:")
for m in mine:
    print(m)

s = 0
for i, card in enumerate(mine):
    print("\n\n card {}".format(i+1))
    matches = 0
    for n in card:
        if n in winners[i]:
            matches += 1 
            print("found {} in winners, matches is now: {} ".format(n, matches))
    if matches > 0:
        s +=  2 ** (matches - 1)
    print("sum is now {}".format(s))

print("SUM: {}".format(s))
