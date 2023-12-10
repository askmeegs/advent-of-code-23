# -------- PARSE INPUT ------------------------------------------------
with open("med-part-two.txt") as f:
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
t = t.replace("S", "Γ", 1)
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

# the max dist away from S is half the length of the path of the cycle.
print(len(result) // 2)


pm = M.copy()
for i in range(0, len(pm)):
    T = list(pm[i])
    for j in range(0, len(T)):
        if (i, j) in result:
            T[j] = "🟩"
        elif (
            T[j] == "Γ"
            or T[j] == "⅂"
            or T[j] == "⅃"
            or T[j] == "L"
            or T[j] == "|"
            or T[j] == "-"
        ):
            T[j] = "🟦"
        else:
            T[j] = "🟫"
    pm[i] = "".join(T)

"""
Border calculations to get exact shape 

for row 0, get min and max c, where c is a green 
turn any col cell outside those boundaries to black 
"""
row_boundaries = {}  # row --> (min_col, max_col)
for coord in result:
    r = coord[0]
    c = coord[1]
    if r not in row_boundaries:
        row_boundaries[r] = (c, c)
    else:
        if c < row_boundaries[r][0]:
            row_boundaries[r] = (c, row_boundaries[r][1])
        if c > row_boundaries[r][1]:
            row_boundaries[r] = (row_boundaries[r][0], c)

print(row_boundaries)
for i in range(0, len(pm)):
    T = list(pm[i])
    for j in range(0, len(T)):
        # if j is outside the row boundaries for i, turn cell to black
        if i not in row_boundaries:
            T[j] = "🟧"
        elif j < row_boundaries[i][0] or j > row_boundaries[i][1]:
            T[j] = "🟧"
    pm[i] = "".join(T)


# now do the same but with col_boundaries 
col_boundaries = {}  # col --> (min_row, max_row)
for coord in result:
    r = coord[0]
    c = coord[1]
    if c not in col_boundaries:
        col_boundaries[c] = (r, r)
    else:
        if r < col_boundaries[c][0]:
            col_boundaries[c] = (r, col_boundaries[c][1])
        if r > col_boundaries[c][1]:
            col_boundaries[c] = (col_boundaries[c][0], r)
print(col_boundaries)

for i in range(0, len(pm)):
    T = list(pm[i])
    for j in range(0, len(T)):
        # if i is outside the col boundaries for j, turn cell to black
        if j not in col_boundaries:
            T[j] = "🟧"
        elif i < col_boundaries[j][0] or i > col_boundaries[j][1]:
            T[j] = "🟧"
    pm[i] = "".join(T)
pp(pm)

# return the sum of all blue and brown squares
total = 0
for i in range(0, len(pm)):
    T = list(pm[i])
    for j in range(0, len(T)):
        if T[j] == "🟦" or T[j] == "🟫":
            total += 1
print(total)