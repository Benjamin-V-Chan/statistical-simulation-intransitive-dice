import csv
import random
from itertools import combinations

# Load dice data
def load_dice(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        return [eval(row[1]) for row in reader]

dice = load_dice("outputs/dice_data.csv")

# Simulate battles
def simulate_battle(die1, die2, trials=1000):
    die1_wins, die2_wins = 0, 0
    for _ in range(trials):
        roll1, roll2 = random.choice(die1), random.choice(die2)
        if roll1 > roll2:
            die1_wins += 1
        elif roll2 > roll1:
            die2_wins += 1
    return die1_wins, die2_wins

# Generate all pair combinations
results = []
for die1, die2 in combinations(dice, 2):
    wins1, wins2 = simulate_battle(die1, die2)
    results.append((str(die1), str(die2), wins1, wins2))

# Save results
with open("outputs/simulation_results.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Die 1", "Die 2", "Die 1 Wins", "Die 2 Wins"])
    writer.writerows(results)