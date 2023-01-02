with open('input.txt') as f:
    lines = f.read().splitlines()


def get_answer(coords):
    hidden = 0
    for x, y, z in coords:
        if (x + 1, y, z) in coords:
            hidden += 1
        if (x - 1, y, z) in coords:
            hidden += 1
        if (x, y + 1, z) in coords:
            hidden += 1
        if (x, y - 1, z) in coords:
            hidden += 1
        if (x, y, z + 1) in coords:
            hidden += 1
        if (x, y, z - 1) in coords:
            hidden += 1

    return hidden

    
coords = set()

for line in lines:
    x, y, z = line.split(",")
    x, y, z = int(x), int(y), int(z)
    coords.add((x, y, z))

minx = None
maxx = None
miny = None
maxy = None
minz = None
maxz = None

for x, y, z in coords:
    if minx is None or x < minx:
        minx = x
    if maxx is None or x > maxx:
        maxx = x
    if miny is None or y < miny:
        miny = y
    if maxy is None or y > maxy:
        maxy = y
    if minz is None or z < minz:
        minz = z
    if maxz is None or z > maxz:
        maxz = z

minx -= 1
maxx += 1
miny -= 1
maxy += 1
minz -= 1
maxz += 1

print("\nDay 18")
print("Part 1:", len(coords) * 6 - get_answer(coords))

# Create a set with all_coords coordinates 1 outside the min and max
all_coords = set()

for a in range(minx, maxx + 1):
    for b in range(miny, maxy + 1):
        for c in range(minz, maxz + 1):
            all_coords.add((a, b, c))

queue = [(minx, miny, minz)]
visited = set()

while queue:
    x = queue[0][0]
    y = queue[0][1]
    z = queue[0][2]
    coord = (x, y, z)
    # print(coord)
    if coord in coords:
        visited.add(coord)
        queue.pop(0)
    else:
        all_coords.remove(coord)
        visited.add(coord)
        # Get neighbours
        n = (x - 1, y, z)
        if n not in visited and n not in queue:
            if not (x - 1 < minx):
                queue.append(n)
        n = (x + 1, y, z)
        if n not in visited and n not in queue:
            if not (x + 1 > maxx):
                queue.append(n)
        n = (x, y - 1, z)
        if n not in visited and n not in queue:
            if not (y - 1 < miny):
                queue.append(n)
        n = (x, y + 1, z)
        if n not in visited and n not in queue:
            if not (y + 1 > maxy):
                queue.append(n)
        n = (x, y, z - 1)
        if n not in visited and n not in queue:
            if not (z - 1 < minz):
                queue.append(n)
        n = (x, y, z + 1)
        if n not in visited and n not in queue:
            if not (z + 1 > maxz):
                queue.append(n)

        queue.pop(0)

print("Part 2:", len(all_coords) * 6 - get_answer(all_coords))
