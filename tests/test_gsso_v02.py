import unittest

from src.gsso_v02 import (
    brier_score,
    false_warning_duration,
    roc_auc,
    total_information_cost,
    warning_lead_time,
)


class GSSOv02Tests(unittest.TestCase):
    def test_brier_score(self):
        self.assertAlmostEqual(brier_score([0, 1], [0.0, 1.0]), 0.0)

    def test_auc_perfect_ranking(self):
        self.assertAlmostEqual(roc_auc([0, 0, 1, 1], [0.1, 0.2, 0.8, 0.9]), 1.0)

    def test_auc_ties(self):
        self.assertAlmostEqual(roc_auc([0, 1], [0.5, 0.5]), 0.5)

    def test_lead_time(self):
        self.assertEqual(warning_lead_time([0, 0, 1], [0.6, 0.4, 0.9]), 2)

    def test_false_warning_duration(self):
        self.assertEqual(false_warning_duration([0, 1, 0], [0.6, 0.7, 0.4]), 1)

    def test_information_cost(self):
        self.assertEqual(total_information_cost([0.5, 0.8, 1.2]), 2.5)


if __name__ == "__main__":
    unittest.main()
