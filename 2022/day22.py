with open('input.txt') as f:
    map_in, path = f.read().split("\n\n")


def get_answer(part):
    
    # Map of directions:
    # R -> 0, D -> 1, L -> 2, U -> 3
    # Turning L changes facing by -1 (if facing becomes -1 then facing = 3 - use facing % 4)
    # Turning R changes facing by +1 (if facing becomes 4 then facing = 0 - use facing % 4)
    
    # Dictionary is in format:
    # "xy": [s, e, f]
    # Where x = old side number
    #       y = old facing
    #       s = new side number
    #       e = new edge (0 = right, 1 = bottom, 2 = left, 3 = top)
    #       f = new facing
    
    # Part 1
    if part == 1:
        side_wraps = {
            "10": [2, 2, 0],
            "11": [3, 3, 1],
            "12": [2, 0, 2],
            "13": [5, 1, 3],
            "20": [1, 2, 0],
            "21": [2, 3, 1],
            "22": [1, 0, 2],
            "23": [2, 1, 3],
            "30": [3, 2, 0],
            "31": [5, 3, 1],
            "32": [3, 0, 2],
            "33": [1, 1, 3],
            "40": [5, 2, 0],
            "41": [6, 3, 1],
            "42": [5, 0, 2],
            "43": [6, 1, 3],
            "50": [4, 2, 0],
            "51": [1, 3, 1],
            "52": [4, 0, 2],
            "53": [3, 1, 3],
            "60": [6, 2, 0],
            "61": [4, 3, 1],
            "62": [6, 0, 2],
            "63": [4, 1, 3]
        }

    # Part 2
    elif part == 2:
        side_wraps = {
            "10": [2, 2, 0],
            "11": [3, 3, 1],
            "12": [4, 2, 0],
            "13": [6, 2, 0],
            "20": [5, 0, 2],
            "21": [3, 0, 2],
            "22": [1, 0, 2],
            "23": [6, 1, 3],
            "30": [2, 1, 3],
            "31": [5, 3, 1],
            "32": [4, 3, 1],
            "33": [1, 1, 3],
            "40": [5, 2, 0],
            "41": [6, 3, 1],
            "42": [1, 2, 0],
            "43": [3, 2, 0],
            "50": [2, 0, 2],
            "51": [6, 0, 2],
            "52": [4, 0, 2],
            "53": [3, 1, 3],
            "60": [5, 1, 3],
            "61": [2, 3, 1],
            "62": [1, 3, 1],
            "63": [4, 1, 3]
        }

    # Starting position, side, and direction
    pos = (0, 50)
    side = 1
    facing = 0

    for move in instructions:

        # Moving forwards
        if type(move) == int:
            m = 0

            while m < move:

                # Change in coordinates depending on direction
                if facing == 0:
                    y = 0
                    x = 1
                elif facing == 1:
                    y = 1
                    x = 0
                elif facing == 2:
                    y = 0
                    x = -1
                elif facing == 3:
                    y = -1
                    x = 0

                # Get next position to move to
                next_pos = (pos[0] + y, pos[1] + x)

                # Determine relative coordinates of next position
                xr = next_pos[1] - side_bounds[side][2]
                yr = next_pos[0] - side_bounds[side][3]

                # Check if hit the edge of a side
                if (facing == 0 and next_pos[1] > side_bounds[side][facing]) or (
                        facing == 1 and next_pos[0] > side_bounds[side][facing]) or (
                        facing == 2 and next_pos[1] < side_bounds[side][facing]) or (
                        facing == 3 and next_pos[0] < side_bounds[side][facing]):

                    # Identify the new side
                    new_side = side_wraps[str(side) + str(facing)][0]
                    new_bounds = side_bounds[new_side]

                    # Identify the edge to come in on
                    new_edge = side_wraps[str(side) + str(facing)][1]

                    # Identify which way you will be facing (on the new side)
                    new_facing = side_wraps[str(side) + str(facing)][2]

                    # Identify position on new side
                    if facing == 0 and new_edge == 2:
                        new_x = new_bounds[2]
                        new_y = new_bounds[3] + yr
                    elif facing == 1 and new_edge == 3:
                        new_x = new_bounds[2] + xr
                        new_y = new_bounds[3]
                    elif facing == 2 and new_edge == 2:
                        new_x = new_bounds[2]
                        new_y = new_bounds[1] - yr
                    elif facing == 3 and new_edge == 2:
                        new_x = new_bounds[2]
                        new_y = new_bounds[3] + xr
                    elif facing == 0 and new_edge == 0:
                        new_x = new_bounds[0]
                        new_y = new_bounds[1] - yr
                    elif facing == 1 and new_edge == 0:
                        new_x = new_bounds[0]
                        new_y = new_bounds[3] + xr
                    elif facing == 2 and new_edge == 0:
                        new_x = new_bounds[0]
                        new_y = new_bounds[3] + yr
                    elif facing == 3 and new_edge == 1:
                        new_x = new_bounds[2] + xr
                        new_y = new_bounds[1]
                    elif facing == 0 and new_edge == 1:
                        new_x = new_bounds[2] + yr
                        new_y = new_bounds[1]
                    elif facing == 2 and new_edge == 3:
                        new_x = new_bounds[2] + yr
                        new_y = new_bounds[3]

                    next_pos = (new_y, new_x)

                    # If the next move forwards is a wall, don't move and break to next instruction
                    if map[next_pos[0]][next_pos[1]] == "#":
                        break

                    # Update facing and side once you know you have moved onto that side
                    facing = new_facing
                    side = new_side

                # If the next move forwards is a wall, don't move and break to next instruction
                if map[next_pos[0]][next_pos[1]] == "#":
                    break

                # Count move as having happened
                m += 1

                # Update current position
                pos = (next_pos[0], next_pos[1])

        # Turning
        else:
            if move == "L":
                facing = (facing - 1) % 4
            elif move == "R":
                facing = (facing + 1) % 4

    result = (1000 * (pos[0] + 1)) + (4 * (pos[1] + 1)) + facing

    return result


# Parsing map
map_in = map_in.splitlines()

map = []

for line in map_in:
    points = []
    for i in range(len(max(map_in, key=len))):
        if i < len(line):
            point = line[i]
        else:
            point = " "
        points.append(point)

    map.append(points)

# End parsing map

# Parsing path into instructions
i = 0
instructions = []

for _ in range(len(path)):
    move = ""
    turn = ""
    while i < len(path) and path[i].isnumeric():
        move += path[i]
        i += 1
    if move.isnumeric():
        move = int(move)
    if i < len(path) and path[i].isalpha():
        turn = path[i]
        i += 1

    if move != "":
        instructions.append(move)
    if turn != "":
        instructions.append(turn)

    if i >= len(path):
        break

# End parsing path

# Set up coordinates of edges of each side
# Order in list is [right, bottom, left, top] (matches order of directions)
#          indices [    0,      1,    2,   3]

side_bounds = {
    1: [99, 49, 50, 0],
    2: [149, 49, 100, 0],
    3: [99, 99, 50, 50],
    4: [49, 149, 0, 100],
    5: [99, 149, 50, 100],
    6: [49, 199, 0, 150]
}


print("\nDay 22")
print("Part 1:", get_answer(1))
print("Part 2:", get_answer(2))
