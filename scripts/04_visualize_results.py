import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Load results
results = pd.read_csv("outputs/simulation_results.csv")

# Visualize win rates
def plot_win_rates(data):
    fig, ax = plt.subplots()
    for _, row in data.iterrows():
        ax.bar(row["Die 1"], row["Die 1 Wins"], label="Die 1 Wins")
        ax.bar(row["Die 2"], row["Die 2 Wins"], label="Die 2 Wins")
    plt.legend()
    plt.savefig("outputs/win_rates.png")

plot_win_rates(results)