with open("input.txt") as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]


W = {}  # workflows


i = 0

while lines[i] != "":
    s = lines[i].split("{")
    name = s[0]
    wf = s[1][:-1]  # remove closing bracket
    wf = wf.split(",")
    W[name] = wf
    i += 1
i += 1

W["A"] = ["A"]
W["R"] = ["R"]


"""

"""
def get_min_max(W):
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


res = get_min_max(W)
print(res)