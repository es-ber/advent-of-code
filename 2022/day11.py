from math import prod

with open('input.txt') as f:
    monkey_data = f.read().split("\n\n")

    
def monkey_business(part, rounds):
    items = []
    for monkey in monkey_data:
        items_ = monkey.splitlines()[1]
        items.append(items_.strip()[16:].split(", "))

    inspect_count = [0 for _ in range(len(test))]
    divisor = prod(test)
    round_no = 0

    while round_no < rounds:
        for i in range(len(test)):
            if items[i]:
                for _ in range(len(items[i])):
                    inspect_count[i] += 1

                    items[i][0] = eval("int(items[i][0]) " + op[i])
                    if part == 1:
                        items[i][0] = items[i][0] // 3
                    elif part == 2:
                        items[i][0] = items[i][0] % divisor

                    if items[i][0] % test[i] == 0:
                        eval("items[" + m_true[i] + "].append(items[i][0])")
                        items[i].pop(0)
                    else:
                        eval("items[" + m_false[i] + "].append(items[i][0])")
                        items[i].pop(0)

        round_no += 1

    inspect_count = sorted(inspect_count, reverse=True)

    return inspect_count[0] * inspect_count[1]


op = []
test = []
m_true = []
m_false = []

for monkey in monkey_data:
    lines = monkey.splitlines()
    op.append(lines[2].strip()[21:])
    test.append(int(lines[3].strip()[19:]))
    m_true.append(lines[4].strip()[25:])
    m_false.append(lines[5].strip()[26:])

for o in range(len(op)):
    if op[o] == "* old":
        op[o] = "** 2"

print("\nDay 11")
print("Part 1:", monkey_business(part=1, rounds=20))
print("Part 2:", monkey_business(part=2, rounds=10000))
