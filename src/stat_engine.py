import math
from collections import Counter

class StatEngine:
    def __init__(self, data):
        self.data = self._clean_data(data)
        if len(self.data) == 0:
            raise ValueError("Dataset cannot be empty.")

    def _clean_data(self, data):
        if not isinstance(data, (list, tuple)):
            raise TypeError("Input must be a list or tuple.")
        cleaned = []
        for item in data:
            if isinstance(item, (int, float)):
                cleaned.append(item)
            else:
                raise TypeError(f"Invalid data type: {item}")
        return cleaned

    # -------- CENTRAL TENDENCY --------
    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 1:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2

    def get_mode(self):
        counts = Counter(self.data)
        max_freq = max(counts.values())
        if max_freq == 1:
            return "No mode (all values unique)"
        return [k for k, v in counts.items() if v == max_freq]

    # -------- DISPERSION --------
    def get_variance(self, is_sample=True):
        mean = self.get_mean()
        n = len(self.data)
        if is_sample and n < 2:
            raise ValueError("Sample variance needs at least 2 values.")
        denominator = n - 1 if is_sample else n
        return sum((x - mean) ** 2 for x in self.data) / denominator

    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))

    # -------- OUTLIERS --------
    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()
        return [x for x in self.data if abs(x - mean) > threshold * std]