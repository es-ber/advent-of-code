with open('input.txt') as f:
    data = f.read().splitlines()


def north(x, y, pos):
    if [x - 1, y - 1] in pos or [x, y - 1] in pos or [x + 1, y - 1] in pos:
        return False
    else:
        return True


def south(x, y, pos):
    if [x - 1, y + 1] in pos or [x, y + 1] in pos or [x + 1, y + 1] in pos:
        return False
    else:
        return True


def east(x, y, pos):
    if [x + 1, y - 1] in pos or [x + 1, y] in pos or [x + 1, y + 1] in pos:
        return False
    else:
        return True


def west(x, y, pos):
    if [x - 1, y - 1] in pos or [x - 1, y] in pos or [x - 1, y + 1] in pos:
        return False
    else:
        return True


def move_elf(new, pos, new_pos, dups, elf):
    # If the potential new position is already taken by another elf, don't move either elf
    if new in new_pos:
        index = new_pos.index(new)  # Get index of existing one in new_pos and replace that with old elf pos
        new_pos[index] = pos[index]
        new_pos.append(elf)  # Then put old elf pos for this one into new_pos
        dups.append(new)  # And also add this new_pos to dups
    elif new in dups:
        new_pos.append(elf)  # Put old elf pos for this one into new_pos
    else:
        new_pos.append(new)

    return new_pos, dups


def get_answer(part, pos):
    i = 0
    while True:

        i += 1

        new_pos = []
        dups = []

        # Check each elf and move as required
        for elf in pos:

            x = elf[0]
            y = elf[1]

            # Check if elf has any other elf around it
            if [x - 1, y - 1] in pos or [x, y - 1] in pos or [x + 1, y - 1] in pos or [x - 1, y] in pos \
                    or [x + 1, y] in pos or [x - 1, y + 1] in pos or [x, y + 1] in pos or [x + 1, y + 1] in pos:

                if i % 4 == 1:
                    if north(x, y, pos):
                        new_pos, dups = move_elf([x, y - 1], pos, new_pos, dups, elf)

                    elif south(x, y, pos):
                        new_pos, dups = move_elf([x, y + 1], pos, new_pos, dups, elf)

                    elif west(x, y, pos):
                        new_pos, dups = move_elf([x - 1, y], pos, new_pos, dups, elf)

                    elif east(x, y, pos):
                        new_pos, dups = move_elf([x + 1, y], pos, new_pos, dups, elf)

                    else:
                        new_pos.append([x, y])

                elif i % 4 == 2:
                    if south(x, y, pos):
                        new_pos, dups = move_elf([x, y + 1], pos, new_pos, dups, elf)

                    elif west(x, y, pos):
                        new_pos, dups = move_elf([x - 1, y], pos, new_pos, dups, elf)

                    elif east(x, y, pos):
                        new_pos, dups = move_elf([x + 1, y], pos, new_pos, dups, elf)

                    elif north(x, y, pos):
                        new_pos, dups = move_elf([x, y - 1], pos, new_pos, dups, elf)

                    else:
                        new_pos.append([x, y])

                elif i % 4 == 3:
                    if west(x, y, pos):
                        new_pos, dups = move_elf([x - 1, y], pos, new_pos, dups, elf)

                    elif east(x, y, pos):
                        new_pos, dups = move_elf([x + 1, y], pos, new_pos, dups, elf)

                    elif north(x, y, pos):
                        new_pos, dups = move_elf([x, y - 1], pos, new_pos, dups, elf)

                    elif south(x, y, pos):
                        new_pos, dups = move_elf([x, y + 1], pos, new_pos, dups, elf)

                    else:
                        new_pos.append([x, y])

                elif i % 4 == 0:
                    if east(x, y, pos):
                        new_pos, dups = move_elf([x + 1, y], pos, new_pos, dups, elf)

                    elif north(x, y, pos):
                        new_pos, dups = move_elf([x, y - 1], pos, new_pos, dups, elf)

                    elif south(x, y, pos):
                        new_pos, dups = move_elf([x, y + 1], pos, new_pos, dups, elf)

                    elif west(x, y, pos):
                        new_pos, dups = move_elf([x - 1, y], pos, new_pos, dups, elf)

                    else:
                        new_pos.append([x, y])

            # If no adjacent elf, do not move elf - just give new position same as old
            else:
                new_pos.append([x, y])

        if new_pos == pos:
            break

        pos = []
        for val in new_pos:
            pos.append(val)

        print(i)

        if part == 1 and i == 10:
            break

    minx = min(p[0] for p in pos)
    maxx = max(p[0] for p in pos)
    miny = min(p[1] for p in pos)
    maxy = max(p[1] for p in pos)
    area = (maxx - minx + 1) * (maxy - miny + 1)
    elves = len(pos)

    if part == 1:
        return area - elves
    elif part == 2:
        return i


# Map positions of elves
pos = []

for y in range(len(data)):
    for x in range(len(data[0])):
        if data[y][x] == "#":
            pos.append([x, y])
            
print("\nDay 23")
print("Part 1:", get_answer(1, pos))
print("Part 2:", get_answer(2, pos))
