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


loop = detect_cycle(G, S)

# the max dist away from S is half the length of the path of the cycle.
# part_one_ans = len(result) // 2 

from matplotlib.path import Path

p = Path(loop)

contained = 0  
for r in range(0, len(M)):
    for c in range(0, len(M[r])):
        if (r, c) not in loop and p.contains_point((r, c)):
            contained += 1 

print("🏁 # of cells contained in loop: {}".format(contained))
