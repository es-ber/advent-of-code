with open('input.txt') as f:
    orig = f.read().splitlines()

with open('input.txt') as f:
    new = f.read().splitlines()


def get_answer(part, orig, new):

    if part == 1:
        multi = 1
    elif part == 2:
        multi = 811589153

    orig = [int(x) * multi for x in orig]
    new = list(enumerate([int(x) * multi for x in new]))

    index0 = orig.index(0)

    for _ in range(10 if part == 2 else 1):
        for i, val in enumerate(orig):

            while new[0] != (i, val):
                new.append(new[0])
                new.pop(0)

            index = new[0][1] % (len(orig) - 1) + 1

            new.insert(index, new[0])
            new.pop(0)

    new_index0 = new.index((index0, 0))

    ans = 0

    for index_chk in [1000, 2000, 3000]:
        ans += new[(index_chk + new_index0) % len(orig)][1]

    return ans


print("\nDay 20")
print("Part 1:", get_answer(1, orig, new))
print("Part 2:", get_answer(2, orig, new))
