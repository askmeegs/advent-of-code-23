"""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1


Each row is a row of springs. Each char in the row is the condition of the spring. 
. = operational 
# = damaged 
? = unknown 

The numbers represent the size of each contiguous group of DAMAGED springs. 
Contiguous groups are always separated by at least one operational spring, 
for instance, #### is always 4, never 2,2. 

Goal - for each row, determine the number of possible configurations

EXAMPLE: 
???.### 1,1,3 ==> 1 

#.#.### 

EXAMPLE:
?###???????? 3,2,1 ==> 10 

.###.##.#...
.###.##..#..
.###.##...#.
.###.##....#
.###..##.#..
.###..##..#.
.###..##...#
.###...##.#.
.###...##..#
.###....##.#

Add all the rows possibleConfigs together and return the sum. 

---------

I suspect this is a recursion question, because I imagine it like this: 

Given ?###????????  and [3, 2, 1] 

We know we need to produce a group of 3. Let's say we do that like this: 
.###. 

Now we can narrow the problem to  ??????? and [2, 1]
The next contiguous group must be 2. .##. 
And we need a group of 1 somewhere: .#.  or .# 

So it's the number of ways to arrange that -- 
like permutations but with a condition that the groups must be separated by at least one .

Given n=7, k=2 ==> 

##.....
.##....
..##...
...##..


4 placements that would leave room for a contiguous group of 1 at the end. 

An additionally given, each of those outputs, place a group of 1: 

##.#...
##..#..
##...#.
##....#
.##.#..
.##..#.
.##...#
..##.#.
..##..#
...##.#

Then tack on the original .###. ==> 10 possible results. 
.###.##.#...
.###.##..#..
.###.##...#.
.###.##....#
.###..##.#..
.###..##..#.
.###..##...#
.###...##.#.
.###...##..#
.###....##.#
"""

# recursive func 
def count_configs(inp, nums): 
    # base case 1 
    if inp == "":
        if nums == []: 
            return 1  # as long as we've used all the nums, "" is a valid result. 
        else:
            return 0 #  nums expect more groups of damaged springs, but we have no space left. no options. 
    # base case 2 
    if nums == []: 
        if "#" in inp:  #
            return 0   
        else: 
            return 1 
    # recursive case  
    result = 0 
    firstChar = inp[0]
    if firstChar == "." or firstChar == "?": 
        result += count_configs(inp[1:], nums)
    if firstChar == "#" or firstChar == "?": 
    return result 


with open("small.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

configs = 0  # total number of possible configurations across all rows 
for line in lines: 
    # ???.### 1,1,3 
    line = line.split(" ")
    inp = line[0]
    nums = line[1].split(",")
    nums = [int(num) for num in nums]
    res = count_configs(inp, nums)
    configs += res

print("TOTAL # OF POSSIBLE CONFIGS: ", configs)
    