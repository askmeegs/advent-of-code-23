"""
HASH algorithm: 

Turn any STRING into a NUMBER 0-255 

Start with cur=0 
For every char in string:
    - cur += char's ascii code https://en.wikipedia.org/wiki/ASCII#Printable_characters 
    - cur *= 17 
    - cur = cur % 256 

hash("HASH") = 52 

"""

def hashtime(string):
    cur = 0
    for char in string:
        cur += ord(char)
        cur *= 17
        cur %= 256
    return cur

"""
input: 

rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7

comma separated list of strings
sum the results
"""

with open("input.txt") as f: 
    raw = f.read()
    raw = raw.strip() 

inp = raw.split(",")
print(inp) 

res = 0 
for string in inp:
    res += hashtime(string)
print(res)
    