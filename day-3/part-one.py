def is_symbol(c):
    return c not in "0123456789."


# look around in any direction possible. returns True iff there's a symbol (non digit, non .) around us in any direction. attempt to handle edge cases.
def look_around(lines, i, j):
    # edge case 1 = top row
    if i == 0:
        if j == 0:
            # top left corner
            return (
                is_symbol(lines[i][j + 1])
                or is_symbol(lines[i + 1][j])
                or is_symbol(lines[i + 1][j + 1])
            )
        elif j == len(lines[i]) - 1:
            # top right corner
            return (
                is_symbol(lines[i][j - 1])
                or is_symbol(lines[i + 1][j - 1])
                or is_symbol(lines[i + 1][j])
            )
        else:
            # top row, but not a corner
            return (
                is_symbol(lines[i][j - 1])
                or is_symbol(lines[i][j + 1])
                or is_symbol(lines[i + 1][j - 1])
                or is_symbol(lines[i + 1][j])
                or is_symbol(lines[i + 1][j + 1])
            )

    # edge case 2 = bottom row
    elif i == len(lines) - 1:
        if j == 0:
            # bottom left corner
            return (
                is_symbol(lines[i - 1][j])
                or is_symbol(lines[i - 1][j + 1])
                or is_symbol(lines[i][j + 1])
            )
        elif j == len(lines[i]) - 1:
            # bottom right corner
            return (
                is_symbol(lines[i - 1][j - 1])
                or is_symbol(lines[i - 1][j])
                or is_symbol(lines[i][j - 1])
            )
        else:
            # bottom row, but not a corner
            return (
                is_symbol(lines[i - 1][j - 1])
                or is_symbol(lines[i - 1][j])
                or is_symbol(lines[i - 1][j + 1])
                or is_symbol(lines[i][j - 1])
                or is_symbol(lines[i][j + 1])
            )

    # edge case 3 = left column
    elif j == 0:
        return (
            is_symbol(lines[i - 1][j])
            or is_symbol(lines[i - 1][j + 1])
            or is_symbol(lines[i][j + 1])
            or is_symbol(lines[i + 1][j])
            or is_symbol(lines[i + 1][j + 1])
        )

    # edge case 4 = right column
    elif j == len(lines[i]) - 1:
        return (
            is_symbol(lines[i - 1][j - 1])
            or is_symbol(lines[i - 1][j])
            or is_symbol(lines[i][j - 1])
            or is_symbol(lines[i + 1][j - 1])
            or is_symbol(lines[i + 1][j])
        )

    # not an edge case, so we're in the middle
    else:
        return (
            is_symbol(lines[i - 1][j - 1])
            or is_symbol(lines[i - 1][j])
            or is_symbol(lines[i - 1][j + 1])
            or is_symbol(lines[i][j - 1])
            or is_symbol(lines[i][j + 1])
            or is_symbol(lines[i + 1][j - 1])
            or is_symbol(lines[i + 1][j])
            or is_symbol(lines[i + 1][j + 1])
        )


"""
Gondola engine schematic -- add up part numbers to find missing part 
Visual rep. of engine -- 

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

Any number adjacent to a symbol, incl. diagonally ($ * # ) is a part number. 
Periods aren't symbols. 
Anything that's not a digit or a period is a symbol. 

Every number above IS a part number EXCEPT FOR 114 and 58. All others touch a symbol in some direction. 

GOAL - Sum up all the valid part numbers 

The hard part is that digits are "sticky" to one another. we can't look at digits in isolation, because contiguous digits form one big number. 
"""

"""
Keep track of sum 
Approach -- walk through every line.
For every char in the line, check if it's a digit. IF it's a digit, start holding temporary memory and walk forward j steps.
    set ValidPartNum = False 
    for the starting digit, look in all avaialble directions (5 total) 
    for the next digit (and every subsequent middle digit) look up and down 
    
    ^^^ if at ANY point we hit a symbol (anything other than num or .) can set ValidPartNum = False, but keep walking forward until we run out of digits
    when we run out of digits (or line space) and ValidPartNum = True, add the number to the sum 

"""

def part_one(lines):
    s = 0
    for r, line in enumerate(lines):
        print("\n New line: {}".format(line))
        i = 0 
        # 467..114..
 
        while i < len(line):
            # print("\n NEW CHAR, i = {}, c = {}".format(i, line[i]))
            c = line[i]
            if c.isdigit():
                valid_part = False
                sticky = []
                j = i
                while j < len(line) and line[j].isdigit():
                    sticky.append(line[j])
                    # r = row, j = col 
                    if look_around(lines, r, j):
                        valid_part = True
                    j += 1
                if valid_part:
                    whole_sticky = int("".join(sticky))
                    s += whole_sticky
                    print("🌟 Number {} touches symbol. Adding, sum is now: {}".format(whole_sticky, s))

                    print("jumping ahead, setting i=j {}".format(j))
                    i = j  # jump ahead! keep going!
            i += 1 
    return s


with open("input.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
s = part_one(lines)
print("✅ DONE")
print(s)

"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

"""