def hashtime(string):
    cur = 0
    for char in string:
        cur += ord(char)
        cur *= 17
        cur %= 256
    return cur


"""
PART 1 
"""
with open("input.txt") as f:
    raw = f.read()
    raw = raw.strip()

inp = raw.split(",")
print(inp)

res = 0
hash_results = {}
for s in inp:
    h = hashtime(s)
    res += h
    hash_results[s] = h
print("PART ONE:", res)
print("*********************")


"""
PART 2 

A series of boxes numbered 0-255 
Arranged in a line. 
Boxes have holes, allowing light to pass through.

      +-----+  +-----+         +-----+
Light | Box |  | Box |   ...   | Box |
----------------------------------------->
      |  0  |  |  1  |   ...   | 255 |
      +-----+  +-----+         +-----+


Within each box, list lenses 
[FRONT .... BACK ] eg. 
Box 3: [ot 7] [ab 5] [pc 6]
where "ot" is the lens label I marked, and "7" is the focal length.


Inside each box are LENS SLOTS that hold lenses to focus light.
You can add or remove lenses to each box. 

You also have access to a set of lenses with FOCAL LENGTH 1-9. 

Perform a new operation called 
HASHMAP. (Holiday ASCII String Helper Manual Arrangement Procedure)

HASH tells you the box label, eg. "rn" or "cm. Box 0-255 is valid.

{'rn=1': 30, 'cm-': 253, 'qp=3': 97, 'cm=2': 47, 'qp-': 14, 'pc=4': 180, 'ot=9': 9, 'ab=5': 197, 'pc-': 48, 'pc=6': 214, 'ot=7': 231}

How HASHMAP works:
- get the symbol from the key 
    - if it's a DASH - 
        - go to the box val 
        - if lens label is in the box 
            - remove the lens from the box
            - move any lenses in the box as far forward as they'll go 
        - else: do nothing 
    - if it's an EQUALS =
        - get the number right after. that's the FOCAL LENGTH 
        - from the library, go get a lens with that focal length 
        - before putting the lens in the light box, check: 
                - if there is already a lens in the box with the same label
                    - replace the old lens with new 
                    - do not move any other lenses in the box 
                - if there is NOT already a lens with the same label 
                    - add the lens immediately behind the other lenses (or as far up as it will go)

"""
print(hash_results)

boxes = []
for i in range(0, 256):
    boxes.append([])
# o indexed boxes
# Box 3: [(ot, 7) (ab, 5) (pc 6)


def label_in_box(box, label):
    for i, lens in enumerate(box):
        if lens[0] == label:
            return i
    return -1


"""
After "ab=5":
Box 0: [rn 1] [cm 2]
Box 3: [pc 4] [ot 9] [ab 5]
"""
def ppboxes(boxes): 
    print("----------------------")
    for b in boxes: 
        if len(b) > 0: 
            print("Box", boxes.index(b))
            res = ""
            for lens in b: 
                res = res + " " + str(lens)
            print(res)
    print("----------------------")


for s in inp:
    print("\n\n 🐸 processing {}".format(s))
    # is the last character a dash?
    if s[-1] == "-":
        print("DASH")
        label = s[:-1]
        box = hashtime(label)
        i = label_in_box(boxes[box], label)
        if i >= 0:
            print("label in box, removing")
            boxes[box].pop(i)
    elif s[-1].isdigit():
        print("EQUALS")
        focal_length = int(s[-1])
        label = s[:-2]
        box = hashtime(label)
        i = label_in_box(boxes[box], label)
        if i >= 0:  # label already in box
            print("label already in box")
            boxes[box][i] = (label, focal_length)
        else:
            print("label not in box, appending")
            boxes[box].append((label, focal_length))
    else:
        print("ERROR: invalid symbol in string")
    print("After {}:".format(s))
    ppboxes(boxes)


"""
After computing HASHMAP above, compute the FOCUSING POWER of all the lenses across all boxes. 
FP(lens) = 
    1 + box_number  TIMES 
    slot_number_in_box (1-indexed) TIMES 
    focal_length_of_lens

Return the sum of FP across all lenses in all boxes by the end of computation.  
"""
total_fp = 0 
for box_number, b in enumerate(boxes): 
    for lens in b: 
        print(lens)
        fp = 1 + box_number 
        fp *= b.index(lens) + 1
        fp *= int(lens[1]) # focal length 
        total_fp += fp
print("PART 2: ", total_fp)