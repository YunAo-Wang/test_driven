import unittest
import geometric_sequence


class TestRunner(unittest.TestCase):

    def test_seq(self):
        list1 = [2, 4, 8, 18]
        list2 = [3, 6, 9, 24]

        self.assertEqual(geometric_sequence.geom_seq(list1), 18)
        self.assertEqual(geometric_sequence.geom_seq(list2), 9)


if __name__ == "__main__":
    unittest.main()
