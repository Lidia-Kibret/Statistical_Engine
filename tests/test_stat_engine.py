# tests/test_stat_engine.py
import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):

    def test_mean_median_mode(self):
        data = [1, 2, 2, 3, 4]
        stats = StatEngine(data)
        self.assertEqual(stats.get_mean(), 2.4)
        self.assertEqual(stats.get_median(), 2)
        self.assertEqual(stats.get_mode(), [2])

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    def test_standard_deviation(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        stats = StatEngine(data)
        self.assertAlmostEqual(stats.get_standard_deviation(is_sample=True), 2.138, places=3)

if __name__ == "__main__":
    unittest.main()