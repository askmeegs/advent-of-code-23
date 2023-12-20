"""
Part categories:

x: Extremely cool looking
m: Musical (it makes a noise when you hit it)
a: Aerodynamic
s: Shiny

Each part is sent through workflows --> accept or reject
Workflows have rules 


ex{x>10:one,m<20:two,a>30:R,A}

workflow name: ex 
4 rules:
    1.  x>10:one        If the part's x is more than 10, send the part to the workflow named one.
    2.  m<20:two        elif the part's m is less than 20, send the part to the workflow named two.
    3.  a>30:R          elif the part's a is more than 30, the part is immediately rejected (R)
    4.  A               else Accept 

When a part is sent to another workflow, start at the beginning of that workflow
A = Accepted 
R = rejected 


Whole input looks like this --

px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}


a series of workflows, then a list of part specs (ratings)

always start at workflow "in" 

TASK - for all parts, determine if it's accepted or rejected. 
if accepted, sum up the x, m, a, s values for all accepted parts. (big sum)
"""


"""
More example workflows:

cpz{x>2062:mvc,x<1856:gmr,s>3599:rgb,czs}
pks{a>1889:A,A}
rd{x>2635:R,R}
tnc{a>1862:A,s<3634:R,m<3035:R,R}
"""

with open("input.txt") as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]


W = {}  # workflows
P = {}  # parts

i = 0
# process workflows
# px{a<2006:qkq,m>2090:A,rfg}

while lines[i] != "":
    s = lines[i].split("{")
    name = s[0]
    wf = s[1][:-1]  # remove closing bracket
    wf = wf.split(",")
    W[name] = wf
    i += 1
i += 1
# process parts
# {x=787,m=2655,a=1222,s=2876}

p = 0
while i < len(lines):
    line = lines[i]
    line = line[1:]
    line = line[:-1]
    line = line.split(",")
    d = {}
    for val in line:
        val = val.split("=")
        k = val[0]
        v = val[1]
        d[k] = int(v)
    P[p] = d
    p += 1
    i += 1

W["A"] = ["A"]
W["R"] = ["R"]

print("W:")
print(W)
print("\nP:")
print(P)


def process_part(W, p):
    x = p["x"]
    m = p["m"]
    a = p["a"]
    s = p["s"]
    import time 
    wf = "in"
    rules = W[wf]
    r_index = 0
    while True: # keep going through workflows until we get an A or R. 
        while r_index < len(rules):
            # time.sleep(1)
            rule = rules[r_index]
            print("workflow={}, rule #{}, rule={}".format(wf, r_index, rule))
            if rule == "R":
                return 0
            elif rule == "A":
                return x + m + a + s
            # qqz{s>2770:qs,m<1801:hdj,R}
            elif ">" in rule:
                rule = rule.split(":")
                cond = rule[0]
                cond = cond.split(">")
                attr = cond[0]
                val = int(cond[1])
                print("I'm checking if p[attr]={} is greater than val={}".format(p[attr], val))
                if p[attr] > val:
                    print ("it is")
                    wf = rule[1] 
                    rules = W[wf]
                    print("setting workflow to wf={} and resetting r_index to 0".format(wf))
                    r_index = 0
                else: 
                    print("it's not")
                    r_index += 1 
            elif "<" in rule:
                rule = rule.split(":")
                cond = rule[0]
                cond = cond.split("<")
                attr = cond[0]
                val = int(cond[1])
                print("I'm checking if p[attr]={} is less than val={}".format(p[attr], val))
                if p[attr] < val:
                    print("it is")
                    wf = rule[1]
                    rules = W[wf]
                    print("setting workflow to wf={} and resetting r_index to 0".format(wf))
                    r_index = 0
                else: 
                    print("it's not")
                    r_index += 1 
            else: 
                # the instruction is just a go-to
                wf = rule 
                rules = W[wf]
                r_index = 0 


s = 0
for p_index, p_val in P.items():
    print("\n\nprocessing part={}:{}".format(p_index, p_val))
    r = process_part(W, p_val)
    print("result: {}".format(r))
    s += r
print("DONE: sum of accepted parts is: {}".format(s))
