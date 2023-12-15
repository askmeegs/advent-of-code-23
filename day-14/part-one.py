with open("input.txt") as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]


def pp(L):
    for l in L:
        print(l)
    print("----------------------------------")


print("BEFORE ROLL")
pp(lines)

def shift_north(rows):
    r = 0
    while r < len(rows):
        for c in range(0, len(rows[r])):
            if rows[r][c] == "O":
                if r == 0:
                    continue
                else:
                    z = r  
                    while z > 0 and rows[z - 1][c] == ".":
                        # move O up one row 
                        rows[z-1] = rows[z-1][:c] + "O" + rows[z-1][c + 1:]
                    
                        # replace current row cell with "."
                        rows[z] = rows[z][:c] + "." + rows[z][c + 1:]
                        z -= 1
            c += 1
        r += 1
    return rows


lines = shift_north(lines)
print("AFTER ROLL")
pp(lines)

# calculate weight 
# load rock = len(rows) - cur_row 
res = 0 
for r in range(0, len(lines)):
    for c in range(0, len(lines[r])):
        if lines[r][c] == "O":
            res += len(lines) - r
print("DONE. RESULT = {}".format(res))