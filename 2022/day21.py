import re

with open('input.txt') as f:
    data = f.read().splitlines()


def get_answer(part, data):

    monk_calc = dict()

    # Dictionary of monkeys (keys) and their calculations/numbers (values)
    for line in data:
        monkey, calc = line.split(": ")

        monk_calc[monkey] = calc

    # Replace original root operator with == for comparison
    if part == 2:
        root_op_index = re.search('[+\-*/]', monk_calc.get("root")).start()
        root_op = monk_calc.get("root")[root_op_index]
        monk_calc["root"] = monk_calc.get("root").replace(root_op, "==")

    # Find first instance of monkey string in root
    match = re.search('[a-zA-Z]', monk_calc.get("root"))

    # While there's still strings left to replace in root
    while match is not None:
        # Find the position of the string to replace
        index = match.start()

        # Get the value of the string to replace
        lookup = monk_calc.get("root")[index:index + 4]

        # If the human monkey, temp replace with non-alphanumeric placeholder
        if lookup == "humn":
            value = "."
        # Otherwise find value of monkey to look up
        else:
            value = monk_calc.get(lookup)
        # Replace value in string with lookup monkey calculation/number
        monk_calc["root"] = monk_calc.get("root").replace(lookup, "(" + value + ")")

        match = re.search('[a-zA-Z]', monk_calc.get("root"))

    # Put actual value of humn back in and evaluate the final calculation
    if part == 1:
        monk_calc["root"] = monk_calc.get("root").replace(".", "(" + monk_calc.get("humn") + ")")

        calc = monk_calc.get("root")

        result = eval(calc)
        print("Part 1:", int(result))

    if part == 2:
        # Split the calculation into the two sides
        left, right = monk_calc.get("root").split(" == ")

        # Check which side has the humn (.) value to be calculated
        if re.search('[.]', left) is not None:
            humn = "left"
        else:
            humn = "right"

        # Update calculation to put humn part on left and evaluated answer of other part on right of equation
        if humn == "left":
            ans = str(int(eval(right)))
            left = left[1:len(left) - 1]
            calc = left + " = " + ans
        else:
            ans = str(int(eval(left)))
            right = right[1:len(right) - 1]
            calc = right + " = " + ans

        while True:

            # Find positions of brackets to determine where to split
            istart = []  # Stack of indices of opening parentheses
            d = {}

            for i, c in enumerate(calc):
                if c == '(':
                    istart.append(i)
                if c == ')':
                    d[istart.pop()] = i

            # Split into left and right side of left calculation, operator, and answer
            left = calc[0:d.get(0) + 1]
            op = calc[d.get(0) + 2]
            right_b = d.get(0) + 4  # Starting bracket position for right side
            right = calc[right_b:d.get(right_b) + 1]
            ans = calc[d.get(right_b) + 4:]

            # Reverse operators for new calculations
            if op == "/":
                new_op = "*"
            elif op == "*":
                new_op = "/"
            elif op == "+":
                new_op = "-"
            elif op == "-":
                new_op = "+"

            # Check which side has the humn (.) value to be calculated
            if re.search('[.]', left) is not None:
                humn = "left"
            else:
                humn = "right"

            # Move the non-humn side to the right and evaluate the new answer and new calculation
            if humn == "left":
                new_right = ans + new_op + right
                new_ans = str(int(eval(new_right)))
                left = left[1:len(left) - 1]
                calc = left + " = " + new_ans

                # Calculation is finished once the humn side is just the . (humn replacement)
                if left == ".":
                    print("Part 2:", int(new_ans))
                    break

            # Extra manipulation of both sides required to ensure positive humn value on left side
            # and correctly calculated answer on right side of new calculation
            else:
                new_left = right[1:len(right) - 1]

                if op == "+" or op == "*":
                    new_right = ans + new_op + left
                    new_ans = str(int(eval(new_right)))
                elif op == "-":
                    new_right = "-(" + ans + "-" + left + ")"
                    new_ans = str(int(eval(new_right)))
                elif op == "/":
                    new_right = left + "/" + ans
                    new_ans = str(int(eval(new_right)))

                calc = new_left + " = " + new_ans

                # Calculation is finished once the humn side is just the . (humn replacement)
                if right == ".":
                    print("Part 2:", int(new_ans))
                    break

print("\nDay 21")
get_answer(1, data)
get_answer(2, data)
