with open("input.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

games = {}
for line in lines:
    game_id = line.split(":")[0]
    game_id = game_id.split(" ")[1]
    game_id = int(game_id)
    # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game = line.split(":")[1]
    hands = game.split(";")
    hands = [hand.strip() for hand in hands]
    f_hands = []
    for h in hands:
        cur_hand = (0, 0, 0)
        h = h.split(",")
        for i, color in enumerate(h):
            color = color.strip()
            color = color.split(" ")
            num_color = int(color[0])
            # (red, green, blue)
            if color[1] == "red":
                cur_hand = (num_color, cur_hand[1], cur_hand[2])
            if color[1] == "green":
                cur_hand = (cur_hand[0], num_color, cur_hand[2])
            if color[1] == "blue":
                cur_hand = (cur_hand[0], cur_hand[1], num_color)
        f_hands.append(cur_hand)
    games[game_id] = f_hands
print(games)


"""
Now, raw input:
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

Looks like:
{1: [(4, 0, 3), (1, 2, 6), (0, 2, 0)]}
"""

"""
PART 2 

Cast off the cube amounts from part 1. 

What is the FEWEST number of cubes of each color that *could* have been in the bag,
to make the game possible? 

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

^ Could have been played with as few as: 
4 red, 
2 green, and 
6 blue cubes

Basically take the max val of all colors seen 
For return value, multiply all together (across all games) and return the sum. 
"""

vals = []
for game_id, game in games.items():
    max_red = 0  # 0 index
    max_green = 0  # 1 index
    max_blue = 0  # 2 index
    for hand in game:
        if hand[0] > max_red:
            max_red = hand[0]
        if hand[1] > max_green:
            max_green = hand[1]
        if hand[2] > max_blue:
            max_blue = hand[2]
    vals.append((max_red, max_green, max_blue))


# process vals to get return value
s = 0
for v in vals:
    power = 1
    for c in v:
        power *= c
    print(power)
    s += power

print("💪🏻 DONE: sum of all powers is {}".format(s))
