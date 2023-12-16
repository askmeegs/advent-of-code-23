import os

"""

The beam of light is pointed at a contraption: a flat 2D grid consisting of: 
- EMPTY SPACE . 
- MIRRORS / and \
- SPLITTERS | - 

Each grid tile converts light into heat to melt the rock in the cave. 
The beam enters from top left, heading right. 

.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....

For the input above, this is the path:
>|<<<\....
|v-.\^....
.v...|->>>
.v...v^.|.
.v...v^...
.v...v^..\
.v../2\\..
<->-/vv|..
.|<<<2-|.\
.v//.|.v..

Any time the beam touches a tile, it becomes "energized" # 
Count how many tiles become energized on the path. 
"""


def pp(M):
    print("\n")
    for line in M:
        print("".join(line))
    print("\n")


with open("input.txt") as f:
    lines = f.readlines()

M = []
for line in lines:
    M.append(list(line.strip()))


# directional path
W = []
for i in range(len(M)):
    t = []
    for j in range(len(M[i])):
        t.append(M[i][j])
    W.append(t)


# result, # or . energized
R = []
for i in range(len(M)):
    t = []
    for j in range(len(M[i])):
        t.append(".")
    R.append(t)

# beams can pass through other beams, a tile can have multiple beams passing through it.
# we have a set of beams (At first, just one) all in different spots, traveling in different directions.
# R, L, U, D
beams = [(0, -1, "R")]
# each beam should keep going until it hits the edge of the map.

"""
MOVEMENT ALGORITHM:
    If empty space
        continue 1 step in same direction 
    If mirror / or \  ==> reflect 90 degrees based on mirror direction 
        if / 
            if moving right ==> move up 
            if moving left ==> move down 
            if moving up ==> move right 
            if moving down ==> move left
        if \ 
            if moving right ==> move down 
            if moving left ==> move up 
            if moving up ==> move left 
            if moving down ==> move right
        if pointy end of splitter | or - ==> passthrough, treat as empty space (continue 1 step in same direction)
            if moving up ==> | ==> keep moving up 
            if moving down ==> | ==> keep moving down
            if moving left ==> - ==> keep moving left
            if moving right ==> - ==> keep moving right
        if flat end of splitter  | or -  ==> split into 2 beams in the direction the splitter is going
            if moving right ==> | ==> split into 2 beams, 1 moving up, 1 moving down
            if moving left ==> | ==> split into 2 beams, 1 moving up, 1 moving down
            if moving up ==> - ==> split into 2 beams, 1 moving left, 1 moving right
            if moving down ==> - ==> split into 2 beams, 1 moving left, 1 moving right  
"""

D = {"R": ">", "L": "<", "U": "^", "D": "v"}
print(beams)
# at each iteration, we advance the beam (or split the beam) moving all beams 1 step in a direction.
while len(beams) > 0:
    NW = W.copy()
    pp(R)
    mark_del = []
    add_these = []
    for b_i, b in enumerate(beams):
        r = b[0]
        c = b[1]
        d = b[2]
        # mark cell as visited
        R[r][c] = "#"
        # look ahead 1 tile in the direction of the beam
        if d == "R":
            n_r = r
            n_c = c + 1
        if d == "L":
            n_r = r
            n_c = c - 1
        if d == "U":
            n_r = r - 1
            n_c = c
        if d == "D":
            n_r = r + 1
            n_c = c

        # have we hit a wall? if so, take the beam out of rotation
        if n_r < 0 or n_r >= len(M) or n_c < 0 or n_c >= len(M[0]):
            mark_del.append(b_i)
            continue

        # otherwise, what's at the next cell?
        n_cell = M[n_r][n_c]
        if n_cell == ".":  # continue in same direction
            beams[b_i] = (n_r, n_c, d)
            NW[n_r][n_c] = D[d]
            continue
        elif n_cell == "/":
            n_d = ""
            if d == "R":
                n_d = "U"
            elif d == "L":
                n_d = "D"
            elif d == "U":
                n_d = "R"
            else:  # D
                n_d = "L"
            beams[b_i] = (n_r, n_c, n_d)
            NW[n_r][n_c] = n_cell
            continue
        elif n_cell == "\\":  # need to escape backslashes in python
            n_d = ""
            if d == "R":
                n_d = "D"
            if d == "L":
                n_d = "U"
            if d == "U":
                n_d = "L"
            if d == "D":
                n_d = "R"
            beams[b_i] = (n_r, n_c, n_d)
            NW[n_r][n_c] = n_cell
            continue
        elif n_cell == "|":
            if d == "U" or d == "D":
                beams[b_i] = (n_r, n_c, d)
                NW[n_r][n_c] = D[d]
                continue
            if d == "L" or d == "R":
                # split into 2 beams, 1 moving up, 1 moving down
                mark_del.append(b_i)
                b_up = (n_r, n_c, "U")
                b_down = (n_r, n_c, "D")
                add_these.append(b_up)
                add_these.append(b_down)
                NW[n_r][n_c] = "2"
        elif n_cell == "-":
            if d == "L" or d == "R":
                beams[b_i] = (n_r, n_c, d)
                NW[n_r][n_c] = D[d]
                continue
            if d == "U" or d == "D":
                mark_del.append(b_i)
                b_left = (n_r, n_c, "L")
                b_right = (n_r, n_c, "R")
                add_these.append(b_left)
                add_these.append(b_right)
                NW[n_r][n_c] = "2"
        else:
            print("err: unrecognized cell")
            os.exit(1)

    # check exit case
    W = NW 
    
    beams_copy = [] 
    for b_i, b in enumerate(beams):
        if b_i not in mark_del: 
            beams_copy.append(b)
    for a in add_these:
        beams_copy.append(a)
    beams = beams_copy
pp(R)
pp(W)