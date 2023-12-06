"""
Time:      7  15   30
Distance:  9  40  200

Time:        49     97     94     94
Distance:   263   1532   1378   1851

Now the input is just one big race. 

Time: 71530
Dist:  940200

Time: 49979494
Distance: 263153213781851
"""

t = 49979494
record_dist = 263153213781851
numways = 0
# big_times = [49, 97, 94, 94]
# big_rec_dist = [263, 1532, 1378, 1851]


for b in range(0, t + 1):
    # print % complete
    if b % 100000 == 0:
        print("Progress: ", b / t * 100, "%")
    speed = b  # b mm/ms
    moving_time = t - b
    d = speed * moving_time
    if d > record_dist:
        numways += 1


print("Result: ", numways)
