with open('input.txt') as f:
    data = f.read().splitlines()

path = []
all_totals = dict()

for line in data:
    words = line.split(" ")
    # Determine current path
    if len(words) == 3:
        if words[2] == "/":
            path.append(" ")
        elif words[2] == "..":
            path.pop()
        elif words[2].isalpha():
            path.append(words[2])
    else:
        if words[0] == "dir":
            continue
        elif words[0] == "$" and words[1] == "ls":
            continue
        # When at a file, add the size of this to the current path and all higher level paths within the dictionary
        elif words[0].isnumeric():
            for i in range(1, len(path) + 1):
                if tuple(path[:i]) in all_totals:
                    all_totals[tuple(path[:i])] += int(words[0])
                else:
                    all_totals[tuple(path[:i])] = int(words[0])

max_total = 0
part1 = 0
part2 = 70000000

# Find the sum of the sizes as needed for part 1 and find the overall size for part 2
for total in all_totals:
    if all_totals[total] < 100000:
        part1 += all_totals[total]
    max_total = max(max_total, all_totals[total])

# Determine the potential overall size if each path was deleted and find the minimum that frees up enough space
for total in all_totals:
    potential = 70000000 - max_total + all_totals[total]
    if potential >= 30000000:
        part2 = min(part2, all_totals[total])

print("\nDay 7")
print("Part 1:", part1)
print("Part 2:", part2)
