import unittest

from src.gsso_v03 import (
    evaluate_scenarios,
    mean_metric,
    paired_difference,
    scenario_summary,
)


class GSSOv03Tests(unittest.TestCase):
    def test_mean_metric(self):
        self.assertAlmostEqual(mean_metric([1.0, 2.0, 3.0]), 2.0)

    def test_paired_difference(self):
        self.assertAlmostEqual(paired_difference([1.0, 2.0], [2.0, 4.0]), 1.5)

    def test_scenario_summary(self):
        result = scenario_summary([0.2, 0.4], [0.3, 0.5])
        self.assertAlmostEqual(result["baseline_mean"], 0.3)
        self.assertAlmostEqual(result["active_mean"], 0.4)
        self.assertAlmostEqual(result["active_minus_baseline"], 0.1)

    def test_evaluate_scenarios(self):
        def evaluator(name):
            return (0.2, 0.4) if name == "low" else (0.5, 0.7)

        result = evaluate_scenarios(["low", "high"], evaluator)
        self.assertAlmostEqual(result["low"]["active_mean"], 0.4)
        self.assertAlmostEqual(result["high"]["active_minus_baseline"], 0.2)


if __name__ == "__main__":
    unittest.main()
