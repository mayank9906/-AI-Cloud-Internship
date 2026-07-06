import pandas as pd

# Read CSV
df = pd.read_csv("ipl_players.csv")

# Highest Run Scorer
highest_run_scorer = df.loc[df["Runs"].idxmax()]

# Most Wickets
most_wickets = df.loc[df["Wickets"].idxmax()]

# Best Strike Rate
best_strike_rate = df.loc[df["StrikeRate"].idxmax()]

# Team with Most Wins
team_wins = df.groupby("Team")["TeamWins"].max()
best_team = team_wins.idxmax()

print("========== IPL DATA ANALYSIS ==========\n")

print("Highest Run Scorer")
print("--------------------")
print(highest_run_scorer["Player"])
print("Runs:", highest_run_scorer["Runs"])

print("\nMost Wickets")
print("--------------------")
print(most_wickets["Player"])
print("Wickets:", most_wickets["Wickets"])

print("\nBest Strike Rate")
print("--------------------")
print(best_strike_rate["Player"])
print("Strike Rate:", best_strike_rate["StrikeRate"])

print("\nTeam With Most Wins")
print("--------------------")
print(best_team)
print("Wins:", team_wins.max())