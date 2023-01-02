with open('input.txt') as f:
    data = f.read().splitlines()


def check_coord(j, x, y, beacon=True):
    while beacon:  # Still on the walk around
        if 0 <= x <= 4000000 and 0 <= y <= 4000000:
            # Go through each sensor to check if current coordinate is within it
            for sx, sy, d, k in sensors:
                # Skip the sensor you're currently walking around
                if j == k:
                    continue
                # Check whether the current coordinate is within the current sensor
                if abs(sx - x) + abs(sy - y) <= d:
                    # If within the sensor then there can be a beacon
                    beacon = True
                    # If we know we're within a sensor no point in checking other sensors
                    # As we already know there could be a beacon here which is not what we want
                    # So might as well keep walking
                    return beacon
                else:
                    # If we're not within this sensor, so far we think there might not be a beacon
                    # If this is still true after all sensors have been checked then we can stop
                    beacon = False
        else:
            return beacon

    return beacon

    
sensors = set()
beacons = set()
btarget = set()

ytarget = 2000000

for i, line in enumerate(data):
    sensor, beacon = line[12:].split(": closest beacon is at x=")
    sensorx, sensory = sensor.split(", y=")
    beaconx, beacony = beacon.split(", y=")
    distance = abs(int(sensorx) - int(beaconx)) + abs(int(sensory) - int(beacony))

    sensors.add((int(sensorx), int(sensory), distance, i))
    beacons.add((int(beaconx), int(beacony)))

    if int(beacony) == ytarget:
        btarget.add(int(beaconx))

targetx = set()
scorners = set()

for sx, sy, d, i in sensors:
    if (sy > ytarget >= sy - d) or (sy < ytarget <= sy + d) or sy == ytarget:
        minx = sx - (d - abs(sy - ytarget))
        maxx = sx + (d - abs(sy - ytarget))
        targetx.add((minx, maxx))

    scorners.add(((sx - d, sy), (sx, sy - d), (sx + d, sy), (sx, sy + d), i))

# Sort values of x-axis sensor ranges for given y-axis value
targetx = sorted(targetx)

# Determine overlap and take off areas with no overlap to get final answer
start = 0
end = 0
subtract = 0

for i, target in enumerate(targetx):
    if i == 0:
        start = target[0]
    elif i == len(targetx) - 1:
        end = target[1]
    else:
        prev_end = targetx[i-1][1]
        curr_end = target[1]
        next_start = targetx[i+1][0]
        if (next_start - 1) > curr_end >= prev_end:
            subtract += curr_end - next_start + 1

part1 = end - start - subtract

print("\nDay 15")
print("Part 1:", part1)

checked = set()
beacon = True
x = None
y = None

# Cycle through each sensor to walk around the perimeter
for c1, c2, c3, c4, j in scorners:
    if not beacon:
        break
    # Walk around each sensor until the returned answer is false - i.e. the coordinate is not within any sensors
    x = c1[0] - 1
    y = c1[1]
    while x < c2[0]:
        if (x, y) not in checked:
            beacon = check_coord(j, x, y)
        checked.add((x, y))
        if not beacon:
            break
        x += 1
        y -= 1
    while y < c3[1]:
        if (x, y) not in checked:
            beacon = check_coord(j, x, y)
        checked.add((x, y))
        if not beacon:
            break
        x += 1
        y += 1
    while x > c4[0]:
        if (x, y) not in checked:
            beacon = check_coord(j, x, y)
        checked.add((x, y))
        if not beacon:
            break
        x -= 1
        y += 1
    while y > c1[1]:
        if (x, y) not in checked:
            beacon = check_coord(j, x, y)
        checked.add((x, y))
        if not beacon:
            break
        x -= 1
        y -= 1

print("Part 2:", x*4000000+y)
