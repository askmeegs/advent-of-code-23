"""
now, scratchcard causes you to win more scratchcards, a number equal to the # of winning numbers

you win copies of the next scratchcards in the list - so if you have 4 winning numbers, you get 1 copy of the next 4 cards 
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

# indexed hash of cards and the winning numbers
all_cards = {}
for i in range(0, len(winners)):
    all_cards[i] = (winners[i], mine[i])
print(all_cards)


# the number of times to compute card i (1 indexed)
# I really hope this works and I don't need recursion.... it's too soon
compute = {}
for i in range(0, len(mine)):
    compute[i] = 1

s = 0 
for i, card in enumerate(mine):
    print("I need to process card {} {} times".format(i+1, compute[i]))
    for num_times in range(0, compute[i]):
        matches = 0
        for n in card:
            if n in winners[i]:
                matches += 1
        if matches > 0:
            s += matches 
            compute[i] = compute[i]-1 
            for j in range(0, matches):
                if i + j + 1 in compute:
                    compute[i + j + 1 ] = compute[i + j + 1 ] + 1
                else:
                    compute[i + j + 1] = 1

s += len(mine)
print(s)