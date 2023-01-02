with open('input.txt') as f:
    data = f.read().splitlines()

# Set starting total to first number and remove from list
total = data[0]
data.pop(0)

# Add each item in turn
for line in data:

    # Reset carry over and interim result
    carry = 0
    result = ""

    # Read in each value of current total and next number to add from right to left
    # Convert - and = to decimal numbers
    for i in range(1, max(len(line), len(total)) + 1):

        if i > len(total):
            tot = 0
        else:
            tot = total[-i]
            if tot == "=":
                tot = -2
            elif tot == "-":
                tot = -1
            else:
                tot = int(tot)

        if i > len(line):
            add = 0
        else:
            add = line[-i]
            if add == "=":
                add = -2
            elif add == "-":
                add = -1
            else:
                add = int(add)

        # Get sum of numbers for current column and add any carry over
        sum = tot + add + carry

        # Update sum and determine carry over if out of bounds
        if sum == -5:
            carry = -1
            sum = 0
        elif sum == -4:
            carry = -1
            sum = 1
        elif sum == -3:
            carry = -1
            sum = 2
        elif sum == 3:
            carry = 1
            sum = -2
        elif sum == 4:
            carry = 1
            sum = -1
        elif sum == 5:
            carry = 1
            sum = 0
        elif sum == 6:
            carry = 1
            sum = 1
        else:
            carry = 0

        # Convert decimal numbers back to system and concatenate to result
        if sum == -2:
            result += "="
        elif sum == -1:
            result += "-"
        else:
            result += str(sum)

    # Reverse result to get new total as they were concatenated right to left and need to read left to right
    total = result[::-1]

# Final total
print("\nDay 25")
print("Part 1:", total)
