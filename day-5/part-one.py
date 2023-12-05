# PARSE INPUT 😳
with open('input.txt', 'r') as f:
    lines = f.read()
    
# HUMIDITY TO LOCATION 
lines = lines.split("humidity-to-location map:")
h = lines[1]
h = h.split('\n')
h = list(filter(None, h))
h = [x.split(' ') for x in h]
humidity_location = []
for line in h:
    t = []
    for x in line:
        t.append(int(x))
    humidity_location.append(t)    
    
# TEMPERATURE TO HUMIDITY 
lines = lines[0]
lines = lines.split("temperature-to-humidity map:")
h = lines[1]
h = h.split('\n')
h = list(filter(None, h))
h = [x.split(' ') for x in h]
temp_humidity = []
for line in h:
    t = []
    for x in line:
        t.append(int(x))
    temp_humidity.append(t)    

# LIGHT TO TEMPERATURE 
lines = lines[0]
lines = lines.split("light-to-temperature map:")
h = lines[1]
h = h.split('\n')
h = list(filter(None, h))
h = [x.split(' ') for x in h]
light_temperature = []
for line in h:
    t = []
    for x in line:
        t.append(int(x))
    light_temperature.append(t)   

# WATER TO LIGHT 
lines = lines[0]
lines = lines.split("water-to-light map:")
h = lines[1]
h = h.split('\n')
h = list(filter(None, h))
h = [x.split(' ') for x in h]
water_light = []
for line in h:
    t = []
    for x in line:
        t.append(int(x))
    water_light.append(t)   

# FERTILIZER TO WATER 
lines = lines[0]
lines = lines.split("fertilizer-to-water map:")
h = lines[1]
h = h.split('\n')
h = list(filter(None, h))
h = [x.split(' ') for x in h]
fertilizer_water = []
for line in h:
    t = []
    for x in line:
        t.append(int(x))
    fertilizer_water.append(t)   

# SOIL TO FERTIZLIER 
lines = lines[0]
lines = lines.split("soil-to-fertilizer map:")
h = lines[1]
h = h.split('\n')
h = list(filter(None, h))
h = [x.split(' ') for x in h]
soil_fertilizer = []
for line in h:
    t = []
    for x in line:
        t.append(int(x))
    soil_fertilizer.append(t)   

# SEED TO SOIL 
lines = lines[0]
lines = lines.split("seed-to-soil map:")
h = lines[1]
h = h.split('\n')
h = list(filter(None, h))
h = [x.split(' ') for x in h]
seed_soil = []
for line in h:
    t = []
    for x in line:
        t.append(int(x))
    seed_soil.append(t)   

# SEEDS 
lines = lines[0]
lines = lines.split("seeds: ")
seeds = lines[1]
seeds = seeds.split(' ')
seeds = list(filter(None, seeds))
seeds = [int(x) for x in seeds]


"""
Now we have a list of seeds numbers, then 7 raw lists of lists for:

seed_soil
soil_fertilizer
fertilizer_water
water_light
light_temperature
temp_humidity
humidity_location


We eventually need to map every seed # to a location, then return the seed # with the min location. 
For the "maps" (lists of lists), in each line (sublist) there are always 3 numbers:
    DEST RANGE START
    SOURCE RANGE START
    RANGE LENGTH 

So if seed_soil has a line like this: 
50 98 2 

Source range start 98, dest range start 50, range length 2 
that means seed 98->50, seed 99->51. 

52 50 48
50->52, 51->53, all the way +46 more steps to 97->99. 
Any source seed that isn't in the range maps to its own source value. So seed 10 -> 10. 

Therefore the whole seed to soil mapping is: 
0 -> 0
1 -> 1
...
49 -> 49
50 -> 52  <--- our second mapping declared this change 
...
97 -> 99 <-- end of our second mapping 
98 -> 50 <-- beginning of our first mapping 
99 -> 51 <-- end of our first mapping


So if we go back to our seed list, 
79 -> 81 
14 -> 14 
55 -> 57
13 -> 13 

^ here, the first value is seed #, second value if soil #. 
We then need to map those soil numbers to fertilizer, then to water, all the way until we get to location. 

Due to the large #s in input, we CANNOT keep track of the entire ranges like we did here. ^ We only have room to keep track of the seeds and where we're at. 
"""

"""
Let's just try seed to soil with the big #s. DO NOT ITERATE OVER RANGES. 
For every mapping in the soil map, we need to determine if our seed is in that range.
If it's not, map the seed to itself


seed_soil
soil_fertilizer
fertilizer_water
water_light
light_temperature
temp_humidity
humidity_location

"""

print("Seeds: ", seeds)
print("OG seed to soil map: ", seed_soil)
R = {} # all results, mapping seed # to soil, etc. all the way to location
for s in seeds:
    R[s] = {}
    R[s]["seed"] = s
    R[s]["soil"] = s
    R[s]["fertilizer"] = s
    R[s]["water"] = s
    R[s]["light"] = s
    R[s]["temperature"] = s
    R[s]["humidity"] = s
    R[s]["location"] = s
# SEED TO SOIL 
for s in seeds:
    R[s]["soil"] = s
    for m in seed_soil:
        dest_range_start = m[0]
        source_range_start = m[1]
        range_length = m[2]
        if s >= source_range_start and s < source_range_start + range_length:
            R[s]["soil"] = s - source_range_start + dest_range_start
            break
# SOIL TO FERTILIZER
for s in seeds:
    R[s]["fertilizer"] = R[s]["soil"]
    for m in soil_fertilizer:
        dest_range_start = m[0]
        source_range_start = m[1]
        range_length = m[2]
        if R[s]["soil"] >= source_range_start and R[s]["soil"] < source_range_start + range_length:
            R[s]["fertilizer"] = R[s]["soil"] - source_range_start + dest_range_start
            break
# FERTILIZER TO WATER
for s in seeds:
    R[s]["water"] = R[s]["fertilizer"]
    for m in fertilizer_water:
        dest_range_start = m[0]
        source_range_start = m[1]
        range_length = m[2]
        if R[s]["fertilizer"] >= source_range_start and R[s]["fertilizer"] < source_range_start + range_length:
            R[s]["water"] = R[s]["fertilizer"] - source_range_start + dest_range_start
            break
# WATER TO LIGHT
for s in seeds:
    R[s]["light"] = R[s]["water"]
    for m in water_light:
        dest_range_start = m[0]
        source_range_start = m[1]
        range_length = m[2]
        if R[s]["water"] >= source_range_start and R[s]["water"] < source_range_start + range_length:
            R[s]["light"] = R[s]["water"] - source_range_start + dest_range_start
            break
# LIGHT TO TEMPERATURE
for s in seeds:
    R[s]["temperature"] = R[s]["light"]
    for m in light_temperature:
        dest_range_start = m[0]
        source_range_start = m[1]
        range_length = m[2]
        if R[s]["light"] >= source_range_start and R[s]["light"] < source_range_start + range_length:
            R[s]["temperature"] = R[s]["light"] - source_range_start + dest_range_start
            break
# TEMPERATURE TO HUMIDITY
for s in seeds:
    R[s]["humidity"] = R[s]["temperature"]
    for m in temp_humidity:
        dest_range_start = m[0]
        source_range_start = m[1]
        range_length = m[2]
        if R[s]["temperature"] >= source_range_start and R[s]["temperature"] < source_range_start + range_length:
            R[s]["humidity"] = R[s]["temperature"] - source_range_start + dest_range_start
            break
# HUMIDITY TO LOCATION
for s in seeds:
    R[s]["location"] = R[s]["humidity"]
    for m in humidity_location:
        dest_range_start = m[0]
        source_range_start = m[1]
        range_length = m[2]
        if R[s]["humidity"] >= source_range_start and R[s]["humidity"] < source_range_start + range_length:
            R[s]["location"] = R[s]["humidity"] - source_range_start + dest_range_start
            break

# pretty print R dictionary
for s in seeds:
    print("\n🌰 Seed: ", s)
    print("🌾 Soil: ", R[s]["soil"])
    print("💩 Fertilizer: ", R[s]["fertilizer"])
    print("💧 Water: ", R[s]["water"])
    print("☀️ Light: ", R[s]["light"])
    print("🥵 Temperature: ", R[s]["temperature"])
    print("🧽 Humidity: ", R[s]["humidity"])
    print("📍 Location: ", R[s]["location"])
    print("")  


# get the seed with the lowest location value 
min_loc = -1 
min_seed = -1
for s in seeds:
    if min_loc == -1:
        min_loc = R[s]["location"]
        min_seed = s
    elif R[s]["location"] < min_loc:
        min_loc = R[s]["location"]
        min_seed = s
print("🏁 SEED #{} HAS THE LOWEST LOCATION VALUE OF {}".format(min_seed, min_loc))