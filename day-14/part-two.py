"""
The platform now has a button called Spin Cycle. 
One spin cycle = N, W, S, E. 

Calculate total load on support beams after 1000000000 (or 1 billion) spin cycles. 

"""


def north(P):
    r = 0
    while r < len(P):
        for c in range(0, len(P[r])):
            if P[r][c] == "O":
                # if we're a rock on the top row, we can't move any more.
                if r == 0:
                    continue
                else:
                    z = r
                    # look up. move until we can't move anymore.
                    while z > 0 and P[z - 1][c] == ".":
                        P[z - 1] = P[z - 1][:c] + "O" + P[z - 1][c + 1 :]
                        P[z] = P[z][:c] + "." + P[z][c + 1 :]
                        z -= 1
            c += 1
        r += 1
    return P


def west(P):
    c = 0
    while c < len(P[0]):
        for r in range(0, len(P)):
            if P[r][c] == "O":
                # if we're a rock on the leftmost column, we can't move any more.
                if c == 0:
                    continue
                else:
                    z = c
                    # look left. move until we can't move anymore.
                    while z > 0 and P[r][z - 1] == ".":
                        P[r] = P[r][: z - 1] + "O" + P[r][z:]
                        P[r] = P[r][:z] + "." + P[r][z + 1 :]
                        z -= 1
            r += 1
        c += 1
    return P


def south(P):
    r = len(P) - 1
    while r >= 0:
        for c in range(0, len(P[r])):
            if P[r][c] == "O":
                # if we're a rock on the bottom row, we can't move any more.
                if r == len(P) - 1:
                    continue
                else:
                    z = r
                    # look down. move until we can't move anymore.
                    while z < len(P) - 1 and P[z + 1][c] == ".":
                        P[z + 1] = P[z + 1][:c] + "O" + P[z + 1][c + 1 :]
                        P[z] = P[z][:c] + "." + P[z][c + 1 :]
                        z += 1
            c += 1
        r -= 1
    return P


def east(P):
    c = len(P[0]) - 1
    while c >= 0:
        for r in range(0, len(P)):
            if P[r][c] == "O":
                # if we're a rock on the rightmost column, we can't move any more.
                if c == len(P[0]) - 1:
                    continue
                else:
                    z = c
                    # look right. move until we can't move anymore.
                    while z < len(P[0]) - 1 and P[r][z + 1] == ".":
                        P[r] = P[r][:z] + "." + P[r][z + 1 :]
                        P[r] = P[r][: z + 1] + "O" + P[r][z + 2 :]
                        z += 1
            r += 1
        c -= 1
    return P


def spin_cycle(P):
    P = north(P)
    P = west(P)
    P = south(P)
    P = east(P)
    return P


def pp(L):
    for l in L:
        print(l)
    print("----------------------------------")



# solve
with open("input.txt") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]


hist = [] 
for i in range(0, 1000):
    # progress %  
    print("progress: {}%".format((i / 1000) * 100))
    lines = spin_cycle(lines)
    hist.append(lines.copy())

# calculate weight
# load rock = len(rows) - cur_row
def calc_north_load(x): 
    res = 0
    for r in range(0, len(x)):
        for c in range(0, len(x[r])):
            if x[r][c] == "O":
                res += len(x) - r
    return res 

res_vals = [] 
for i, h in enumerate(hist):
    load = calc_north_load(h)
    res_vals.append(load)

# plot res_vals 
import matplotlib.pyplot as plt
plt.plot(res_vals)
plt.ylabel("load")
plt.xlabel("spin cycle")
plt.show()

"""
it's definitely some kind of sine (?) wave. 
after the 100th spin cycle, the wave starts and the solution hovers between 104,000 and 105,000 load. 
"""
