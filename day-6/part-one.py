"""
Time:      7  15   30
Distance:  9  40  200

Time:        49     97     94     94
Distance:   263   1532   1378   1851

Toy boat race: 
Holding the button charges the boat
Releasing the button = boat moves

Time spent holding the button counts against time 

Each column in the input is a race.
The first race lasts 7ms and the record distance is 9mm. 

The starting speed is 0mm/ms. 
For each whole ms you press the button, the boat's speed increases by 1mm/ms.

Distance = speed * time

There are multiple ways usually to get the same distance/time result in a race, for instance:
    hold button 0ms --> speed remains at 0mm/ms for 7 seconds --> distance = 0mm 
    hold button 1ms --> speed increases to 1mm/ms for 6 seconds --> distance = 6mm
    hold button 2ms --> speed increases to 2mm/ms for 5 seconds --> distance = 10mm
    hold button 3ms --> speed increases to 3mm/ms for 4 seconds --> distance = 12mm
    hold button 4ms --> speed increases to 4mm/ms for 3 seconds --> distance = 12mm
    hold button 5ms --> speed increases to 5mm/ms for 2 seconds --> distance = 10mm
    hold button 6ms --> speed increases to 6mm/ms for 1 seconds --> distance = 6mm
    hold button 7ms --> speed increases to 7mm/ms for 0 seconds --> distance = 0mm

Races have times. Distances are the record. 
The record for race 1 is 9mm, and there are 4 ways to beat this (hold for 2,3,4,5 ms)

TASK - determine the # of ways to beat the race distance for each race time. 
Multiply each race-#-beat value together (eg. for race 1, that value=4).
"""

# small_times = [7, 15, 30]
# small_rec_dist = [9, 40, 200]

big_times = [49, 97, 94, 94]
big_rec_dist = [263, 1532, 1378, 1851]

numways = [0, 0, 0, 0]

for i, t in enumerate(big_times):
    record_dist = big_rec_dist[i]
    # b = # of ms holding button
    for b in range(0, t + 1):
        speed = b  # b mm/ms
        # moving_time = the remaining time to cover the distance at this speed
        moving_time = t - b
        d = speed * moving_time
        if d > record_dist:
            numways[i] += 1

# multiply values in numways to get result
result = 1
for n in numways:
    result *= n
print("Result: ", result)