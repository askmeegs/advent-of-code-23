# read in input.txt into list of strings
with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

digits = []

for line in lines:
    first = ""
    print(line)
    for i, d in enumerate(line):
        if d.isdigit():
            first = d
            break
        else:
            if d == "o" and line[i + 1] == "n" and line[i + 2] == "e":
                first = "1"
                break
            if d == "t" and line[i + 1] == "w" and line[i + 2] == "o":
                first = "2"
                break
            if (
                d == "t"
                and line[i + 1] == "h"
                and line[i + 2] == "r"
                and line[i + 3] == "e"
                and line[i + 4] == "e"
            ):
                first = "3"
                break
            if (
                d == "f"
                and line[i + 1] == "o"
                and line[i + 2] == "u"
                and line[i + 3] == "r"
            ):
                first = "4"
                break
            if (
                d == "f"
                and line[i + 1] == "i"
                and line[i + 2] == "v"
                and line[i + 3] == "e"
            ):
                first = "5"
                break
            if d == "s" and line[i + 1] == "i" and line[i + 2] == "x":
                first = "6"
                break
            if (
                d == "s"
                and line[i + 1] == "e"
                and line[i + 2] == "v"
                and line[i + 3] == "e"
                and line[i + 4] == "n"
            ):
                first = "7"
                break
            if (
                d == "e"
                and line[i + 1] == "i"
                and line[i + 2] == "g"
                and line[i + 3] == "h"
                and line[i + 4] == "t"
            ):
                first = "8"
                break
            if (
                d == "n"
                and line[i + 1] == "i"
                and line[i + 2] == "n"
                and line[i + 3] == "e"
            ):
                first = "9"
                break

    last = ""
    # go backwards through line
    # print(line)
    # walk through line backwards, by character
    for i in range(len(line) - 1, -1, -1):
        d = line[i]
        # print("i={}, d={}".format(i, d))
        if d.isdigit():
            last = d
            # print("last is digit")
            break
        else:
            if d == "e" and line[i - 1] == "n" and line[i - 2] == "o":
                last = "1"
                # print("last is 1")
                break
            if d == "o" and line[i - 1] == "w" and line[i - 2] == "t":
                last = "2"
                break
            if (
                d == "e"
                and line[i - 1] == "e"
                and line[i - 2] == "r"
                and line[i - 3] == "h"
                and line[i - 4] == "t"
            ):
                last = "3"
                break
            if (
                d == "r"
                and line[i - 1] == "u"
                and line[i - 2] == "o"
                and line[i - 3] == "f"
            ):
                last = "4"
                break
            if (
                d == "e"
                and line[i - 1] == "v"
                and line[i - 2] == "i"
                and line[i - 3] == "f"
            ):
                last = "5"
                break
            if d == "x" and line[i - 1] == "i" and line[i - 2] == "s":
                last = "6"
                break
            if (
                d == "n"
                and line[i - 1] == "e"
                and line[i - 2] == "v"
                and line[i - 3] == "e"
                and line[i - 4] == "s"
            ):
                last = "7"
                break
            if (
                d == "t"
                and line[i - 1] == "h"
                and line[i - 2] == "g"
                and line[i - 3] == "i"
                and line[i - 4] == "e"
            ):
                last = "8"
                break
            if (
                d == "e"
                and line[i - 1] == "n"
                and line[i - 2] == "i"
                and line[i - 3] == "n"
            ):
                last = "9"
                break

    print("⭐️ For line={}, first={}, last={}".format(line, first, last))
    digits.append(first + last)
print("DONE")
digits = [int(d) for d in digits]
print(sum(digits))
