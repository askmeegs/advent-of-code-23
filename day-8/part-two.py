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

starts = []
for node in M:
    if node[-1] == "A":
        starts.append(node)

ends = [] 
for node in M:
    if node[-1] == "Z":
        ends.append(node)

def all_end_z(N):
    for node in N:
        if node[-1] != "Z":
            return False
    return True

print("Nodes that end in A={}".format(starts))
print(starts)
print("Nodes that end in Z={}".format(ends))
print(ends)


result = {}
for n in starts:
    result[n] = 0

for n in starts:
    # get # of steps from AAA to ZZZ
    steps = 0
    cur_i = 0 
    current = n
    while current not in ends:
        if cur_i >= len(I):
            cur_i = 0
        inst = I[cur_i]
        steps += 1 
        if inst == "L":
            current = M[current]["left"]
        else:
            current = M[current]["right"]
        cur_i += 1 
    result[n] = steps

print(result) 

# get LCM of all result values
import math
lcm = 1
for n in result:
    lcm = lcm * result[n] // math.gcd(lcm, result[n])
print(lcm)