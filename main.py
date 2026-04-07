# main.py
from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes
import json

# Load salary data
with open("data/sample_salaries.json") as f:
    salaries = json.load(f)

# Initialize StatEngine
stats = StatEngine(salaries)

print("Mean:", stats.get_mean())
print("Median:", stats.get_median())
print("Mode:", stats.get_mode())
print("Variance (sample):", stats.get_variance(is_sample=True))
print("Standard Deviation (sample):", stats.get_standard_deviation(is_sample=True))
print("Outliers:", stats.get_outliers())

# Monte Carlo Simulation
days_list = [30, 365, 10000]
for days in days_list:
    crashes, sim_prob = simulate_crashes(days)
    print(f"\nDays: {days}")
    print(f"Total crashes: {crashes}")
    print(f"Simulated probability: {sim_prob:.4f}")