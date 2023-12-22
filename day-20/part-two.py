"""
PART TWO 

rx is the final module - a "leaf" module that receives but does not send.
rx turns on when it receives a SINGLE LO PULSE.

what is the fewest # of button presses needed for rx to receive a single low pulse? 
"""

ff = (
    {}
)  # % - flip flops. maps module name to [ON/OFF STATE, [<dest_list]]. start by defaulting all FF to OFF
conj = (
    {}
)  # &  - maps module names to a submap of destinations => hi/lo vals  (remembers last pulse sent, start with LO for all)
broadcaster = []  # list of broadcast destination modules
allk = {}  # map all source modules to destinations

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

for line in lines:
    line = line.split(" -> ")

    # PROCESS FLIP FLOP
    if "%" in line[0]:
        mod = line[0][1:]  # remove % symbol
        dest = line[1].split(", ")
        ff[mod] = ["OFF", dest]
        allk[mod] = dest

    # PROCESS CONJ
    # map conj name ==> [{INPUTS} [dest]]
    elif "&" in line[0]:
        mod = line[0][1:]  # remove & symbol
        dest = line[1].split(", ")
        allk[mod] = dest
        conj[mod] = [{}, dest]  # deal with {} in a second.

    # PROCESS BROADCASTER
    elif "broadcaster" in line[0]:
        dest = line[1].split(", ")
        allk["broadcaster"] = dest
        for d in dest:
            broadcaster.append(d)
    else:
        print("⚠️ unexpected token in line: ", line)


# post process conj by finding everything that maps TO each key.
# remember the last pulse sent from each...
# and set each to lo
for k, v in allk.items():
    for d in v:
        if d in conj:
            mem = conj[d][0]
            mem[k] = "LO"
            conj[d][0] = mem

print("\n\nSTARTING POINT:")
print("FF: {}".format(ff))
print("CONJ: {}".format(conj))
print("BROADCASTER: {}".format(broadcaster))
print("\n\n")

# track # of button presses
presses = 0
hi_total = 0
lo_total = 0

# FIFO queue of pulses
while presses < 10000000000:
    if presses % 100000 == 0:
        print("presses={} hi_total={} lo_total={}".format(presses, hi_total, lo_total))
    pulses = [("LO", "button", "broadcaster")]
    lo_total += 1
    # print(
    #     "press={}, hi_total={}, lo_total={}, about to press button".format(
    #         presses, hi_total, lo_total
    #     )
    # )
    while len(pulses) > 0:
        # pop from front of queue
        p = pulses[0]
        # print("\nprocessing: {}".format(p))
        # print("starting state: FF: {}\n conj: {}".format(ff, conj))
        if len(pulses) > 1:
            pulses = pulses[1:]
        else:
            pulses = []
        # process pulse
        # pulse is a tuple : (FREQ, SOURCE_MODULE, DEST_MODULE)
        freq = p[0]
        src = p[1]
        dest = p[2]

        # BROADCASTER ==> amplify pulse to all destinations
        if dest == "broadcaster":
            for m in broadcaster:
                pulses.append(("LO", dest, m))
                lo_total += 1
        # FLIP FLOP
        elif dest in ff:
            m = ff[dest]
            m_state = m[0]
            m_dest = m[1]
            if freq == "LO":
                if m_state == "OFF":
                    ff[dest] = ["ON", m_dest]
                    for d in m_dest:
                        pulses.append(("HI", dest, d))
                        hi_total += 1
                else:
                    ff[dest] = ["OFF", m_dest]
                    for d in m_dest:
                        pulses.append(("LO", dest, d))
                        lo_total += 1

        # CONJUNCTION
        elif dest in conj:
            mem = conj[dest][0]
            c_dest = conj[dest][1]
            if freq == "LO":
                mem[src] = "LO"
            else:
                mem[src] = "HI"
            conj[dest][0] = mem
            
            if all(m == "HI" for m in mem.values()):
                # print("mem {} - is all hi, so sending los.".format(mem))
                for d in c_dest:
                    pulses.append(("LO", dest, d))
                    lo_total += 1
            else:
                # print("mem {} - is NOT all hi, so sending hi.".format(mem))
                for d in c_dest:
                    pulses.append(("HI", dest, d))
                    hi_total += 1
        elif dest == "rx": 
            if freq == "LO": 
                print("🟢 RX RECEIVED LO PULSE after pressing button {} times".format(presses))
                break 
        # err
        else:
            print("⚠️ err - unexpected pulse dest: {}".format(p))

    presses += 1


