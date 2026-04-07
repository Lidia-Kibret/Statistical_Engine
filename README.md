# 🧮 Statistical Engine Project

## 📊 Project Overview

Statistical Engine is a pure Python project that allows you to analyze numerical datasets and perform statistical calculations from scratch.

### Key capabilities:

➡️ Compute mean, median, and mode (handles multimodal distributions and unique datasets).

➡️ Compute variance and standard deviation with options for sample or population calculations.

➡️ Detect outliers based on a configurable number of standard deviations.

➡️ Run Monte Carlo simulations to estimate server crash probabilities and demonstrate the Law of Large Numbers (LLN).

---

## 📐 Mathematical Logic

### Central Tendency

➡️ Mean: Sum of all values divided by the number of values.

➡️ Median: If the dataset length is odd, the middle value. If even, the average of the two middle values.

➡️ Mode: The most frequent value(s). Returns a list for multimodal datasets or a message if all values are unique.

### Dispersion

➡️ Variance: Measures spread from the mean.

➡️ Standard Deviation: Square root of variance.

### Outliers

➡️ Any value greater than threshold × standard deviation away from the mean is considered an outlier.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository:

```bash
git clone https://github.com/Lidia-Kibret/Statistical_Engine.git
cd Statistical_Engine

```


### 2️⃣ Run the main analysis:

```bash
python3 main.py
```
---

## 🧪 Testing

### 1. Run unit tests using Python’s unittest framework:

```bash
python3 -m unittest discover tests
```

### 2. Tests include:

➡️ Correct calculation of mean, median, and mode.

➡️ Handling of empty lists (graceful errors).

➡️ Sample vs. population variance and standard deviation.

➡️ Outlier detection.


## ✅ Acceptance Criteria Checklist

 ✔️ Handles empty datasets gracefully.
 
 ✔️ Cleans or raises errors for mixed data types.
 
 ✔️ Correctly computes mean, median, mode.
 
 ✔️ Correctly computes sample and population variance.
 
 ✔️ Correctly computes standard deviation.
 
 ✔️ Detects outliers using standard deviation thresholds.
 
 ✔️ Monte Carlo simulation approximates server crash probability accurately.
 
 ✔️ Code is organized with src/ and tests/ folders.




