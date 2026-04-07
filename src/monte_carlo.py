# src/monte_carlo.py
import random

def simulate_crashes(days, crash_prob=0.045):
    crashes = 0
    for _ in range(days):
        if random.random() < crash_prob:
            crashes += 1
    simulated_prob = crashes / days
    return crashes, simulated_prob