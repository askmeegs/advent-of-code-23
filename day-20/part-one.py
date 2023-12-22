"""
Imagine a set of cables connected to communication modules.
These are logic modules that accept pulses of different frequencies.

A pulse can be HI or LO 
A module has DESTINATION MODULES. When a module sends a pulse, it sends that type (HI, LO) to all its destinations.

There are 5 TYPES of modules.
1. % = FLIP FLOP. these are like switches with special logic. 
Example: %nl -> bz, pm
        - FF starts OFF 
        - if it receives a pulse
                - HI ==> nothing happens, send no pulse  
                - LO ==> 
                    if off ==> turn on => send HI 
                    if on ==> turn off ==> send LO 

2. & = CONJUNCTION. these are small memory buffers. 
Example: &bz -> pm, pc, bv, dl, jp, fj, cc
They remember the most recent pulse received by EACH OF its connected input buffers. 
    - default to remembering LO for all inputs 
    - pulse received ==> update memory (HI/LO) for the pulse source input
            THEN:
                if all input memories are set to HI ==> send LO 
                else ==> send HI 
    - by this logic, a module with only one source input is an inverter. when it receives LO, it should send HI, and vice versa. 

3. BROADCASTER. Amplifier. 
    Receive pulse ==> Send same pulse to all dest  

4. BUTTON. There's one of these.
    Press button ==> send one LO pulse to broadcaster 


When you press the button, you have to wait until all pulses are delivered by all transit modules, before pressing it again. 

Pulses should be processed as a queue (in send order). Let's say a LO pulse is sent to modules a, b, and c. NOT recursively where a and its destinations are processed before b. 

------------ Example:------------------------------------------------
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a

FF: {'a': ['OFF', ['b']], 'b': ['OFF', ['c']], 'c': ['OFF', ['inv']]}
CONJ: {'inv': [{'c': 'LO'}, ['a']]}
BROADCASTER: ['a', 'b', 'c']


------------ This is the order of operations:------------------------
*** remember - if a flip flop recieves a HI, nothing happens!! 

button => lo  => broadcaster
broadcaster => lo => a  off 
broadcaster => lo => b off 
broadcaster => lo => c  off 

a off => receives lo => a on => hi => b 
b off => receives lo => b on => hi => c 
c off => receives lo => c on => hi => inv 
b on=> receives hi => nothing 
c on => receives hi => nothing 
inv [hi] => receives hi => inv [hi] => lo => a 
a on=> receives lo => a off => lo => b 
b on => receives lo => b off => lo => c 
c on => receives lo => c off => lo => inv 
inv [hi] => inv [lo] => hi => a 
a => recieves hi => nothing 


^ After this sequence, all pulses are done sending and all FF modules are set to OFF, completing a cycle + everything is back to how it was. (full circle sequence)
Pushing the button a second time yields the same 11-step sequence and outcome because the sequence goes full circle. 

Other configurations are set up so that pushing a button once yields different memory state (either FF or conjunction modules are in an altered state by the time the pulses move through). So pushing the button a second time has a different starting point => yields yet another different result. So you have to push the button "C" times to get a full circle, eg. 4 times puts the modules back into the default state. (all FF = off, all conjuctions = lo for all.)

Imagine that the elves have pushed the button 1000 times. 
TASK = count how many total pulses were sent (hi vs. lo) the whole time. 
In the first example, 1 button ==> 8 lo, 4 hi => 12 total.
So after 1K presses, it's 8,000 lo, 4,000 hi. 
MULTIPLY total_hi * total_lo and that's the final result. 
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
while presses < 1000:
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

        # err
        else:
            print("⚠️ err - unexpected pulse dest: {}".format(p))

    presses += 1


print("FINAL RESULT: {}".format(hi_total * lo_total))
print("ff: {}\n conj:{}".format(ff, conj))