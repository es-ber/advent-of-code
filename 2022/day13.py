import re

with open('input.txt') as f:
    data = f.read().split("\n\n")


def compare(packet1, packet2):
    if type(packet1) == int and type(packet2) == int:
        if packet1 == packet2:
            return 0
        elif packet1 < packet2:
            return 1
        else:
            return -1
    elif type(packet1) == list and type(packet2) == list:
        comp = None
        for j in range(min(len(packet1), len(packet2))):
            comp = compare(packet1[j], packet2[j])
            if comp == 1:
                return 1
            elif comp == -1:
                return -1
        if comp == 0:
            if len(packet1) < len(packet2):
                return 1
            elif len(packet2) < len(packet1):
                return -1
        elif comp is None:
            if len(packet1) == 0 and len(packet2) != 0:
                return 1
            elif len(packet2) == 0 and len(packet1) != 0:
                return -1
    elif type(packet1) == int and type(packet2) == list:
        comp = compare([packet1], packet2)
        if comp == 1:
            return 1
        elif comp == -1:
            return -1
    elif type(packet1) == list and type(packet2) == int:
        comp = compare(packet1, [packet2])
        if comp == 1:
            return 1
        elif comp == -1:
            return -1


all_packets = []
outcome = None
result = 0

for i, line in enumerate(data, 1):
    packet1, packet2 = line.splitlines()
    all_packets.append(packet1)
    all_packets.append(packet2)

    packet1 = eval(packet1)
    packet2 = eval(packet2)

    outcome = compare(packet1, packet2)

    if outcome == 1:
        result += i

print("\nDay 13")
print("Part 1:", result)

# Part 2
# Get first number from each packet
all_numbers = []
for packet in all_packets:

    new_packet = str(packet.replace("[]", "-00"))

    if bool(re.search(r'-?\d', new_packet)):
        number = re.search(r'-?\d+', new_packet).group()
        if number == "-00":
            all_numbers.append(None)
        else:
            all_numbers.append(int(number))
    else:
        all_numbers.append(None)

# Add in 2 and 6 as divider packets
all_numbers.append(2)
all_numbers.append(6)

# Find the smallest number and replace "None" cases with number smaller than this
min_num = None
for num in all_numbers:
    if num is not None:
        if min_num is None:
            min_num = num
        else:
            min_num = min(min_num, num)

for i, num in enumerate(all_numbers):
    if num is None:
        all_numbers[i] = min_num - 1

# Sort data
all_numbers = sorted(all_numbers)

# Find first instance of each divider number - this is where the divider packets end up with sorting by definition
index1 = None
for i, num in enumerate(all_numbers):
    if num == 2:
        index1 = i + 1
        break

index2 = None
for i, num in enumerate(all_numbers):
    if num == 6:
        index2 = i + 1
        break

print("Part 2:", index1*index2)
