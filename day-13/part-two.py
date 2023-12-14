"""
You're given a series of patterns like this - 

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

Task - find the line of reflection (either row or col)
Here, it's the vertical line between cols 5 and 6. 

A vertical line of reflection means that the reflected columns 
going left and right from the LOR are identical.

A horizontal line of reflection is the same, but for rows going up/down.
In this case: 

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#

The line of reflection is horizontal, after row 4. 

TASK: iterate through each pattern in input. 
Then, create a summary by:
- For every VLOR - Sum- the # of cols to the left of each VERTICAL LOR (where applicable)
- For every HLOR - Sum- (100 * # of rows above each HORIZONTAL LOR)
- Sum those 2 results. 

The answer to small is 405.
"""

def pp(L):
    for l in L:
        print(l)
    print("----------------------------------")

inp = []
with open("input.txt") as f:
    lines = f.readlines()

i = 0
inp = []
t = []
while i < len(lines):
    L = lines[i].strip()
    # if L is a blank line
    if "#" not in L and "." not in L:
        inp.append(t)
        t = []
    else:
        t.append(L)
    i += 1
inp.append(t)


# Run computation
# after column c - 0 indexed
vlors = []

# after row r  - 0 indexed
hlors = []


# [h, -1]
part1_answers = {}
for i in range(0, len(inp)):
    part1_answers[i] = ["z", -1]

# COMPARE ROWS - HORIZONTAL LINE OF REFLECTION? 
def check_hlor(s1, s2):
    i = len(s1) - 1
    j = 0 
    # i => s1, walk backwards
    while i >= 0 and j < len(s2):
        print("i={}, j={}, s1[i]={}, s2[j]={}".format(i, j, s1[i], s2[j]))
        if s1[i] != s2[j]:
            return False
        i -= 1
        j += 1
    return True

for idx, i in enumerate(inp):
    # print("\n\n 🏁 STARTING INPUT {}".format(i))
    hlor = False
    # check rows for HLOR
    r = 1
    while r < len(i):
        s1 = i[:r]
        s2 = i[r:]
        # print("\n↔️ r={}, checking horiz line of reflection for \ns1={}\ns2={}".format(r, s1, s2))
        if check_hlor(s1, s2):
            hlors.append(r)
            hlor = True 
            part1_answers[idx] = ["h", r]
            # print("✅ input {} has hlor after row {}".format(i, r))
            break
        r += 1
    if hlor:
        continue

    # create a copy of i, rotated 90 degrees to the right 
    # this will be used to check for VLOR
    i90 = list(zip(*i[::-1]))
    # convert list of tuples to list of strings
    i90 = ["".join(t) for t in i90]
    

    print("ROTATED 90 DEGREES")
    pp(i90)
    r = 1 
    vlor = False
    while r < len(i90):
        s1 = i90[:r]
        s2 = i90[r:]
        # print("\nr={}, checking vert line of reflection for \ns1={}\ns2={}".format(r, s1, s2))
        if check_hlor(s1, s2):
            vlors.append(r)
            vlor = True
            part1_answers[idx] = ["v", r]
            # print("✅ input {} has hlor after row {}".format(i, r))
            break
        r += 1
    
    if not vlor and not hlor:
        print("\n ⚠️  input at index {} has no VLOR or HLOR:".format(idx))
        pp(i)
# calculate summary
"""
TASK: iterate through each pattern in input. 
Then, create a summary by:
- For every VLOR - Sum- the # of cols to the left of each VERTICAL LOR (where applicable)
- For every HLOR - Sum- (100 * # of rows above each HORIZONTAL LOR)
- Sum those 2 results. 
"""

# after row, after col 
res = 0
for h in hlors:
    res += 100 * h
for v in vlors:
    res += v
print("⭐️ PART 1 res={}".format(res))
print(part1_answers)
"""
PART TWO 
Every mirror has exactly one smudge - one # or . is incorrect and should 
be the opposite type. 

For each pattern in inp, locate and fix the smudge that causes a different 
reflection line to be valid. 

For instance, here:

#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

If the top left "#" were "." instead, we'd have a different line of reflection.

..##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.
"""


def pp(L):
    for l in L:
        print(l)
    print("----------------------------------")


inp = []
with open("input.txt") as f:
    lines = f.readlines()

i = 0
inp = []
t = []
while i < len(lines):
    L = lines[i].strip()
    # if L is a blank line
    if "#" not in L and "." not in L:
        inp.append(t)
        t = []
    else:
        t.append(L)
    i += 1
inp.append(t)


# Run computation
# after column c - 0 indexed
vlors = []

# after row r  - 0 indexed
hlors = []


# COMPARE ROWS - HORIZONTAL LINE OF REFLECTION?
# (this also applies to columns because we pre rotate, to treat the cols like rows)
def check_hlor(s1, s2):
    i = len(s1) - 1
    j = 0
    # i => s1, walk backwards
    while i >= 0 and j < len(s2):
        # print("i={}, j={}, s1[i]={}, s2[j]={}".format(i, j, s1[i], s2[j]))
        if s1[i] != s2[j]:
            return False
        i -= 1
        j += 1
    return True


def create_perms(i):
    res = []
    for r in range(0, len(i)):
        for c in range(0, len(i[r])):
            temp = i.copy()
            cur_row = list(temp[r])
            if cur_row[c] == "#":
                cur_row[c] = "."
            else:
                cur_row[c] = "#"
            temp[r] = "".join(cur_row)
            res.append(temp)
    return res


for idx, i in enumerate(inp):
    perms = create_perms(i)
    found_lor = False
    p_index = 0
    while not found_lor:
        hlor = False
        r = 1
        cur = perms[p_index] 
        print("\n\ni=")
        pp(i) 
        print("cur=")
        pp(cur)
        while r < len(i):
            print("r={}".format(r))
            s1 = cur[:r]
            s2 = cur[r:]
            # print("\nevaluating cur where r={}".format(r))
            # pp(cur) 
            # print("where s1=")
            # pp(s1)
            # print("and s2=")
            # pp(s2)
            if check_hlor(s1, s2):
                if part1_answers[idx][0] == "h" and part1_answers[idx][1] == r:
                    print("hlor can't be the same as part 1")
                else:
                    hlor = True
                    found_lor = True 
                    hlors.append(r)
                    print("✅ input has hlor after row {}".format(r))
                    pp(s1) 
                    pp(s2)
                    break
            r += 1

        # create a copy of i, rotated 90 degrees to the right
        # this will be used to check for VLOR
        i90 = list(zip(*cur[::-1]))
        # convert list of tuples to list of strings
        i90 = ["".join(t) for t in i90]

        # print("⭐️ ROTATED 90 DEGREES")
        # pp(i90)
        r = 1
        vlor = False
        while r < len(i90):
            s1 = i90[:r]
            s2 = i90[r:]
            # print("\nr={}, checking vert line of reflection for \ns1={}\ns2={}".format(r, s1, s2))
            if check_hlor(s1, s2):
                if part1_answers[idx][0] == "v" and part1_answers[idx][1] == r:
                    print("vlor can't be the same as part 1")
                else:
                    vlor = True
                    found_lor = True
                    print("✅ input {} has vlor after row {}".format(cur, r))
                    vlors.append(r)
                    break
            r += 1
        p_index += 1

# after row, after col
print("done iterating")
print("hlors={}".format(hlors))
print("vlors={}".format(vlors))
res = 0
for h in hlors:
    res += 100 * h
for v in vlors:
    res += v
print("res={}".format(res))
