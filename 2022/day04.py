import re

with open('input.txt') as f:
    data = f.read().splitlines()

count1 = 0
count2 = 0

for item in data:
    # Split each item on , and - into a list, map results to an integer, and convert back to a list
    values = list(map(int, re.split("[,-]+", item)))
    # Check for full overlaps
    if (values[0] <= values[2] and values[1] >= values[3]) or (values[0] >= values[2] and values[1] <= values[3]):
        count1 += 1
    # Check for partial overlaps
    if values[1] >= values[2] and values[0] <= values[3]:
        count2 += 1

print("\nDay 4")
print("Part 1:", count1)
print("Part 2:", count2)
