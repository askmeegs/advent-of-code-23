"""
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....


Given a map of empty space (.) and galaxies (#), 
sum the length of the shortest paths between every pair of galaxies.

if there are G galaxies, the # of pairs is n(n-1)/2 
For instance, if there are 9 galaxies, it's 9(8)/2, 72/2  = 36 

The catch is that the universe expanded by the time the image reaches earth.
But only some space expands. Any rows or columns that contain NO galaxies,
only empty space, DOUBLE in size. 

This:

   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^
   
Should become this: 

....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......

Using this parsed input, for every pair out of 36 pairs, 
find the shortest path by moving up, down, left, or right. 
(Can pass through galaxies. The contents of the cell don't matter.)

For instance, the shortest route between 5 and 9 is 9 steps. 
The sum of shortest paths for all pairs is 374. 
"""

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


def pp(M):
    for row in M:
        print("".join(row))


M_copy = []

print("Before appending extra rows")
pp(M_copy)

for row in M:
    M_copy.append(row)
    if all_dots(row):
        print("Extra row")
        M_copy.append(row)


print("After appending extra rows")
pp(M_copy)
# get all columns in M_copy
cols = []
for i in range(len(M_copy[0])):
    col = []
    for row in M_copy:
        col.append(row[i])
    cols.append(col)

finalcols = []
for col in cols:
    finalcols.append(col)
    if all_dots(col):
        print("extra col")
        finalcols.append(col)
# flip finalcols to get M_copy
M_copy = []
for i in range(len(finalcols[0])):
    row = []
    for col in finalcols:
        row.append(col[i])
    M_copy.append(row)


M = M_copy

# ------------ CHECK SOLUTION ---------------------------------
# sol = []
# with open("small-parsed.txt") as f:
#     lines = f.readlines()
#     lines = [line.strip() for line in lines]
#     lines = [line.split(",") for line in lines]
#     sol = lines

# if sol != M:
#     print("Incorrect. Sol is")
#     pp(sol)
#     print("Your answer is")
#     pp(M)
# else:
#     print("Correct!")


# replace all # with numbers
galaxy_index = 1
galaxies = []
for i in range(len(M)):
    for j in range(len(M[i])):
        if M[i][j] == "#":
            M[i][j] = str(galaxy_index)
            galaxy_index += 1
            galaxies.append((i, j))
pp(M)


# Given 2D array M, and a start tuple (r, c), and an end tuple (r, c),
# calculate the # of steps to get from start to end.
# using breadth first search. it's ok to pass through "." or "#" characters - the contents of the cell don't matter.
def shortest_path(M, start, end):
    start_r = start[0]
    start_c = start[1]
    end_r = end[0]
    end_c = end[1]
    visited = set()
    queue = [(start_r, start_c, 0)]
    while len(queue) > 0:
        r, c, steps = queue.pop(0)
        if (r, c) == (end_r, end_c):
            return steps
        if (r, c) in visited:
            continue
        visited.add((r, c))
        # add neighbors
        if r > 0:
            queue.append((r - 1, c, steps + 1))
        if r < len(M) - 1:
            queue.append((r + 1, c, steps + 1))
        if c > 0:
            queue.append((r, c - 1, steps + 1))
        if c < len(M[0]) - 1:
            queue.append((r, c + 1, steps + 1))
    return -1


# how many galaxies?
print("There are", len(galaxies), "galaxies")


# sum - part 1 result
s = 0
done = {}
for g in galaxies:
    # calculate progress 
    print("Progress:", len(done), "pairs done of", len(galaxies) * len(galaxies))
    for h in galaxies:
        if g != h and (g, h) not in done and (h, g) not in done:
            sp = shortest_path(M, g, h)
            s += sp
            done[(g, h)] = True

print("🌠 Sum of shortest paths is", s)
