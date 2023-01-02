with open('input.txt') as f:
    rucksacks = f.read().splitlines()

    
# Map each letter to corresponding number
def map_score(all_common):
    common = None
    for item in all_common:
        if item.isupper():
            common = (ord(item) - ord("A") + 27)
        elif item.islower():
            common = (ord(item) - ord("a") + 1)

    return common

    
# Part 1
common1 = []

for rucksack in rucksacks:
    # Split item exactly in 2 in sets (to remove duplicates) and find intersection
    common_item = set(rucksack[len(rucksack) // 2:]).intersection(set(rucksack[:len(rucksack) // 2]))
    common1.append(map_score(common_item))

# Part 2
common2 = []

for i in range(0, len(rucksacks) - 1, 3):
    group = rucksacks[i:i + 3]
    common_item = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
    common2.append(map_score(common_item))

print("\nDay 3")
print("Part 1:", sum(common1))
print("Part 2:", sum(common2))