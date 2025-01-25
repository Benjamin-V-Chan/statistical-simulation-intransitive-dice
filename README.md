# statistical-simulation-intransitive-dice

## Project Overview

This project explores the **Intransitive Dice Paradox**, a fascinating statistical phenomenon where a set of dice exhibits non-transitive relationships. That is, given three dice A, B, and C:

- A beats B with a probability greater than 50%.
- B beats C with a probability greater than 50%.
- Yet, C beats A with a probability greater than 50%.

The paradox challenges our intuition, as it suggests a cyclic superiority among the dice, which contradicts traditional notions of transitivity in probabilities.

### Mathematical Foundation
The probabilities of one die beating another depend on their face values. Given two dice, $D_1 = \{d_{1,1}, d_{1,2}, \dots, d_{1,n}\}$ and $D_2 = \{d_{2,1}, d_{2,2}, \dots, d_{2,n}\}$, the probability of $D_1$ beating $D_2$ is:

$$P(D_1 > D_2) = \frac{1}{n^2} \sum_{i=1}^{n} \sum_{j=1}^{n} \mathbb{I}(d_{1,i} > d_{2,j})$$

Where:
- $n$ is the number of faces per die.
- $\mathbb{I}(d_{1,i} > d_{2,j})$ is an indicator function that equals 1 if $d_{1,i} > d_{2,j}$ and 0 otherwise.

For intransitive dice, the relationships are cyclic, such that:

$$P(A > B) > 0.5, \quad P(B > C) > 0.5, \quad \text{and} \quad P(C > A) > 0.5.$$

To construct such dice, we iteratively adjust the values of the dice to satisfy these relationships. This project generates intransitive dice, simulates their pairwise battles, and analyzes the results to confirm their paradoxical behavior.

---

## Folder Structure
```
project-root/
├── scripts/
│   ├── 01_generate_dice.py       # Script to generate intransitive dice
│   ├── 02_simulate_battles.py    # Simulates dice battles and saves results
│   ├── 03_analyze_results.py     # Analyzes simulation results for intransitivity
│   ├── 04_visualize_results.py   # Visualizes results using graphs
├── outputs/
│   ├── dice_data.csv             # Generated dice values
│   ├── simulation_results.csv    # Simulation results of dice battles
│   ├── analysis_summary.txt      # Summary of intransitivity analysis
│   ├── win_rates.png             # Visualization of win rates
├── README.md                     # Documentation for the project
├── requirements.txt              # Required Python packages
├── config.json                   # Configuration file for simulation settings
```

---

## Usage

### 1. Setup the Project:

1. Clone the repository.
2. Ensure you have Python installed.
3. Install required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 2. Generate Intransitive Dice:

Run the script to generate dice that satisfy intransitive relationships. The dice configurations will be saved in `outputs/dice_data.csv`.

```bash
python scripts/01_generate_dice.py
```

### 3. Simulate Battles:

Run the script to simulate pairwise battles between all dice. Results will be saved in `outputs/simulation_results.csv`.

```bash
python scripts/02_simulate_battles.py
```

### 4. Analyze Results:

Run the script to calculate win rates and confirm the intransitive nature of the dice. A summary will be saved in `outputs/analysis_summary.txt`.

```bash
python scripts/03_analyze_results.py
```

### 5. Visualize Results:

Run the script to create visualizations of the win rates and intransitivity relationships. Plots will be saved in the `outputs/` folder.

```bash
python scripts/04_visualize_results.py
```

---

## Requirements

This project requires the following Python packages:

- pandas
- matplotlib
- networkx

Install all dependencies using:

```bash
pip install -r requirements.txt
```