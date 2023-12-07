with open("small.txt", "r") as f:
    lines = f.read()

# HUMIDITY TO LOCATION
lines = lines.split("humidity-to-location map:")
h = lines[1]
h = h.split("\n")
h = list(filter(None, h))
h = [x.split(" ") for x in h]
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
h = h.split("\n")
h = list(filter(None, h))
h = [x.split(" ") for x in h]
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
h = h.split("\n")
h = list(filter(None, h))
h = [x.split(" ") for x in h]
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
h = h.split("\n")
h = list(filter(None, h))
h = [x.split(" ") for x in h]
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
h = h.split("\n")
h = list(filter(None, h))
h = [x.split(" ") for x in h]
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
h = h.split("\n")
h = list(filter(None, h))
h = [x.split(" ") for x in h]
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
h = h.split("\n")
h = list(filter(None, h))
h = [x.split(" ") for x in h]
seed_soil = []
for line in h:
    t = []
    for x in line:
        t.append(int(x))
    seed_soil.append(t)

# SEED PAIRS
lines = lines[0]
lines = lines.split("seeds: ")
raw_seeds = lines[1]
raw_seeds = raw_seeds.split(" ")
raw_seeds = list(filter(None, raw_seeds))
raw_seeds = [int(x) for x in raw_seeds]


# process pairs, each with (start, end)
seed_pairs = []
for i in range(0, len(raw_seeds), 2):
    start = raw_seeds[i]
    length = raw_seeds[i + 1]
    # OFF BY ONE?
    seed_pairs.append((start, start + length))
print("🌱 Seeds, pair edition: ", seed_pairs)

all_raw = [
    seed_soil,
    soil_fertilizer,
    fertilizer_water,
    water_light,
    light_temperature,
    temp_humidity,
    humidity_location,
]


all_maps = []
for m in all_raw:
    temp = []
    for line in m:
        source_start = line[1]
        dest_start = line[0]
        length = line[2]
        temp.append(
            [(source_start, source_start + length), (dest_start, dest_start + length)]
        )
    all_maps.append(temp)
print("ALL MAPS: ", all_maps)

# initialize result to be the OG values
# 🌱 Seeds, pair edition:  [(79, 93), (55, 68)] 
"""
All map intervals AND seed pair intervals are exclusive (do not include the last elt)

ALL MAPS:  [[[(98, 100), (50, 52)], [(50, 98), (52, 100)]], [[(15, 52), (0, 37)], [(52, 54), (37, 39)], [(0, 15), (39, 54)]], [[(53, 61), (49, 57)], [(11, 53), (0, 42)], [(0, 7), (42, 49)], [(7, 11), (57, 61)]], [[(18, 25), (88, 95)], [(25, 95), (18, 88)]], [[(77, 100), (45, 68)], [(45, 64), (81, 100)], [(64, 77), (68, 81)]], [[(69, 70), (0, 1)], [(0, 69), (1, 70)]], [[(56, 93), (60, 97)], [(93, 97), (56, 60)]]]
{(79, 93): (79, 93), (55, 68): (55, 68)}

each map in all maps is a map we need to process to slice and dice our seed pair intervals to the correct value intervals.
each sub list in map is one mapping. each mapping is [(source_start, source_end), (dest_start, dest_end)] 
if the seed pair interval doesn't fall into the mapping interval, ignore. keep val as is. 

if any part of the seed pair interval falls into the mapping interval, we need to slice and dice the seed pair subinterval to the dest subinterval -- but keep the rest of the seed pair range that DOESN'T overlap intact (map the values to whatever the value range would be.)
"""

map_names = [
    "seed_soil",
    "soil_fertilizer",
    "fertilizer_water",
    "water_light",
    "light_temperature",
    "temp_humidity",
    "humidity_location",
]

# initialize result to map seed pair ranges to themselves.
R = {}
for pair in seed_pairs:
    R[pair] = pair

# ALGORITHM BEGINS HERE  - take a slower approach
for m_index, M in enumerate(all_maps):
    for L in M: 
        source_start = L[0][0]
        source_end = L[0][1]
        source_length = source_end - source_start
        dest_start = L[1][0]
        dest_end = L[1][1]
        for seed in seed_pairs: 
            seed_start = seed[0]
            seed_end = seed[1]
            seed_val_start = R[seed][0]
            seed_val_end = R[seed][1]
            seed_length = seed_end - seed_start
            
            # get length of overlap 
            overlap_length = abs(min(seed_end, source_end) - max(seed_start, source_start))
            
            # case 0: seed pair interval is entirely outside of the mapping interval
            if seed_end <= source_start or seed_start >= source_end:
                continue
            R.pop(seed)
            # case 1: seed pair interval is equal to the source interval 
            if seed_start == source_start and seed_end == source_end:
                R[seed] = (dest_start, dest_end)
            # case 2: seed pair interval finishes partially in source interval 
            elif seed_start < source_start and seed_end > source_start and seed_end < source_end:
                # Doesn't overlap 
                R[seed_start, source_start] = (seed_val_start, seed_val_start + seed_length - overlap_length)
                # overlaps 
                R[source_start, seed_end] =  (dest_start, dest_start + (seed_end - source_start))
            # case 3: seed pair interval starts partially in source interval 
            elif seed_start > source_start and seed_start < source_end and seed_end > source_end:
                R[seed_start, source_end] = (dest_start + (seed_start - source_start), dest_end)
                R[source_end, seed_end] = (seed_val_end - (seed_end - source_end), seed_val_end)
            # case 4: seed pair interval starts before source interval and ends after source interval
            elif seed_start < source_start and seed_end > source_end:
                R[seed_start, source_start] = (seed_val_start, seed_val_start + seed_length - overlap_length)
                R[source_start, source_end] = (dest_start, dest_end)
                R[source_end, seed_end] = (seed_val_end - (seed_end - source_end), seed_val_end)
            
            # case 5: seed pair interval starts after source interval and ends before source interval
            else:
                R[seed_start, source_start] = (seed_val_start, seed_val_start + seed_length - overlap_length)
                R[source_start, seed_end] = (dest_start, dest_start + (seed_end - source_start))
                R[seed_end, source_end] = (seed_val_end - (seed_end - source_end), seed_val_end)
            

            
    
    print("\n\n\n Finished processing map: {} ---> Result is now:".format(map_names[m_index]))
    # pretty print R 
    for k, v in R.items():
        print("🌱 {} ---> {}".format(k, v))

# now, find the lowest v[0] 
min_loc = 100000000000
for k, v in R.items():
    if v[0] < min_loc:
        min_loc = v[0]
print("🌱 Lowest location: {}, corresponding to seed with start: {}".format(min_loc, k))