with open("count.txt") as r: 
    lines = r.readlines()

c = 0 
for line in lines: 
    for char in line: 
        if char == "#":
            c += 1 
print(c)