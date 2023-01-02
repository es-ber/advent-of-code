with open('input.txt') as f:
    elves = f.read().split('\n\n')

totals = []

for elf in elves:
    # Split each group of calories into a list, map each value to an integer, sum the result, append to totals
    calories = sum(list(map(int, elf.splitlines())))
    totals.append(calories)

print("\nDay 1")
print("Part 1:", max(totals))
print("Part 2:", sum(sorted(totals, reverse=True)[:3]))
