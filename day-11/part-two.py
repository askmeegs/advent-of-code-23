with open("input.txt") as f:
    lines = f.readlines()
    line = [line.strip() for line in lines]

M = []
for line in lines:
    line = line.strip()
    line = list(line)
    M.append(line)


def all_dots(L):
    for c in L:
        if c != ".":
            return False
    return True


# get the original coords of all galaxies
galaxies = []
for i in range(len(M)):
    for j in range(len(M[i])):
        if M[i][j] == "#":
            galaxies.append((i, j))

print("\n✨ Galaxies before alteration:")
for g in galaxies:
    print(g)
print("\n")

# find the indices of rows and cols that are all dots - these are the ones we need to copy x 1 million.
# each empty row should be replaced with 1000000 empty rows,
# + each empty column should be replaced with 1000000 empty columns.
all_dot_rows = []
all_dot_cols = []

for i, row in enumerate(M):
    if all_dots(row):
        all_dot_rows.append(i)

# create temporary columns
cols = []
for i in range(len(M[0])):
    col = []
    for row in M:
        col.append(row[i])
    cols.append(col)
for j, col in enumerate(cols):
    if all_dots(col):
        all_dot_cols.append(j)

all_dot_rows = sorted(all_dot_rows)
all_dot_cols = sorted(all_dot_cols)

print("all_dot_rows", all_dot_rows)
print("all_dot_cols", all_dot_cols)

# alter coords:
# for every galaxy with (r,c) location:
# alter row: walk through all_dot_rows. for every value less than r, add 1000000 to r.
# alter col: walk through all_dot_cols. for every value less than c, add 1000000 to c.
for i, g in enumerate(galaxies):
    r = g[0]
    c = g[1]
    tR = r 
    tC = c
    for row in all_dot_rows:
        if row < r:
            tR += 999999
    for col in all_dot_cols:
        if col < c:
            tC += 999999
    galaxies[i] = (tR, tC)


# The key is that you don't need M or any 2D array to calculate the shortest path.
def shortest_path(start, end):
    start_r = start[0]
    start_c = start[1]
    end_r = end[0]
    end_c = end[1]
    return abs(start_r - end_r) + abs(start_c - end_c)


numPairs = len(galaxies) * (len(galaxies) - 1) / 2
print("There are {} galaxies and {} pairs".format(len(galaxies), numPairs))

print("\n✨ Galaxies after alteration:")
for g in galaxies:
    print(g)
print("\n")
# sum - part 2 result (same calculation) - does not require M
s = 0
done = {}
for g in galaxies:
    for h in galaxies:
        if g != h and (g, h) not in done and (h, g) not in done:
            sp = shortest_path(g, h)
            print("The shortest path from {} to {} is {}".format(g, h, sp))
            s += sp
            done[(g, h)] = True

print("🌈 Sum of shortest paths is", s)
