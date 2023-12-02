"""
Bag of cubes with red, green, blue. 
Elf puts cubes in bag. 
Then, grabs a handful of random cubes and shows them to me - then puts them back 


Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

Game ID:  <subsets of cubes revealed  > 
For instance, in Game 1, there were 3 handfuls revealed. 
A handful has at least 1 cube, but could be any combo of the 3 colors, or all 1 color. 

QUESTION:
WHICH games in the list would have been POSSIBLE if there were only 
12 red cubes, 
13 green cubes, and 
14 blue cubes? 

SUM the IDs of the possible games and return them. 


For instance: in the example -- 
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

Games 1,2,5 are possible. 
Game 3 is impossible because we saw 20 red at once. 
Game 4 is impossible because we saw 15 blue. 
"""

# read small.txt
with open("input.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


# FORMAT: GAME[1] = [(red, green, blue), (red, green, blue), (red, green, blue)]
# set tuple value to 0 if it's not in the hand

# process input
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

possible = {}
red = 12  # tuple 0
blue = 14  # tuple 1
green = 13  # tuple 2
for game_id, game in games.items():
    p = True
    for hand in game:
        if hand[0] > red or hand[1] > green or hand[2] > blue:
            print("Disqualifying game_id {} because hand {} is invalid".format(game_id, hand))
            p = False
    possible[game_id] = p

s = 0
print("POSSIBLE IS: {}".format(possible))
for game_id, possible in possible.items():
    if possible:
        s += game_id

print("✅ DONE, sum of possible game IDs is: {}".format(s))
