with open('input.txt') as f:
    data = f.read().splitlines()

data = list(dict.fromkeys(data))

orig_blocked = set()  # Set of rock locations
minx = None  # Minimum bound for rocks in x direction
maxx = None  # Maximum bound for rocks in x direction
maxy = None  # Maximum bound for rocks in y direction

# Determine the rock bounds and original rock locations from the data
for i in range(len(data)):
    rock_path = data[i].split(" -> ")

    for j in range(1, len(rock_path)):
        px, py = rock_path[j - 1].split(",")
        px, py = int(px), int(py)
        if minx is None or px < minx:
            minx = px
        if maxx is None or px > maxx:
            maxx = px
        if maxy is None or py > maxy:
            maxy = py
        x, y = rock_path[j].split(",")
        x, y = int(x), int(y)
        if minx is None or x < minx:
            minx = x
        if maxx is None or x > maxx:
            maxx = x
        if maxy is None or y > maxy:
            maxy = y

        if px == x:
            for k in range(min(py, y), max(py + 1, y + 1)):
                orig_blocked.add((x, k))
        elif py == y:
            for k in range(min(px, x), max(px + 1, x + 1)):
                orig_blocked.add((k, y))

for z in range(500 - (maxy + 2), 500 + maxy + 2 + 1):
    orig_blocked.add((z, maxy + 2))


def add_sand(part, blocked, minx=minx, maxx=maxx, maxy=maxy, sandx=500, sandy=0):
    count = 0
    # Ensure a copy of the original rocks is used, so it resets for each part
    blocked = blocked.copy()
    # Add sand until end condition met
    # Part 1 end condition is when current sand goes fully beyond the bounds of the rocks
    # Part 2 end condition is when sand is stopped at the starting point
    while (part == 1 and minx <= sandx <= maxx and sandy <= maxy) or (part == 2 and (500, 0) not in blocked):
        # Try going down
        if (sandx, sandy + 1) in blocked:
            # Try going down left
            if (sandx - 1, sandy + 1) in blocked:
                # Try going down right
                if (sandx + 1, sandy + 1) in blocked:
                    # If it can't go anywhere, it rests here and now blocks path
                    blocked.add((sandx, sandy))
                    count += 1
                    sandx = 500
                    sandy = 0
                else:
                    # It moves to this spot, and we try to move it again on the next loop
                    sandx = sandx + 1
                    sandy = sandy + 1
            else:
                # It moves to this spot, and we try to move it again on the next loop
                sandx = sandx - 1
                sandy = sandy + 1
        else:
            # It moves to this spot, and we try to move it again on the next loop
            sandx = sandx
            sandy = sandy + 1

    return count


print("\nDay 14")
print("Part 1:", add_sand(part=1, blocked=orig_blocked))
print("Part 2:", add_sand(part=2, blocked=orig_blocked))
