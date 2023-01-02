with open('input.txt') as f:
    jet = f.read()


def create_rock(shape, topy):
    rock = {}
    starty = topy + 4
    if shape == "bar":
        startx = 2
        rock = {
            "settled": False,
            "left": 0,
            "right": 3,
            "top": 0,
            "coords": [
                [startx, starty],
                [startx + 1, starty],
                [startx + 2, starty],
                [startx + 3, starty]
            ]
        }
    elif shape == "plus":
        startx = 3
        rock = {
            "settled": False,
            "left": 1,
            "right": 3,
            "top": 4,
            "coords": [
                [startx, starty],
                [startx - 1, starty + 1],
                [startx, starty + 1],
                [startx + 1, starty + 1],
                [startx, starty + 2]
            ]
        }
    elif shape == "corner":
        startx = 2
        rock = {
            "settled": False,
            "left": 0,
            "right": 4,
            "top": 4,
            "coords": [
                [startx, starty],
                [startx + 1, starty],
                [startx + 2, starty],
                [startx + 2, starty + 1],
                [startx + 2, starty + 2]
            ]
        }
    elif shape == "pipe":
        startx = 2
        rock = {
            "settled": False,
            "left": 0,
            "right": 0,
            "top": 3,
            "coords": [
                [startx, starty],
                [startx, starty + 1],
                [startx, starty + 2],
                [startx, starty + 3]
            ]
        }
    elif shape == "square":
        startx = 2
        rock = {
            "settled": False,
            "left": 0,
            "right": 3,
            "top": 3,
            "coords": [
                [startx, starty],
                [startx + 1, starty],
                [startx, starty + 1],
                [startx + 1, starty + 1]
            ]
        }

    return rock


def move_left(rocks, rock):
    if rock["coords"][rock["left"]][0] >= 1 and not any((coord[0] - 1, coord[1]) in rocks for coord in rock["coords"]):
        for i, coord in enumerate(rock["coords"]):
            x = coord[0] - 1
            y = coord[1]
            rock["coords"][i] = [x, y]

    return rock


def move_right(rocks, rock):
    if rock["coords"][rock["right"]][0] <= 5 and not any((coord[0] + 1, coord[1]) in rocks for coord in rock["coords"]):
        for i, coord in enumerate(rock["coords"]):
            x = coord[0] + 1
            y = coord[1]
            rock["coords"][i] = [x, y]

    return rock


def move_down(rocks, rock, topy):
    if not any((coord[0], coord[1] - 1) in rocks for coord in rock["coords"]):
        for i, coord in enumerate(rock["coords"]):
            x = coord[0]
            y = coord[1] - 1
            rock["coords"][i] = [x, y]
    else:
        for coord in rock["coords"]:
            rocks.add(tuple(coord))
            topy = max(rock["coords"][rock["top"]][1], topy)
            rock["settled"] = True

    return rock, rocks, topy


jetlen = len(jet)

# Starting maximum y coord
topy = 0

# Rock coordinates - starting with just floor
rocks = {(0, topy), (1, topy), (2, topy), (3, topy), (4, topy), (5, topy), (6, topy)}

jetnum = 0
rock_count = 0

# Count how often the jet stream resets and determine shape and jet at that point
reset_count = 0

# We want to track the shape, jet index, number of rocks, and height when each reset happens,
# and the previous states of these
reset_shape = "square"
reset_jetnum = jetlen
reset_rock_count = rock_count
reset_height = 0
prev_shape = None
prev_jetnum = None
prev_rock_count = None

heights = dict()

part1 = 0

while not (prev_shape == reset_shape and prev_jetnum == reset_jetnum) or rock_count < 2022:

    # Add rock
    rock_count += 1

    # Determine shape
    shape = ""
    if rock_count % 5 == 1:
        shape = "bar"
    elif rock_count % 5 == 2:
        shape = "plus"
    elif rock_count % 5 == 3:
        shape = "corner"
    elif rock_count % 5 == 4:
        shape = "pipe"
    elif rock_count % 5 == 0:
        shape = "square"

    # Create rock with correct shape/coordinates
    rock = create_rock(shape, topy)

    # Move rock
    while not rock["settled"]:
        if jet[jetnum] == "<":
            rock = move_left(rocks, rock)
            jetnum += 1
            if jetnum >= jetlen:
                reset_count += 1
                prev_rock_count = reset_rock_count
                prev_shape = reset_shape
                prev_jetnum = reset_jetnum
                prev_height = reset_height
                reset_shape = shape
                reset_jetnum = jetnum
                reset_rock_count = rock_count
                reset_height = topy
                jetnum = 0
            rock, rocks, topy = move_down(rocks, rock, topy)
        elif jet[jetnum] == ">":
            rock = move_right(rocks, rock)
            jetnum += 1
            if jetnum >= jetlen:
                reset_count += 1
                prev_rock_count = reset_rock_count
                prev_shape = reset_shape
                prev_jetnum = reset_jetnum
                prev_height = reset_height
                reset_shape = shape
                reset_jetnum = jetnum
                reset_rock_count = rock_count
                reset_height = topy
                jetnum = 0
            rock, rocks, topy = move_down(rocks, rock, topy)

    heights[rock_count] = topy

    if rock_count == 2022:
        part1 = topy

# Determine height after 1_000_000_000_000 rocks have fallen
# Total number of cycles:
cycles = (1000000000000 - prev_rock_count) // (reset_rock_count - prev_rock_count)
# Total number of rocks left after a complete number of cycles:
rocks_left = (1000000000000 - prev_rock_count) % (reset_rock_count - prev_rock_count)
# Final height
part2 = (heights[reset_rock_count] - heights[prev_rock_count]) * cycles + heights[prev_rock_count + rocks_left]

print("\nDay 17")
print("Part 1:", part1)
print("Part 2:", part2)
