import json

# Read JSON File
with open("cricket_players.json", "r") as file:
    players = json.load(file)

print("\n===== PLAYER STATISTICS =====\n")

for player in players:

    strike_rate = (player["runs"] / player["balls"]) * 100
    average = player["runs"] / player["outs"]

    dismissal_count = {}

    for dismissal in player["dismissals"]:
        dismissal_count[dismissal] = dismissal_count.get(dismissal, 0) + 1

    frequent_dismissal = max(dismissal_count, key=dismissal_count.get)

    print("Player :", player["name"])
    print("Runs :", player["runs"])
    print("Strike Rate :", round(strike_rate, 2))
    print("Average :", round(average, 2))
    print("Better Condition :", player["conditions"])
    print("Frequent Dismissal :", frequent_dismissal)
    print("-" * 40)