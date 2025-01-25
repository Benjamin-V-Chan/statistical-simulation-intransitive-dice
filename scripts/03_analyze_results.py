import pandas as pd

# Load results
results = pd.read_csv("outputs/simulation_results.csv")

# Analyze results
summary = []
for _, row in results.iterrows():
    die1_win_rate = row["Die 1 Wins"] / (row["Die 1 Wins"] + row["Die 2 Wins"])
    die2_win_rate = row["Die 2 Wins"] / (row["Die 1 Wins"] + row["Die 2 Wins"])
    summary.append((row["Die 1"], row["Die 2"], die1_win_rate, die2_win_rate))

# Save summary
with open("outputs/analysis_summary.txt", "w") as f:
    for record in summary:
        f.write(f"{record[0]} vs {record[1]}: {record[2]:.2f} vs {record[3]:.2f}\n")