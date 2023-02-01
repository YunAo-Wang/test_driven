import unittest
import Equidistant_sequence_n


class TestRunner(unittest.TestCase):

    def test_eq(self):
        eq1 = [1, 3, 5, 7, 9, 213, 23, 213, 123, 123, 334, 3]
        eq2 = [2, 4, 6, 8, 10]
        eq3 = [2, 4, 8, 18]
        eq4 = [3, 6, 9, 24]

        self.assertEqual(Equidistant_sequence_n.is_eq(eq1), (False,[213, 23, 213, 123, 123, 334, 3]))
        self.assertEqual(Equidistant_sequence_n.is_eq(eq2), None)
        self.assertEqual(Equidistant_sequence_n.is_eq(eq3), (False,[8, 18]))
        self.assertEqual(Equidistant_sequence_n.is_eq(eq4), (False,[24]))


if __name__ == "__main__":
    unittest.main()
