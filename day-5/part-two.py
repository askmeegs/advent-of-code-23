# PARSE INPUT 😳
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

# SEEDS PART TWO
"""
PART TWO 

Now, instead of seeds describing a list of discrete seeds, it describes ranges.

seeds: 79 14 55 13
this is pairs, with [start, length] - so 79 start with range 14 = 79, 80 ... 92 

55 start with range 13 = 55, 56 ... 67
"""
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
    seed_pairs.append((start, start+length))
print("🌱 Seeds, pair edition: ", seed_pairs)

all_maps = [
    seed_soil,
    soil_fertilizer,
    fertilizer_water,
    water_light,
    light_temperature,
    temp_humidity,
    humidity_location,
]


# initialize beginning to be the original seed pairs and their own values 
B = {}
for pair in seed_pairs:
    B[pair] = pair 
E = {}
for m in all_maps[:1]:
    print("B is:", B)
    E = {}
    for mapping in m:
        # reset R, we're making it anew
        m_dest_start = mapping[0]
        m_source_start = mapping[1]
        m_length = mapping[2]
        m_source_end = m_source_start + m_length
        m_dest_end = m_dest_start + m_length
        print("Mapping has source start {}, source end {}, dest start={} and dest end {}".format(m_source_start, m_source_end, m_dest_start, m_dest_end))
        for k, v in B.items(): 
            s_start = k[0]
            s_end = k[1]
            s_length = s_end - s_start
            

    print("Done with m - E is:", E)
    B = E 

