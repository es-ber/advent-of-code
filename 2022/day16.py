from itertools import combinations

with open('input.txt') as f:
    data = f.read().splitlines()


def dfs(time, valve, opened):
    if (time, valve, tuple(sorted(opened))) in cache:
        return cache[(time, valve, tuple(sorted(opened)))]

    max_flow = 0
    for next_valve in distances[valve]:
        if next_valve in opened:
            continue
        time_left = time - distances[valve][next_valve] - 1
        if time_left <= 0:
            continue
        opened.append(next_valve)
        max_flow = max(max_flow, dfs(time_left, next_valve, sorted([x for x in opened])) + valves[next_valve] * time_left)
        opened.pop()

    cache[(time, valve, tuple(sorted(opened)))] = max_flow
    
    return max_flow


valves = dict()
neighbours = dict()

# Get dictionaries of valves: flows and valves: neighbours
for line in data:
    words = line.split(" ")
    halves = words[4][0:-1]
    if words[5] == "tunnels":
        neighbour = line.split("tunnels lead to valves ")[1].split(", ")
    elif words[5] == "tunnel":
        neighbour = line.split("tunnel leads to valve ")[1].split(", ")
    else:
        neighbour = ""

    valve = words[1]
    flow = int(halves[5:])

    valves[valve] = flow
    neighbours[valve] = neighbour

flow_valves = []
distances = dict()

# Use BFS to determine minimum paths from AA and any non-zero valves to each other
for valve in valves:
    # Only process for AA and any non-zero valves
    if valves[valve] != 0 or valve == "AA":
        targets = neighbours[valve]
        # Valves with any flow
        if valve != "AA":
            flow_valves.append(valve)
        dist = 0
        Q = []
        for target in targets:
            Q.append((target, dist + 1))
        visited = dict()
        visited[valve] = dist

        while Q:
            next_valve = Q[0][0]
            targets = neighbours[next_valve]
            dist = Q[0][1]
            # For all the targets of the current valve, if not already visited or in queue, add to queue
            for target in targets:
                if not (target in list(visited.keys())) and not (target in list(x[0] for x in Q)):
                    Q.append((target, dist + 1))
            visited[next_valve] = Q[0][1]
            Q.pop(0)

        # Ditch the 0 flow valves and the current valve from the visited distances into a dict of actual distances
        distance = dict()
        for key in visited:
            if key != valve and valves[key] != 0:
                distance[key] = visited[key]

        distances[valve] = distance

indices = {}

for index, element in enumerate(flow_valves):
    indices[element] = index

cache = {}

opened = []

print("\nDay 16")
print("Part 1:", dfs(30, "AA", []))

# All combinations of valves split between elephant and human
all_comb = []

for i in range(len(flow_valves)//2 + 1):
    comb = list(combinations(flow_valves, i))
    all_comb += comb

part2 = 0

# Get optimal total flow across elephant and human and all valve combinations
for j in all_comb:
    human = list(j)
    elephant = [x for x in flow_valves if x not in human]

    part2 = max(part2, dfs(26, "AA", human) + dfs(26, "AA", elephant))

print("Part 2:", part2)
