# """
# Given a "dig plan" --

# R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)

# Determine how many cubic meters of lava the lagoon can hold.
# Do this by:
# - Imagining looking over a plot of land from above.
# - The plot of land is a 2D grid, with each square meter being 1x1.
# - Start by digging a 1x1x1 hole in the ground.
# - Then follow the instructions of the dig plan by digging the specifieid
# # of meters in the specified direction. For instance, 6 meters Right, then 5 meters Down.
# (UP = North, DOWN = South, LEFT = West, RIGHT = East)
# - You must also paint the trench, once dug, with the specified hex color.

# The dig plan above results in:

# #######
# #.....#
# ###...#
# ..#...#
# ..#...#
# ###.###
# #...#..
# ##..###
# .#....#
# .######


# Where the lagoon is a big loop, 1 meter deep.
# Then, dig out the interior 1 meter deep too.

# #######
# #######
# #######
# ..#####
# ..#####
# #######
# #####..
# #######
# .######
# .######

# There are 62 "#" symbols in the grid, therefore the lagoon can hold 62 cubic meters of lava.

# """

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


def pp(G):
    print("\n")
    for line in G:
        t = ""
        for c in line:
            if c != ".":
                t += "#"
            else:
                t += "."
        print(t)
    print("\n")


def all_dots(G):
    for line in G:
        for c in line:
            if c != ".":
                return False
    return True


def trim(G):
    # trim the grid
    # trim top
    while all_dots(G[0]):
        G.pop(0)
    # trim bottom
    while all_dots(G[len(G) - 1]):
        G.pop(len(G) - 1)
    # trim left
    while all_dots([G[i][0] for i in range(0, len(G))]):
        for i in range(0, len(G)):
            G[i].pop(0)
    # trim right
    while all_dots([G[i][len(G[i]) - 1] for i in range(0, len(G))]):
        for i in range(0, len(G)):
            G[i].pop(len(G[i]) - 1)
    return G


def expand(G, r, c):
    n = len(G)
    m = len(G[0])
    # if r or c is out of bounds, expand the grid in that direction
    if r >= n:
        # expand grid below
        G.append([])
        for i in range(0, m):
            G[n].append(".")
    if r <= 1:
        # expand grid to the top
        G.insert(0, [])
        for i in range(0, m):
            G[0].append(".")
    if c >= m:
        # expand grid to the right
        for i in range(0, n):
            G[i].append(".")
    if c <= 1:
        # expand grid to the left
        for i in range(0, n):
            G[i].insert(0, ".")
    return G


def paint(inp, G, r, c):
    for item in inp:
        print("processing dig instruction: {}".format(item))
        direction = item[0]
        dist = int(item[1])

        color = item[2]
        # strip parantheses
        color = color[1:-1]
        if direction == "R":
            for s in range(0, int(dist)):
                G = expand(G, r, c)
                G[r][c] = color
                c += 1
        elif direction == "L":
            for s in range(0, int(dist)):
                G = expand(G, r, c)
                G[r][c] = color
                c -= 1
        elif direction == "U":
            for s in range(0, int(dist)):
                G = expand(G, r, c)
                G[r][c] = color
                r -= 1
        elif direction == "D":
            for s in range(0, int(dist)):
                G = expand(G, r, c)
                G[r][c] = color
                r += 1
        else:
            print("ERROR: unknown direction {}".format(direction))
    return G


with open("input.txt") as f:
    inp = f.readlines()
inp = [line.strip() for line in inp]
inp = [line.split(" ") for line in inp]


# draw the grid.
G = []
n = 10000
m = 10000
for i in range(0, n):
    G.append([])
    for j in range(0, m):
        G[i].append(".")
r = 500
c = 500

G = paint(inp, G, r, c)
G = trim(G)


# https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_floodfill.html


# colorprint
# plt.figure()
# for i in range(0, len(G)):
#     for j in range(0, len(G[i])):
#         c = G[i][j]
#         if c != ".":
#             # fill cell with color
#             # plt.gca().add_patch(plt.Rectangle((j, i), 1, 1, fc=c))
#             plt.gca().add_patch(plt.Rectangle((j, i), 1, 1, fc="black"))
#         else:
#             # fill cell with white
#             plt.gca().add_patch(plt.Rectangle((j, i), 1, 1, fc="white"))

# # show grid
# plt.xlim(0, len(G[0]))
# plt.ylim(0, len(G))
# plt.axis("scaled")
# plt.show()


# perimeter = 0
# for i in range(0, len(G)):
#     for j in range(0, len(G[i])):
#         c = G[i][j]
#         if c != 0:
#             perimeter += 1
# print("perimeter={}".format(perimeter))

# # shoelace formula
# # https://en.wikipedia.org/wiki/Shoelace_formula
# # https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
# # https://stackoverflow.com/questions/41077185/fastest-way-to-shoelace-formula
# coords = []
# for i in range(0, len(G)):
#     for j in range(0, len(G[i])):
#         c = G[i][j]
#         if c != ".":
#             coords.append((i, j))
# print(coords)


pp(G)
# pounds and dots version
P = []
for line in G:
    t = []
    for c in line:
        if c != ".":
            t += "#"
        else:
            t += "."
    P.append(t)


"""
#######
#.....#
###...#
..#...#
..#...#
###.###
#...#..
##..###
.#....#
.######

#######
#XXXXX#
###...#
XX#...#
XX#...#
###.###
#XXX#XX
##..###
X#....#
X######
"""


# iterate over every cell.
# if I'm a dot, look up, down, left, and right to figure out if I'm inside the shape or outside.
# I'm only inside if I'm surrounded by # on ALL FOUR sides.
for r in range(0, len(P)):
    for c in range(0, len(P[r])):
        if P[r][c] == ".":
            # print("\n evaluating cell r={}, c={}".format(r, c))
            insides = 0
            # look right
            for x in range(c+1, len(P[r])):
                if P[r][x] == "#":
                    # print("found # to the right at r={}, c={}".format(r, x))
                    insides += 1
                    break
            # look left
            for x in range(0, c):
                if P[r][x] == "#":
                    # print("found # to the left at r={}, c={}".format(r, x))
                    insides += 1
                    break
            # look up
            for y in range(0, r):
                if P[y][c] == "#":
                    # print("found # above at r={}, c={}".format(y, c))
                    insides += 1
                    break
            # look down
            for y in range(r+1, len(P)):
                if P[y][c] == "#":
                    # print("found # below at r={}, c={}".format(y, c))
                    insides += 1
                    break
            # print("r={}, c={}, insides={}".format(r, c, insides))
            if insides < 4:
                P[r][c] = "X"


for r in P:
    print("".join(r))

# count the number of # and . characters
area = 0
for i in range(0, len(P)):
    for j in range(0, len(P[i])):
        if P[i][j] == "#" or P[i][j] == ".":
            area += 1
print("AREA: {}".format(area))
