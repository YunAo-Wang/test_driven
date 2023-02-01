import unittest
import Equidistant_sequence


class TestRunner(unittest.TestCase):

    def test_eq(self):
        eq1 = [1, 3, 5, 7, 9]
        eq2 = [2, 4, 6, 8, 10]
        list1 = [2, 4, 8, 18]
        list2 = [3, 6, 9, 24]

        self.assertEqual(Equidistant_sequence.eq_seq(eq1,eq2), True)
        self.assertEqual(Equidistant_sequence.eq_seq(list1,list2), False)


if __name__ == "__main__":
    unittest.main()
