with open('input.txt') as f:
    data = f.read().splitlines()

x, total = 1, 0
cycles = [0, 1]

for line in data:
    if line == "noop":
        cycles.append(x)
    else:
        cycles.append(x)
        x += int(line.split()[1])
        cycles.append(x)

for c in range(20, 221, 40):
    total += c * cycles[c]

print("\nDay 10")
print("Part 1:", total)

cycles.pop(0)
print("Part 2:")
for i in range(6):
    row = ""
    for j in range(40):
        c = i * 40 + j
        if cycles[c] - 1 <= j <= cycles[c] + 1:
            row += "█"
        else:
            row += " "

    print(row)
