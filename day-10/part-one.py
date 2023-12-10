"""

Input = Pipe Map



Legend:
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east. L
J is a 90-degree bend connecting north and west. ⅃
7 is a 90-degree bend connecting south and west. ⅂
F is a 90-degree bend connecting south and east. Γ
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

The map contains one "big loop" that's continuous. 

Task: given a map with S = animal starting position, find the continous loop that leads you back to S.
Then, find the point in the map FARTHEST (the max steps away) from s.

For instance, if the map is: 

.....
.S-7.
.|.|.
.L-J.
.....

The distances are: 

.....
.012.
.1.3.
.234.
.....

Return 4. 

"""

# -------- PARSE INPUT ------------------------------------------------
with open("input.txt") as f:
    M = f.readlines()
M = [line.strip() for line in M]

S = (-1, -1)
for i in range(0, len(M)):
    t = M[i]
    for j in range(0, len(t)):
        c = t[j]
        t = t.replace("J", "⅃")
        t = t.replace("7", "⅂")
        t = t.replace("F", "Γ")
        if c == "S":
            S = (i, j)
    M[i] = t


def pp(M):
    print("-----MAP ------")
    for line in M:
        print(line)
    print("----------------")


print("S={}".format(S))

# replace S with pipe
t = M[S[0]]
t = t.replace("S", "|", 1)
M[S[0]] = t
pp(M)

"""
..Γ⅂.
.Γ⅃|.
Γ⅃.L⅂
|Γ--⅃
L⅃...
"""


# translate 2D array to graph
def arr_to_graph():
    G = {}
    for i in range(0, len(M)):
        t = M[i]
        # POPULATE NODES
        for j in range(0, len(t)):
            c = t[j]
            if c == ".":
                continue
            if c == "Γ":
                G[(i, j)] = []
            if c == "⅂":
                G[(i, j)] = []
            if c == "⅃":
                G[(i, j)] = []
            if c == "L":
                G[(i, j)] = []
            if c == "|":
                G[(i, j)] = []
            if c == "-":
                G[(i, j)] = []
    # populate edges - only for valid pipe connections

    # these are connector pipes when looking in these directions.
    up = ["⅂", "|", "Γ"]
    down = ["⅃", "|", "L"]
    left = ["L", "-", "Γ"]
    right = ["⅃", "-", "⅂"]

    for i in range(0, len(M)):
        t = M[i]
        for j in range(0, len(t)):
            c = t[j]
            if c == ".":
                continue
            if c == "|":
                # look up
                if i > 0 and M[i - 1][j] in up:
                    G[(i, j)].append((i - 1, j))
                # look down
                if i < len(M) - 1 and M[i + 1][j] in down:
                    G[(i, j)].append((i + 1, j))
            if c == "-":
                # look left
                if j > 0 and M[i][j - 1] in left:
                    G[(i, j)].append((i, j - 1))
                # look right
                if j < len(t) - 1 and M[i][j + 1] in right:
                    G[(i, j)].append((i, j + 1))
            if c == "Γ":
                # look right
                if j < len(t) - 1 and M[i][j + 1] in right:
                    G[(i, j)].append((i, j + 1))
                # look down
                if i < len(M) - 1 and M[i + 1][j] in down:
                    G[(i, j)].append((i + 1, j))
            if c == "⅂":
                # look left
                if j > 0 and M[i][j - 1] in left:
                    G[(i, j)].append((i, j - 1))
                # look down
                if i < len(M) - 1 and M[i + 1][j] in down:
                    G[(i, j)].append((i + 1, j))
            if c == "⅃":
                # look left
                if j > 0 and M[i][j - 1] in left:
                    G[(i, j)].append((i, j - 1))
                # look up
                if i > 0 and M[i - 1][j] in up:
                    G[(i, j)].append((i - 1, j))
            if c == "L":
                # look right
                if j < len(t) - 1 and M[i][j + 1] in right:
                    G[(i, j)].append((i, j + 1))
                # look up
                if i > 0 and M[i - 1][j] in up:
                    G[(i, j)].append((i - 1, j))
    return G


def gpp(G):
    print("-----GRAPH------")
    for k in G:
        print("Node {}: Neighbors: {}".format(k, G[k]))
    print("----------------")


G = arr_to_graph()
gpp(G)


# Detect Cycle in G - return path  (Depth first search)
def detect_cycle(G, start):
    visited = set()
    stack = [start]
    path = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend([x for x in G[vertex] if x not in visited])
        else:
            return path
    return None

result = detect_cycle(G, S)
print(result)

# the max dist away from S is half the length of the path of the cycle. 
print(len(result) // 2)

