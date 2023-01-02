with open('input.txt') as f:
    data = f.read().splitlines()

heights = []  # List of numeric mapping of input heights
paths = []  # List of path lengths
visited = set()  # Set of visited coordinates
start_point = []  # Starting point
end_point = []  # Ending point

# Set up data
for x in range(len(data[0])):

    row = []  # Coordinates on each row
    path_row = []  # Initial path heights (max height of path = number of coords - 1)

    for y in range(len(data)):

        # Start point
        if data[y][x] == "S":
            height = 1
            path = len(data[0]) * len(data) - 1
            start_point = [x, y]
        # End point
        elif data[y][x] == "E":
            height = 26
            path = 0
            end_point = [x, y]
        # All other points
        else:
            height = ord(data[y][x]) - ord("a") + 1
            path = len(data[0]) * len(data) - 1

        row.append(height)
        path_row.append(path)

    heights.append(row)
    paths.append(path_row)

# List of current coordinates to check - start from end point and work backwards
cc_list = [end_point]

visited.add(tuple(end_point))  # End point has been visited by definition

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # Possible directions to move

p = 0  # Steps taken (path length) so far

# While there's still coordinates left to check
while cc_list:
    # Check each direction in turn
    for direction in directions:
        # Check each coordinate in turn
        for cc in cc_list:
            # Mark the coordinate being checked as visited
            visited.add(tuple(cc))
            # Ensure there's a coordinate to move to for the given direction - do nothing if not
            if (cc[0] == 0 and direction[0] < 0) or (cc[1] == 0 and direction[1] < 0) or (
                    cc[0] == len(data[0]) - 1 and direction[0] > 0) or (cc[1] == len(data) - 1 and direction[1] > 0):
                pass
            else:
                height = heights[cc[0]][cc[1]]  # Get the height of the current coord
                new_coord = [cc[0] + direction[0], cc[1] + direction[1]]  # Get the coord to move to
                new_height = heights[new_coord[0]][new_coord[1]]  # Get the height of the new coord

                # Check you can move to the height - any lower and max one higher
                if new_height + 1 >= height:
                    # If the current path + 1 is less than the new coord's path then update new coord's path
                    if paths[cc[0]][cc[1]] + 1 < paths[new_coord[0]][new_coord[1]]:
                        paths[new_coord[0]][new_coord[1]] = paths[cc[0]][cc[1]] + 1

    p += 1  # Increase path length by one step

    # Reset list of coords to check for next pass
    cc_list = []

    # Cycle through each coordinate
    for i in range(len(paths)):
        for j in range(len(paths[0])):
            # Only look for the path values of coordinates not yet visited
            if (i, j) not in visited:
                # Add any coordinates with the next path length that have not been visited to the list to check
                if paths[i][j] == p:
                    cc_list.append([i, j])

print("\nDay 12")

# Get the path length from the end point to the start point
print("Part 1:", paths[start_point[0]][start_point[1]])

# Cycle through each coordinate to get the shortest path to any "a" value
part2 = len(data[0]) * len(data) - 1
for a in range(len(paths)):
    for b in range(len(paths[0])):
        if heights[a][b] == 1:
            if part2 > paths[a][b]:
                part2 = paths[a][b]

print("Part 2:", part2)
