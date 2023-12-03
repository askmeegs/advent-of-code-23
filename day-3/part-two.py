# look_around now returns the coords of a neighboring asterisk, or (-1, -1) if none found
#  where i,j is the coordinates of a single digit
# Note: I am not proud of this.
def look_around(lines, i, j):
    if i == 0:
        if j == 0:
            if lines[i][j + 1] == "*":
                return (i, j + 1)
            if lines[i + 1][j] == "*":
                return (i + 1, j)
            if lines[i + 1][j + 1] == "*":
                return (i + 1, j + 1)
        elif j == len(lines[i]) - 1:
            if lines[i][j - 1] == "*":
                return (i, j - 1)
            if lines[i + 1][j - 1] == "*":
                return (i + 1, j - 1)
            if lines[i + 1][j] == "*":
                return (i + 1, j)
        else:
            if lines[i][j - 1] == "*":
                return (i, j - 1)
            if lines[i][j + 1] == "*":
                return (i, j + 1)
            if lines[i + 1][j - 1] == "*":
                return (i + 1, j - 1)
            if lines[i + 1][j] == "*":
                return (i + 1, j)
            if lines[i + 1][j + 1] == "*":
                return (i + 1, j + 1)
    elif i == len(lines) - 1:
        if j == 0:
            if lines[i - 1][j] == "*":
                return (i - 1, j)
            if lines[i - 1][j + 1] == "*":
                return (i - 1, j + 1)
            if lines[i][j + 1] == "*":
                return (i, j + 1)
        elif j == len(lines[i]) - 1:
            if lines[i - 1][j - 1] == "*":
                return (i - 1, j - 1)
            if lines[i - 1][j] == "*":
                return (i - 1, j)
            if lines[i][j - 1] == "*":
                return (i, j - 1)
        else:
            if lines[i - 1][j - 1] == "*":
                return (i - 1, j - 1)
            if lines[i - 1][j] == "*":
                return (i - 1, j)
            if lines[i - 1][j + 1] == "*":
                return (i - 1, j + 1)
            if lines[i][j - 1] == "*":
                return (i, j - 1)
            if lines[i][j + 1] == "*":
                return (i, j + 1)
    elif j == 0:
        if lines[i - 1][j] == "*":
            return (i - 1, j)
        if lines[i - 1][j + 1] == "*":
            return (i - 1, j + 1)
        if lines[i][j + 1] == "*":
            return (i, j + 1)
        if lines[i + 1][j] == "*":
            return (i + 1, j)
        if lines[i + 1][j + 1] == "*":
            return (i + 1, j + 1)
    elif j == len(lines[i]) - 1:
        if lines[i - 1][j - 1] == "*":
            return (i - 1, j - 1)
        if lines[i - 1][j] == "*":
            return (i - 1, j)
        if lines[i][j - 1] == "*":
            return (i, j - 1)
        if lines[i + 1][j - 1] == "*":
            return (i + 1, j - 1)
        if lines[i + 1][j] == "*":
            return (i + 1, j)
    else:
        if lines[i - 1][j - 1] == "*":
            return (i - 1, j - 1)
        if lines[i - 1][j] == "*":
            return (i - 1, j)
        if lines[i - 1][j + 1] == "*":
            return (i - 1, j + 1)
        if lines[i][j - 1] == "*":
            return (i, j - 1)
        if lines[i][j + 1] == "*":
            return (i, j + 1)
        if lines[i + 1][j - 1] == "*":
            return (i + 1, j - 1)
        if lines[i + 1][j] == "*":
            return (i + 1, j)
        if lines[i + 1][j + 1] == "*":
            return (i + 1, j + 1)
    # no asterisk found
    return (-1, -1)


def part_two(lines):
    ast = {}
    for r, line in enumerate(lines):
        print("\n New line: {}".format(line))
        i = 0
        while i < len(line):
            found_ast = False 
            ast_coords = (-1, -1)
            c = line[i]
            if c.isdigit():
                sticky = []
                j = i
                while j < len(line) and line[j].isdigit():
                    sticky.append(line[j])
                    # r = row, j = col
                    # look_around now returns the coords of a neighboring asterisk, or (-1, -1) if none found
                    actual_coords = look_around(lines, r, j) 
                    if actual_coords != (-1, -1):
                        print("🌟 For digit {} at coords ({}, {}), found adjacent ast at {}".format(line[j], r, j, ast_coords))
                        found_ast = True
                        ast_coords = actual_coords
                    j += 1
                if found_ast: 
                    print("🌈 Appending {} to ast at {}".format("".join(sticky), ast_coords))
                    whole_sticky = int("".join(sticky))
                    if ast_coords in ast: 
                        temp = ast[ast_coords]
                        ast[ast_coords] = temp + [whole_sticky]
                        print("ast_coords were already in ast, ast is now: {}".format(ast))
                    else:
                        ast[ast_coords] = [whole_sticky]
                        print("ast_coords were not in ast, ast is now: {}".format(ast))
                    i = j
            i += 1
    return ast


with open("input.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

# pretty print lines into a grid
print("Lines:")
for line in lines:
    print(line)
    
# get the raw coordinates of every asterix 
coords = []
for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "*":
            coords.append((r, c))
print("All asterisk coords: {}".format(coords))

ast = part_two(lines)
print("\n\nDONE, got ast:")
print(ast)

s = 0
for k, v in ast.items():
    if v is not None and len(v) == 2:
        s += v[0] * v[1]
print("\n\nSUM: {}".format(s))
