from operator import add, sub

# Read in instructions
with open('input.txt') as f:
    instruction = f.read().splitlines()


def all_moves(tail_knots):
    # Starting positions for all knots
    k = [[0 for _ in range(2)] for _ in range(tail_knots + 1)]

    # Set for all final tail positions
    ts = set()

    # Move each tail
    def move_tail(tn):
        # Distance of tail from next knot
        diff = list(map(sub, k[tn - 1], k[tn]))

        # Update position of tail only if either direction > 1 away
        if max(diff) > 1 or min(diff) < -1:
            move = [None, None]
            if diff[0] > 0:
                move[0] = 1
            elif diff[0] < 0:
                move[0] = -1
            else:
                move[0] = 0
            if diff[1] > 0:
                move[1] = 1
            elif diff[1] < 0:
                move[1] = -1
            else:
                move[1] = 0
            new = list(map(add, k[tn], move))
        else:
            new = k[tn]

        return new

    for line in instruction:
        md, mn = line.split()
        mn = int(mn)

        # Move head value by 1 in given direction
        # To be looped for mn moves after all tail moves for each move
        for m in range(1, mn + 1):
            k[0][0] += mx[md]
            k[0][1] += my[md]

            # Loop through tails i.e. K1 - Kn
            for t in range(1, tail_knots + 1):
                k[t] = move_tail(t)

            ts.add(tuple(k[tail_knots]))

    return ts

    
# Map distances to move
mx = {"U": 0, "R": 1, "D": 0, "L": -1}
my = {"U": 1, "R": 0, "D": -1, "L": 0}

print("\nDay 9")
print("Part 1:", len(all_moves(1)))
print("Part 2:", len(all_moves(9)))
