with open('input.txt') as f:
    data = f.read().splitlines()


def make_robot(i, max_geodes, blueprint, max_ore, max_clay, max_obs, states_in, time):
    i += 1

    # Try to make each robot in turn
    for robot in ["ore", "clay", "obs", "geode"]:

        if robot == "ore":
            ore_id = 1
            robot_id = 5
            max_amnt = max_ore
        elif robot == "clay":
            ore_id = 2
            robot_id = 6
            max_amnt = max_clay
        elif robot == "obs":
            ore_id = 3
            robot_id = 7
            max_amnt = max_obs
        elif robot == "geode":
            ore_id = 4
            robot_id = 8
            max_amnt = None

        values = blueprint[robot]
        ore = values["ore"]
        clay = values["clay"]
        obs = values["obs"]

        states = [state for state in states_in]

        # Determine if it's worth aiming to make this robot
        # No point making it if you can already make max needed resource in a minute
        if robot != "geode":
            if states[robot_id] >= max_amnt:
                continue
        # No point in making if already have as much resource as can be used in remaining time
        if robot != "geode":
            if states[ore_id] >= (time - states[0]) * max_amnt:
                continue
        # No point in making if no robots that can make resource needed (and don't already have enough resource)
        if ore > 0 and states[1] < ore and states[5] == 0:
            continue
        if clay > 0 and states[2] < clay and states[6] == 0:
            continue
        if obs > 0 and states[3] < obs and states[7] == 0:
            continue
        # Check if it's possible to make as many geodes in the time left as we know is the max so far

        # Run time until enough resources to make robot
        while states[0] < time and (not (states[1] >= ore and states[2] >= clay and states[3] >= obs)):
            states[0] += 1  # Add a minute
            # Collect each resource
            states[1] = states[1] + states[5]
            states[2] = states[2] + states[6]
            states[3] = states[3] + states[7]
            states[4] = states[4] + states[8]

        # Once we have enough of the given resource(s), make the robot, if time left
        if states[0] < time:
            states[0] += 1
            states[robot_id] += 1
            states[1] -= ore
            states[2] -= clay
            states[3] -= obs
            states[1] = states[1] + states[5]
            states[2] = states[2] + states[6]
            states[3] = states[3] + states[7]
            states[4] = states[4] + states[8]
            states[robot_id - 4] -= 1

        else:
            if states[4] > max_geodes:
                max_geodes = states[4]
            break

        states, max_geodes = make_robot(i, max_geodes, blueprint, max_ore, max_clay, max_obs, states, time)

    return states, max_geodes


def part(part_no, data):
    if part_no == 1:
        return data, 24
    elif part_no == 2:
        return data[:3], 32


def get_answer(part_no, data):

    subset, time = part(part_no, data)

    quality_level = 0
    part2 = 1

    for line in subset:
        words = line.split(" ")

        blueprint = {
            "id": int(words[1][:-1]),
            "ore": {
                "ore": int(words[6]),
                "clay": 0,
                "obs": 0
            },
            "clay": {
                "ore": int(words[12]),
                "clay": 0,
                "obs": 0
            },
            "obs": {
                "ore": int(words[18]),
                "clay": int(words[21]),
                "obs": 0
            },
            "geode": {
                "ore": int(words[27]),
                "clay": 0,
                "obs": int(words[30])
            }
        }

        # Determine maximum amount of each resource needed in a given minute
        max_ore = max(blueprint["ore"]["ore"], blueprint["clay"]["ore"], blueprint["obs"]["ore"], blueprint["geode"]["ore"])
        max_clay = max(blueprint["ore"]["clay"], blueprint["clay"]["clay"], blueprint["obs"]["clay"],
                       blueprint["geode"]["clay"])
        max_obs = max(blueprint["ore"]["obs"], blueprint["clay"]["obs"], blueprint["obs"]["obs"], blueprint["geode"]["obs"])

        i = 0
        max_geodes = 0

        states, max_geodes = make_robot(i, max_geodes, blueprint, max_ore, max_clay, max_obs, [0, 0, 0, 0, 0, 1, 0, 0, 0],
                                        time)

        # print("ID", blueprint["id"], "final max", max_geodes, "total", blueprint["id"] * max_geodes)

        quality_level += blueprint["id"] * max_geodes

        part2 *= max_geodes

    if part_no == 1:
        return quality_level

    elif part_no == 2:
        return part2

print("\nDay 19")
print("Part 1:", get_answer(1, data))
print("Part 2:", get_answer(2, data))
