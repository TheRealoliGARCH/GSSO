import unittest
from src.gsso_v01 import Edge, MultilayerWorld, Node, Observation, crisis_probability, information_gain, information_value, select_destination, stress_index

class GSSOv01Tests(unittest.TestCase):
    def test_information_gain(self):
        self.assertGreater(information_gain(0.5, 0.9), 0.0)
    def test_information_value_respects_cost(self):
        self.assertGreater(information_value(0.5, 0.9, 1.0), information_value(0.5, 0.9, 2.0))
    def test_destination_selection(self):
        candidates = [Observation("A", 0.9, 2.0), Observation("B", 0.8, 0.5)]
        self.assertEqual(select_destination(0.5, candidates).node, "B")
    def test_stress_index(self):
        self.assertAlmostEqual(stress_index([1.0, 3.0], [1.0, 1.0]), 2.0)
    def test_probability_bounds(self):
        self.assertEqual(crisis_probability(-1.0), 0.0)
        self.assertEqual(crisis_probability(2.0), 1.0)
    def test_multilayer_neighbors(self):
        world = MultilayerWorld([Node("A"), Node("B")], [Edge("A", "B", "trade", 1.0)])
        self.assertEqual(world.neighbors("A"), ["B"])

if __name__ == "__main__":
    unittest.main()
