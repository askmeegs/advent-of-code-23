



# read in input.txt into list of strings
with open('input.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

digits = [] 

for line in lines: 
    # find the first char that is a digit 
    pair = [] 
    for i in range(len(line)):
        if line[i].isdigit():
            pair.append(i)
            break
    # find the last char that is a digit 
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            pair.append(i)
            break
    # create a joined string of the digits
    digit = int(''.join(pair)) 
    print(digit)
    digits.append(digit)

print("DONE")
print