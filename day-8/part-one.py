"""
Given a map --

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)


Start at AAA and get to ZZZ through the instructions "RL" 
NODE = (LEFT, RIGHT) 

So AAA --> CCC --> ZZZ 
Reach ZZZ in 2 steps 

If you run out of instructions, repeat, ie. RLRLRLRLRLR...


LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)

        L       L       R       L       L       R
AAA --> BBB --> AAA --> BBB --> AAA --> BBB --> ZZZ
TOTAL = 6 steps 

For the large input, Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ? 
"""

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

I = lines[0]
I = list(I)
# strip instructions
lines = lines[2:]
M = {}
for line in lines:
    line = line.split(" = ")
    node = line[0]
    children = line[1].split(", ")
    # strip parens
    left = children[0][1:]
    right = children[1][:-1]
    M[node] = {}
    M[node]["left"] = left
    M[node]["right"] = right

print("Instructions={}, Map={}".format(I, M))

# get # of steps from AAA to ZZZ
steps = 0
cur_i = 0 
current = "AAA"
while current != "ZZZ":
    if cur_i >= len(I):
        cur_i = 0
    inst = I[cur_i]
    steps += 1 
    if inst == "L":
        current = M[current]["left"]
    else:
        current = M[current]["right"]
    cur_i += 1 

print("STEPS={}".format(steps))
