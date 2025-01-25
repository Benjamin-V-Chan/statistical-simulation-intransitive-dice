import json
import csv
import random

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

def generate_intransitive_dice(num_dice, sides):
    dice = []
    for i in range(num_dice):
        die = sorted(random.choices(range(1, sides + 1), k=sides))
        dice.append(die)
    # Shuffle to introduce intransitivity
    for i in range(num_dice - 1):
        dice[i + 1] = sorted(random.choices(range(1, sides + 1), k=sides))
    return dice

# Generate dice
dice = generate_intransitive_dice(config["num_dice"], config["sides_per_die"])

# Save dice to CSV
with open("outputs/dice_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Die", "Values"])
    for i, die in enumerate(dice):
        writer.writerow([f"Die {i + 1}", die])