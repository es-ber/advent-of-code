with open('input.txt') as f:
    data = f.read().split("\n\n")

    
# Move the crates using the given instructions
def move_crates(reverse):
    crate_rows = []

    for row_in in crate_rows_in:
        row = []
        for i in range(1, max_length, 4):
            crate = row_in[i:i + 1]
            row.append(crate)
        crate_rows.append(row)

    crate_rows.reverse()

    crates_temp = list(zip(*crate_rows))

    crates = []

    for col in crates_temp:
        temp = []
        for j in range(num_rows):
            if col[j] != " ":
                temp.append(col[j])
        crates.append(temp)

    for move in moves:
        crate = crates[move[1]][-move[0]:]
        if reverse:
            crate.reverse()
        del crates[move[1]][-move[0]:]
        crates[move[2]].extend(crate)

    return crates

    
# Find the top crate in each column and combine
def find_top_crates(crates):
    top_crates = ""

    for stack in crates:
        top_crates += stack[-1]

    return top_crates

    
# Separate out crates part of the input in original format and drop the column numbers row
crate_rows_in = data[0].splitlines()
del crate_rows_in[-1]

# The maximum length of the original crate input to split out into columns of only crate letters
max_length = len(max(crate_rows_in, key=len))

# Determine how many rows deep the crates are stacked
num_rows = len(crate_rows_in)

# Separate out the moves part of the input in original format
all_moves = data[1].splitlines()

moves = []

# Format original moves input to make usable for applying instructions
for move in all_moves:
    instruction = []
    move = move.split(" ")
    for word in move:
        if word.isnumeric():
            instruction.append(int(word))
    for k in range(len(instruction)):
        if k > 0:
            instruction[k] = instruction[k] - 1
    moves.append(instruction)

print("\nDay 5")

# Part 1
crates = move_crates(reverse=True)
top_crates = find_top_crates(crates)
print("Part 1:", top_crates)

# Part 2
crates = move_crates(reverse=False)
top_crates = find_top_crates(crates)
print("Part 2:", top_crates)
