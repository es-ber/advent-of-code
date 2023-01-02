with open('input.txt') as f:
    games = f.read().splitlines()

map_score = {"X": 1, "Y": 2, "Z": 3}

outcomes = {"wins": {"A": "Y", "B": "Z", "C": "X"},
            "draws": {"A": "X", "B": "Y", "C": "Z"},
            "losses": {"A": "Z", "B": "X", "C": "Y"},
            }

scores1 = []
scores2 = []

for game in games:

    opponent = game.split(" ")[0]
    player = game.split(" ")[1]

    win = outcomes["wins"].get(opponent)
    draw = outcomes["draws"].get(opponent)
    loss = outcomes["losses"].get(opponent)

    # Part 1
    if player == win:
        scores1.append(map_score.get(player) + 6)
    elif player == draw:
        scores1.append(map_score.get(player) + 3)
    elif player == loss:
        scores1.append(map_score.get(player))

    # Part 2
    if player == "X":
        scores2.append(map_score.get(loss))
    elif player == "Y":
        scores2.append(map_score.get(draw) + 3)
    elif player == "Z":
        scores2.append(map_score.get(win) + 6)

print("\nDay 2")
print("Part 1:", sum(scores1))
print("Part 2:", sum(scores2))