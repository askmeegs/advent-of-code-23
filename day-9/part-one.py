"""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45

Each line is the history of an environmental factor. 
Predict the next value by computing the differences:
 
 
0 3 6 9 12 15 -->
    3 3 3 3 3 

Repeat until the sequence is all zeroes.
0 3 6 9 12 15  
 3 3 3 3 3 
  0 0 0 0

Use this data to predict the next value in the sequence.
Do this by adding an extra zero to the end of zeroes, then a placeholder at the end of every intermediate sequence: 

0 3 6 9 12 15 B  
 3 3 3 3 3 A
  0 0 0 0 0 

Populate the placeholders by adding the below value to the last numerical value in the previous line. 

0+3 -- >
0 3 6 9 12 15 B  
 3 3 3 3 3 3
  0 0 0 0 0

15+3 --> 
 0 3 6 9 12 15 18  
 3 3 3 3 3 3
  0 0 0 0 0
  
  
====== ANOTHER EXAMPLE ============
Input: 
1 3 6 10 15 21

Differences:
1   3   6  10  15  21
  2   3   4   5   6
    1   1   1   1
      0   0   0

Predict next value: ==> 28 
1   3   6  10  15  21    28 
  2   3   4   5   6    7
    1   1   1   1   1 
      0   0   0   0
      
GOAL: Predict the next value in every history sequence. Return the SUM. 
"""

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

lines = [line.split(" ") for line in lines]
inputs = [] 
for line in lines:
    t = []  
    for c in line: 
        t.append(int(c))
    inputs.append(t)
print("INPUTS: ", inputs)


def allZeroes(L):
    for i in L:
        if i != 0:
            print("{} is not all zeroes".format(L))
            return False
    print("{} is all zeroes".format(L))
    return True


# list of lists
allseqs = []
for i in inputs:
    print("\n Now processing input: {}".format(i))
    seqs = [i]
    curseq = seqs[-1]
    while not allZeroes(curseq):
        t = []
        for j in range(1, len(curseq)):
            d = curseq[j] - curseq[j-1]
            t.append(d)
        seqs.append(t)
        print("input={}, seqs is now={}".format(input, seqs)) 
        curseq = seqs[-1]
    allseqs.append(seqs)
print("\n\n Final seqs: {}".format(allseqs))

# append an extra zero to the last list in each 
for A in allseqs: 
    A[-1] = A[-1].append(0)


"""
0 3 6 9 12 15 B  
 3 3 3 3 3 A
  0 0 0 0 0 
"""
sum = 0
for A in allseqs: 
    j = len(A)-2 
    p = 0 #predict. the last row is always 0s.   
    while j >= 0:
        p = p + A[j][-1]
        j -= 1 
    print("Input={}, next predicted value is {}".format(A[0], p))
    sum += p 

print("SUM={}".format(sum))
