with open('input.txt') as f:
    data = f.read()


def day6(unique):
    for i in range(len(data) - (unique - 1)):
        if len(set(data[i:i + unique])) == unique:
            return i + unique


print("\nDay 6")
print("Part 1:", day6(4))
print("Part 2:", day6(14))
