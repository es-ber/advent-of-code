with open('input.txt') as f:
    data = f.read().splitlines()


def move_b_up(b_up):
    for i, bliz in enumerate(b_up):
        if bliz[1] - 1 == top_edge:
            b_up[i] = (bliz[0], bottom_edge - 1)
        else:
            b_up[i] = (bliz[0], bliz[1] - 1)

    return b_up


def move_b_down(b_down):
    for i, bliz in enumerate(b_down):
        if bliz[1] + 1 == bottom_edge:
            b_down[i] = (bliz[0], top_edge + 1)
        else:
            b_down[i] = (bliz[0], bliz[1] + 1)

    return b_down


def move_b_left(b_left):
    for i, bliz in enumerate(b_left):
        if bliz[0] - 1 == left_edge:
            b_left[i] = (right_edge - 1, bliz[1])
        else:
            b_left[i] = (bliz[0] - 1, bliz[1])

    return b_left


def move_b_right(b_right):
    for i, bliz in enumerate(b_right):
        if bliz[0] + 1 == right_edge:
            b_right[i] = (left_edge + 1, bliz[1])
        else:
            b_right[i] = (bliz[0] + 1, bliz[1])

    return b_right

    
top_edge = 0
bottom_edge = len(data) - 1
left_edge = 0
right_edge = len(data[0]) - 1

b_up = []
b_down = []
b_left = []
b_right = []

start = ()
end = ()

for y, line in enumerate(data):
    if line[:3] == "#.#":
        start = (left_edge + 1, 0)
    elif line[-3:] == "#.#":
        end = (right_edge - 1, bottom_edge)
    else:
        for x in range(left_edge + 1, right_edge):
            if line[x] == "^":
                b_up.append((x, y))
            elif line[x] == "v":
                b_down.append((x, y))
            elif line[x] == "<":
                b_left.append((x, y))
            elif line[x] == ">":
                b_right.append((x, y))

all_b = set(tuple(b_up) + tuple(b_down) + tuple(b_left) + tuple(b_right))

# Time (moves), and queue with starting position
m = 0
Q = [(start[0], start[1], 0)]

visited = set()

min_m = right_edge * bottom_edge

i = 0

b_moves = 0

while Q:

    # Get position to check
    pos = Q[0]

    # Drop this from current Q as we're doing it now
    Q.pop(0)

    # If we've already been at this position with this state of blizzards then continue
    if (pos[0], pos[1], pos[2] % 600) in visited:
        continue

    # We have visited this position at this time
    visited.add((pos[0], pos[1], pos[2] % 600))  # Assumption on lowest common multiplier of input height * width

    # Get current moves
    m = pos[2] + 1

    while not (b_moves == m):

        # Move all blizzards by one
        b_up = move_b_up(b_up)
        b_down = move_b_down(b_down)
        b_left = move_b_left(b_left)
        b_right = move_b_right(b_right)

        # All unique blizzard locations after moving
        all_b = set(tuple(b_up) + tuple(b_down) + tuple(b_left) + tuple(b_right))

        b_moves += 1

    # Check if moving down would get you to your end point, mark current minimum m and continue to next move if so
    if (pos[0], pos[1] + 1) == end:
        min_m = m
        break

    # Check if you can stay in same place and add to queue if so
    if not (pos[:2] in all_b):
        Q.append((pos[0], pos[1], m))

    # Check if moving up would take you to the starting position and add to queue if so
    if (pos[0], pos[1] - 1) == start:
        Q.append((pos[0], pos[1] - 1, m))

    # Check if you can move up (other than starting position) and add to queue if so
    elif pos[1] - 1 > top_edge and not ((pos[0], pos[1] - 1) in all_b):
        Q.append((pos[0], pos[1] - 1, m))

    # Check if you can move down and add to queue if so
    if pos[1] + 1 < bottom_edge and not ((pos[0], pos[1] + 1) in all_b):
        Q.append((pos[0], pos[1] + 1, m))

    # Check if you can move left and add to queue if so
    if pos[1] != top_edge and pos[1] != bottom_edge and pos[0] - 1 > left_edge and not ((pos[0] - 1, pos[1]) in all_b):
        Q.append((pos[0] - 1, pos[1], m))

    # Check if you can move right and add to queue if so
    if pos[1] != top_edge and pos[1] != bottom_edge and pos[0] + 1 < right_edge and not ((pos[0] + 1, pos[1]) in all_b):
        Q.append((pos[0] + 1, pos[1], m))

print("\nDay 24")
print("Part 1:", min_m)

Q = [(end[0], end[1], min_m)]

visited = set()

min_m = right_edge * bottom_edge

i = 0

while Q:

    # Get position to check
    pos = Q[0]

    # Drop this from current Q as we're doing it now
    Q.pop(0)

    if (pos[0], pos[1], pos[2] % 600) in visited:
        continue

    # We have visited this position
    visited.add((pos[0], pos[1], pos[2] % 600))  # Assumption on lowest common multiplier of input height * width

    # Get current moves
    m = pos[2] + 1

    while not (b_moves == m):

        # Move all blizzards by one
        b_up = move_b_up(b_up)
        b_down = move_b_down(b_down)
        b_left = move_b_left(b_left)
        b_right = move_b_right(b_right)

        # All unique blizzard locations after moving
        all_b = set(tuple(b_up) + tuple(b_down) + tuple(b_left) + tuple(b_right))

        b_moves += 1

    # Check if moving up would get you to your start point, mark current minimum m and continue to next move if so
    if (pos[0], pos[1] - 1) == start:
        min_m = m
        break

    # Check if you can stay in same place and add to queue if so
    if not (pos[:2] in all_b):
        Q.append((pos[0], pos[1], m))

    # Check if you can move up and add to queue if so
    if pos[1] - 1 > top_edge and not ((pos[0], pos[1] - 1) in all_b):
        Q.append((pos[0], pos[1] - 1, m))

    # Check if moving down would take you to the ending position and add to queue if so
    if (pos[0], pos[1] + 1) == end:
        Q.append((pos[0], pos[1] + 1, m))

    # Check if you can move down (other than to end) and add to queue if so
    elif pos[1] + 1 < bottom_edge and not ((pos[0], pos[1] + 1) in all_b):
        Q.append((pos[0], pos[1] + 1, m))

    # Check if you can move left and add to queue if so
    if pos[1] != top_edge and pos[1] != bottom_edge and pos[0] - 1 > left_edge and not ((pos[0] - 1, pos[1]) in all_b):
        Q.append((pos[0] - 1, pos[1], m))

    # Check if you can move right and add to queue if so
    if pos[1] != top_edge and pos[1] != bottom_edge and pos[0] + 1 < right_edge and not ((pos[0] + 1, pos[1]) in all_b):
        Q.append((pos[0] + 1, pos[1], m))

    i += 1

Q = [(start[0], start[1], min_m)]

visited = set()

min_m = right_edge * bottom_edge

i = 0

while Q:

    # Get position to check
    pos = Q[0]

    # Drop this from current Q as we're doing it now
    Q.pop(0)

    if (pos[0], pos[1], pos[2] % 600) in visited:
        continue

    # We have visited this position
    visited.add((pos[0], pos[1], pos[2] % 600))  # Assumption on lowest common multiplier of input height * width

    # Get current moves
    m = pos[2] + 1

    while not (b_moves == m):

        # Move all blizzards by one
        b_up = move_b_up(b_up)
        b_down = move_b_down(b_down)
        b_left = move_b_left(b_left)
        b_right = move_b_right(b_right)

        # All unique blizzard locations after moving
        all_b = set(tuple(b_up) + tuple(b_down) + tuple(b_left) + tuple(b_right))

        b_moves += 1

    # Check if moving down would get you to your end point, mark current minimum m and continue to next move if so
    if (pos[0], pos[1] + 1) == end:
        min_m = m
        break

    # Check if you can stay in same place and add to queue if so
    if not (pos[:2] in all_b):
        Q.append((pos[0], pos[1], m))

    # Check if moving up would take you to the starting position and add to queue if so
    if (pos[0], pos[1] - 1) == start:
        Q.append((pos[0], pos[1] - 1, m))

    # Check if you can move up (other than starting position) and add to queue if so
    elif pos[1] - 1 > top_edge and not ((pos[0], pos[1] - 1) in all_b):
        Q.append((pos[0], pos[1] - 1, m))

    # Check if you can move down and add to queue if so
    if pos[1] + 1 < bottom_edge and not ((pos[0], pos[1] + 1) in all_b):
        Q.append((pos[0], pos[1] + 1, m))

    # Check if you can move left and add to queue if so
    if pos[1] != top_edge and pos[1] != bottom_edge and pos[0] - 1 > left_edge and not ((pos[0] - 1, pos[1]) in all_b):
        Q.append((pos[0] - 1, pos[1], m))

    # Check if you can move right and add to queue if so
    if pos[1] != top_edge and pos[1] != bottom_edge and pos[0] + 1 < right_edge and not ((pos[0] + 1, pos[1]) in all_b):
        Q.append((pos[0] + 1, pos[1], m))

print("Part 2:", min_m)
