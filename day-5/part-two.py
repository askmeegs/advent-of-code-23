# Helper func Source:
# https://stackoverflow.com/questions/2953967/built-in-function-for-computing-overlap-in-python
# return (-1, -1) if no overlap
def overlap(interval1, interval2):
    """
    Given [0, 4] and [1, 10] returns [1, 4]
    """
    if interval2[0] <= interval1[0] <= interval2[1]:
        start = interval1[0]
    elif interval1[0] <= interval2[0] <= interval1[1]:
        start = interval2[0]
    else:
        start = -1

    if interval2[0] <= interval1[1] <= interval2[1]:
        end = interval1[1]
    elif interval1[0] <= interval2[1] <= interval1[1]:
        end = interval2[1]
    else:
        end = -1
    return (start, end)


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
result = {}
for v in seed_pairs:
    result[v] = v
print(result)

"""
keep result continually up to date with intervals - we will be slicing, dicing, and removing.

result[(seedrangestart, seedrangeend)] = (deststart, destend)]
at the end, dest represents location mappings, so the goal is return the min val[0] (deststart) since deststart will always be less than or equal to destand.
"""


"""
We have (79, 93): (79, 93)
        ^ SEED RANGE     ^ VAL RANGE 

And we continuosly meet mappings like this: 
[(98, 100), (50, 52)] 
This means that a source range of 98, 100 maps to dest range of 50, 52 

Our task is to take a source range and see if there is any overlap with the seed range. 
"""


for m in all_maps:
    print("\n\nSTARTING NEW MAP")
    for l in m:
        print("\nprocessing mapping: ", l)
        source_start = l[0][0]
        source_end = l[0][1]
        dest_start = l[1][0]
        dest_end = l[1][1]
        for sr in list(result):
            v = result[sr]
            v_start = v[0]
            v_end = v[1]
            result.pop(sr)  # we will put back the slice-and-diced versions.
            seed_start = sr[0]
            seed_end = sr[1]
            o = overlap((source_start, source_end), (seed_start, seed_end))
            if o == (-1, -1):
                result[sr] = v  # put back the OG values as is.
                print(
                    "No overlap between seed range {} and source range {}, result is still={}".format(
                        sr, l[0], result
                    )
                )
                continue
            else:
                o_start = o[0]
                o_end = o[1]
                # BEFORE
                if seed_start < o_start:
                    result[(seed_start, o_start)] = (v_start, v_start + o_start)
                # OVERLAP
                """
                for the overlapping range encompassing both source and seed range, map to corresponding dest range 
                based on the overlap values 
                """
                result[(o_start, o_end)] = (dest_start + o_start, dest_start + o_end)
                # AFTER
                if seed_end > o_end:
                    result[(o_end + 1, seed_end)] = (v_end - o_end, v_end)

            print(
                "Seed range {} overlaps with source range {}, result is now={}".format(
                    sr, l[0], result
                )
            )
# find the min dest start
min_val = 100000000000
for k, v in result.items():
    if v[0] < min_val:
        min_val = v[0]
print("MIN LOCATION: ", min_val)
